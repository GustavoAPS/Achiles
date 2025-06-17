from app.database import get_connection
from app.database import get_all_weight_records
from app.database import get_all_run_records
# from app.models.weight_record import WeightRecord
from app.models.run_record import RunRecord


class HermesService:
    def __init__(self) -> None:
        pass

    def create_weight_record(self):
        conn = get_connection()
        cursor = conn.cursor()

        # Format: YYYY-MM-DD
        cursor.execute("""
        INSERT INTO weight_records (weight_kg, record_date)
        VALUES (?, ?)
        """, (86.8, '9999-12-31'))
        conn.commit()
        conn.close()
        return "New record created"

    def get_weight_record(self):
        pass

    def get_all_weight_records(self):
        return get_all_weight_records()

    def update_weight_record(self):
        pass

    def delete_wight_record():
        pass

    def create_run_record(self, run_record: RunRecord):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS run_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            duration_seconds INTEGER NOT NULL,
            distance_km DOUBLE NOT NULL,
            record_date DATE NOT NULL
        );
        """)
        conn.commit()
        # Format: YYYY-MM-DD
        cursor.execute("""
        INSERT INTO run_records (duration_seconds, distance_km, record_date)
        VALUES (?, ?, ?)
        """, (run_record.duration_seconds,
              run_record.distance_km,
              run_record.day))

        conn.commit()
        conn.close()

        return "New run record created"

    def get_all_run_records(self):
        return get_all_run_records()  # imported from database.py
