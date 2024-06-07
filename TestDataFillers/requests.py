import os
import random
import psycopg2
from datetime import datetime, timedelta


num_records=100
time_to_connect = 30

time = datetime.now()

# Database connection parameters
db_params = {
    'dbname': os.getenv("POSTGRES_DB"),
    'user': os.getenv("POSTGRES_USER"),
    'password': os.getenv("POSTGRES_PASSWORD"),
    'host': 'postgres',
    'port': os.getenv("PORT")
}

# Connect to PostgreSQL
try:
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    # Execute SQL commands directly
    def execute_sql(sql_command):
        cursor.execute(sql_command)
        connection.commit()
    query1 = ("""SELECT Tank_ID, SUM((case
    when Gun_ID > 10 and Gun_ID < 100 then 1
    when Gun_ID <= 10 or Gun_ID >= 100 then 0
    end)+(case
    when Turret_ID > 10 and Turret_ID < 100 then 1
    when Turret_ID <= 10 or Turret_ID >= 100 then 0
    end))
                FROM Tank_status
                where Tank_ID in
              (SELECT Tank_ID
                FROM Tank_status
                GROUP BY Tank_ID
                ORDER BY COUNT(*) DESC
                fetch first 3 rows only)
                AND
                Status = 1
                GROUP BY Tank_ID;""")
    execute_sql(query1)
    table = cursor.fetchall()
    print("Most popular tank components")
    for row in table:
        print(row[0],row[1])

    query1 = ("""SELECT Turret_ID
            FROM Tank_status
            where Tank_ID < 50 AND  Status = 1
            GROUP BY Turret_ID
		    ORDER BY COUNT(*) DESC
		    LIMIT 1;""")
    execute_sql(query1)
    table = cursor.fetchall()
    print("Most popular Turrets")
    for row in table:
        print(row[0])

    query1 = ("""SELECT Client_ID
            FROM Client_Replay
            GROUP BY Client_ID
		    ORDER BY COUNT(*) DESC
		    LIMIT 5;""")
    execute_sql(query1)
    table = cursor.fetchall()
    print("Most active Players")
    for row in table:
        print(row[0])

except (Exception, psycopg2.DatabaseError) as error:
    print(f"Error: {error}")

finally:
    if connection:
        cursor.close()
        connection.close()