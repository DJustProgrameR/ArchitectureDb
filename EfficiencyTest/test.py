import datetime
import os
import time
import re

import psycopg2


def connect_db():
    return psycopg2.connect(
        host="postgres",
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        port=os.getenv("PORT"),
    )


def run_explain_analyze(query, attempts):
    costs = []
    with connect_db() as conn:
        with conn.cursor() as cursor:
            for _ in range(attempts):
                cursor.execute(f"EXPLAIN ANALYZE {query}")
                result = cursor.fetchall()
                if "cost=" in result[0][0]:
                    # Extracting the total cost value from each row
                    cost_part = re.search(r'cost=(\d+\.\d+)\.\.(\d+\.\d+)', result[0][0])
                    end_cost = float(cost_part.group(2))
                costs.append(end_cost)
    return costs


def write_results(query_name, costs):
    if costs:
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        filepath = f"/src/results/{timestamp}_{query_name}.txt"
        with open(filepath, 'w') as file:
            file.write(f"Query: {query_name}\n")
            file.write(f"Best Case: {min(costs)}\n")
            file.write(f"Average Case: {sum(costs) / len(costs)}\n")
            file.write(f"Worst Case: {max(costs)}\n")
    else:
        print(f"No costs were recorded for query {query_name}.")


def wait_for_db():
    retries = 5
    while retries > 0:
        try:
            conn = connect_db()
            conn.close()
            return True
        except psycopg2.OperationalError:
            retries -= 1
            print("Database not ready yet, waiting...")
            time.sleep(10)
    raise Exception("Database not available")


if __name__ == "__main__":
    wait_for_db()

    queries = [
        {
            "name": "Most popular Tanks components usage",
            "query": """SELECT Tank_ID, SUM((case
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
                GROUP BY Tank_ID;"""
        },
        {
            "name": "Most popular Turret_ID",
            "query": """SELECT Turret_ID
            FROM Tank_status
            where Tank_ID < 50 AND  Status = 1
            GROUP BY Turret_ID
		    ORDER BY COUNT(*) DESC
		    LIMIT 1;"""
        },
        {
            "name": "Most active Gamers",
            "query": """SELECT Client_ID
            FROM Client_Replay
            GROUP BY Client_ID
		    ORDER BY COUNT(*) DESC
		    LIMIT 5;"""
        }
    ]

    attempts = int(os.getenv("ATTEMPTS", 3))

    for query in queries:
        costs = run_explain_analyze(query["query"], attempts)
        write_results(query["name"], costs)

    print("All tests passed!")