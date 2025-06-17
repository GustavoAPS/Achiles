import datetime
from pydantic import BaseModel, Field


class RunRecord(BaseModel):
    day: datetime.date
    duration_seconds: int = Field(ge=0)
    distance_km: float

    @property
    def as_timedelta(self) -> datetime.timedelta:
        return datetime.timedelta(second=self.duration_seconds)

    @property
    def hours_minutes_seconds(self):
        """Return as hours minutes and seconds"""
        hours, remainder = divmod(self.duration_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return hours, minutes, seconds
