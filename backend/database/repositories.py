from __future__ import annotations

from dataclasses import replace
from typing import Iterable

from .database import Database
from .models import APPLICATION_STATUSES, Application


class RecordNotFoundError(LookupError):
    """Raised when a requested database record does not exist."""


class ApplicationRepository:
    """Persists and retrieves application-tracker records."""

    def __init__(self, database: Database) -> None:
        self.database = database
        self.database.initialize()

    def create(self, application: Application) -> Application:
        if application.id is not None:
            raise ValueError("New applications must not already have an id.")

        query = """
            INSERT INTO applications (
                company,
                job_title,
                status,
                job_url,
                notes,
                applied_on,
                created_at,
                updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """

        with self.database.transaction() as connection:
            cursor = connection.execute(query, application.insert_values())

        return replace(application, id=cursor.lastrowid)

    def get(self, application_id: int) -> Application:
        with self.database.connect() as connection:
            row = connection.execute(
                "SELECT * FROM applications WHERE id = ?",
                (application_id,),
            ).fetchone()

        if row is None:
            raise RecordNotFoundError(
                f"Application with id {application_id} was not found."
            )

        return Application.from_row(row)

    def list(
        self,
        *,
        status: str | None = None,
        search: str | None = None,
    ) -> list[Application]:
        clauses: list[str] = []
        values: list[str] = []

        if status is not None:
            if status not in APPLICATION_STATUSES:
                raise ValueError(f"Unknown application status: {status}")
            clauses.append("status = ?")
            values.append(status)

        if search:
            clauses.append("(company LIKE ? OR job_title LIKE ?)")
            pattern = f"%{search.strip()}%"
            values.extend((pattern, pattern))

        where_clause = f"WHERE {' AND '.join(clauses)}" if clauses else ""

        query = f"""
            SELECT *
            FROM applications
            {where_clause}
            ORDER BY applied_on DESC, company COLLATE NOCASE, id DESC
        """

        with self.database.connect() as connection:
            rows = connection.execute(query, values).fetchall()

        return [Application.from_row(row) for row in rows]

    def update(self, application: Application) -> Application:
        if application.id is None:
            raise ValueError("An application id is required for updates.")

        query = """
            UPDATE applications
            SET
                company = ?,
                job_title = ?,
                status = ?,
                job_url = ?,
                notes = ?,
                applied_on = ?,
                updated_at = ?
            WHERE id = ?
        """

        values = (*application.update_values(), application.id)

        with self.database.transaction() as connection:
            cursor = connection.execute(query, values)

        if cursor.rowcount == 0:
            raise RecordNotFoundError(
                f"Application with id {application.id} was not found."
            )

        return self.get(application.id)

    def save(self, application: Application) -> Application:
        if application.id is None:
            return self.create(application)

        return self.update(application)

    def delete(self, application_id: int) -> None:
        with self.database.transaction() as connection:
            cursor = connection.execute(
                "DELETE FROM applications WHERE id = ?",
                (application_id,),
            )

        if cursor.rowcount == 0:
            raise RecordNotFoundError(
                f"Application with id {application_id} was not found."
            )

    def update_status(self, application_id: int, status: str) -> Application:
        application = self.get(application_id)

        updated_application = replace(application, status=status)
        updated_application.__post_init__()

        return self.update(updated_application)

    def count_by_status(self) -> dict[str, int]:
        counts = {status: 0 for status in APPLICATION_STATUSES}

        with self.database.connect() as connection:
            rows = connection.execute(
                """
                SELECT status, COUNT(*) AS total
                FROM applications
                GROUP BY status
                """
            ).fetchall()

        for row in rows:
            counts[row["status"]] = row["total"]

        return counts

    def delete_many(self, application_ids: Iterable[int]) -> int:
        ids = tuple(application_ids)

        if not ids:
            return 0

        placeholders = ", ".join("?" for _ in ids)

        with self.database.transaction() as connection:
            cursor = connection.execute(
                f"DELETE FROM applications WHERE id IN ({placeholders})",
                ids,
            )

        return cursor.rowcount