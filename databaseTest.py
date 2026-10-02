import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        database="Attendace",
        user="postgres",
        password="vansie@1234",
        port="5432"
    )

    print("Database connected successfully!")

    connection.close()

except Exception as e:
    print("Database connection failed!")
    print(e)