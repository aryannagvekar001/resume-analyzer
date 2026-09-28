from __future__ import annotations

import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Generator


class Database:
    """Creates SQLite connections and initializes the application-tracker schema."""

    def __init__(self, database_path: str | Path | None = None) -> None:
        self.database_path = Path(database_path or "resume_analyzer.db")

    def connect(self) -> sqlite3.Connection:
        self.database_path.parent.mkdir(parents=True, exist_ok=True)

        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        return connection

    def initialize(self) -> None:
        with self.connect() as connection:
            connection.executescript(
                """
                CREATE TABLE IF NOT EXISTS applications (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    company TEXT NOT NULL,
                    job_title TEXT NOT NULL,
                    status TEXT NOT NULL,
                    job_url TEXT NOT NULL DEFAULT '',
                    notes TEXT NOT NULL DEFAULT '',
                    applied_on TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                );

                CREATE INDEX IF NOT EXISTS idx_applications_status
                ON applications(status);

                CREATE INDEX IF NOT EXISTS idx_applications_company
                ON applications(company COLLATE NOCASE);

                CREATE INDEX IF NOT EXISTS idx_applications_applied_on
                ON applications(applied_on DESC);
                """
            )

    @contextmanager
    def transaction(self) -> Generator[sqlite3.Connection, None, None]:
        connection = self.connect()

        try:
            connection.execute("BEGIN")
            yield connection
            connection.commit()
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()