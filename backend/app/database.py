import sqlite3

DB_NAME = "data.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Acessar os resultados como dicionário
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS weight_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        weight_kg DOUBLE NOT NULL,
        record_date DATE NOT NULL
    );
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS run_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        duration_seconds INTEGER NOT NULL,
        distance_km DOUBLE NOT NULL,
        record_date DATE NOT NULL
    );
    """)

    conn.commit()
    conn.close()


def get_all_weight_records():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM weight_records")
    rows = cursor.fetchall()  # Lista de objetos `sqlite.Row`

    conn.close()
    return [dict(row) for row in rows]


def get_all_run_records():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM run_records")
    rows = cursor.fetchall()

    conn.close()
    return [dict(row) for row in rows]
