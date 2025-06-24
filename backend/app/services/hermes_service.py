from app.database import get_connection
from app.database import get_all_run_records
from app.models.run_record import RunRecord
from app.models.weight_record import WeightRecord


class HermesService:
    def __init__(self) -> None:
        pass

    def create_weight_record(self, weight_record: WeightRecord):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO weight_records (weight_kg, record_date)
        VALUES (?, ?)
        """, (weight_record.weight_kg, weight_record.record_date))
        conn.commit()
        conn.close()

    def get_all_weight_records(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM weight_records")
        rows = cursor.fetchall()  # Lista de objetos `sqlite.Row`

        conn.close()
        return [dict(row) for row in rows]

    def update_weight_record(
            self,
            weight_record_id: int,
            weight_record: WeightRecord
    ):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE weight_records
            Set weight_kg = ?, record_date = ?
            WHERE id = ?
        """, (weight_record.weight_kg, weight_record.record_date, weight_record_id))
        conn.commit()
        conn.close()

    def delete_weight_record(self, weight_record_id: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM weight_records
            WHERE id = ?
        """, (weight_record_id,))
        conn.commit()
        conn.close()
        return {"msg": "user deleted"}

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
              run_record.record_date))

        conn.commit()
        conn.close()

        return "New run record created"

    def get_all_run_records(self):
        return get_all_run_records()  # imported from database.py
