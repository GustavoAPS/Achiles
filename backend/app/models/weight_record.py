import datetime
from pydantic import BaseModel


class WeightRecord(BaseModel):
    record_date: datetime.date
    weight_kg: float

# import datetime

# # today = datetime.date(2024, 6, 9)
# today = datetime.date.today()

# print(today)
