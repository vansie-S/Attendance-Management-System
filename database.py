import psycopg2
from datetime import date, datetime


# Connect to PostgreSQL
def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="Attendace",
        user="postgres",
        password="vansie@1234",
        port="5432"
    )


# Mark attendance
def mark_attendance(student_id):

    conn = get_connection()
    cursor = conn.cursor()

    try:
        query = """
        INSERT INTO attendance
        (student_id, date, time, status)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (student_id, date)
        DO NOTHING;
        """

        today = date.today()
        current_time = datetime.now().time()

        cursor.execute(
            query,
            (student_id, today, current_time, "Present")
        )

        conn.commit()

        if cursor.rowcount == 1:
            print("Attendance marked!")
        else:
            print("Attendance already marked today!")

    except Exception as e:
        print("Database error:", e)
        conn.rollback()

    finally:
        cursor.close()
        conn.close()