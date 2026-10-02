from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from typing import Any, Mapping


APPLICATION_STATUSES = (
    "Applied",
    "Interview",
    "Offer",
    "Rejected",
    "Withdrawn",
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _today() -> str:
    return date.today().isoformat()


@dataclass(slots=True)
class Application:
    company: str
    job_title: str
    status: str = "Applied"
    job_url: str = ""
    notes: str = ""
    applied_on: str = field(default_factory=_today)
    id: int | None = None
    created_at: str = field(default_factory=_utc_now)
    updated_at: str = field(default_factory=_utc_now)

    def __post_init__(self) -> None:
        self.company = self.company.strip()
        self.job_title = self.job_title.strip()
        self.status = self.status.strip()
        self.job_url = self.job_url.strip()
        self.notes = self.notes.strip()
        self.applied_on = self.applied_on.strip()

        if not self.company:
            raise ValueError("Company is required.")

        if not self.job_title:
            raise ValueError("Job title is required.")

        if self.status not in APPLICATION_STATUSES:
            valid_statuses = ", ".join(APPLICATION_STATUSES)
            raise ValueError(f"Status must be one of: {valid_statuses}.")

        try:
            date.fromisoformat(self.applied_on)
        except ValueError as error:
            raise ValueError("Applied date must use YYYY-MM-DD format.") from error

    @classmethod
    def from_row(cls, row: Mapping[str, Any]) -> "Application":
        return cls(
            id=row["id"],
            company=row["company"],
            job_title=row["job_title"],
            status=row["status"],
            job_url=row["job_url"],
            notes=row["notes"],
            applied_on=row["applied_on"],
            created_at=row["created_at"],
            updated_at=row["updated_at"],
        )

    def insert_values(self) -> tuple[str, str, str, str, str, str, str, str]:
        return (
            self.company,
            self.job_title,
            self.status,
            self.job_url,
            self.notes,
            self.applied_on,
            self.created_at,
            self.updated_at,
        )

    def update_values(self) -> tuple[str, str, str, str, str, str, str]:
        return (
            self.company,
            self.job_title,
            self.status,
            self.job_url,
            self.notes,
            self.applied_on,
            _utc_now(),
        )