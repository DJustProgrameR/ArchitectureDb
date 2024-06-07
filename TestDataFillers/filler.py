import os
import random
import psycopg2
from datetime import datetime, timedelta

num_main_records = int(os.getenv('NUM_MAIN_RECORDS'))
num_tank_records = int(os.getenv('NUM_TANK_RECORDS'))
num_other_records = int(os.getenv('NUM_OTHER_RECORDS'))
num_records=100
time_to_connect = 30

time = datetime.now()
# Open and read the file
# Function to generate a random integer between a specified range
def random_integer(min_val, max_val):
    return random.randint(min_val, max_val)

# Function to generate a random string of specified length
def random_string(length):
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=length))

# Function to generate a random email address
def random_email(length):
    return random_string(length) + '@example.com'

# Function to choose a random ENUM value
def random_enum(options):
    return random.choice(options)
def random_integer_array(size, min_val, max_val):
    array = [random.randint(min_val, max_val) for _ in range(size)]
    return array
def random_ip():
    ip_parts = [str(random.randint(0, 255)) for _ in range(4)]
    return ".".join(ip_parts)
def random_boolean():
    return random.choice([True, False])

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

    TABLE_NAME = "Client"
    query1 = (f"""SELECT COUNT(*) FROM {TABLE_NAME};""")
    execute_sql(query1)
    count = cursor.fetchone()[0]
    if count == 0:
        NUM_ROWS = num_main_records
        for i in range(1, NUM_ROWS + 1):
            email = random_email(10)
            password = random_integer(100000, 999999)
            silver = random_integer(0, 100)
            gold = random_integer(0, 100)
            general_experience = random_integer(0, 100)
            banned = random_boolean()
            execute_sql(f"INSERT INTO {TABLE_NAME} (Email, Password, Silver, Gold, General_experience, Banned) VALUES ('{email}', '{password}', {silver}, {gold}, {general_experience}, {banned});")
    print("Client generated")

    TABLE_NAME = "Map"
    query1 = (f"""SELECT COUNT(*) FROM {TABLE_NAME};""")
    execute_sql(query1)
    count = cursor.fetchone()[0]
    if count == 0:
        NUM_ROWS = num_other_records
        for i in range(1, NUM_ROWS + 1):
            description = random_string(20)
            min_level = random_integer(1, 10)
            max_level = random_integer(11, 20)
            model_filepath = random_string(32)
            execute_sql(f"""INSERT INTO {TABLE_NAME} (Description, Min_level, Max_level, "3D_model_filepath")
                VALUES ('{description}', {min_level}, {max_level}, '{model_filepath}');""")
    print("Map generated")

    TABLE_NAME = "Replay"
    query1 = (f"""SELECT COUNT(*) FROM {TABLE_NAME};""")
    execute_sql(query1)
    count = cursor.fetchone()[0]
    if count == 0:
        NUM_ROWS = num_other_records
        for i in range(1, NUM_ROWS + 1):
            map_id = random_integer(1, num_other_records)
            video_filepath = random_string(32)
            execute_sql(f"INSERT INTO {TABLE_NAME} (Map_ID, Video_filepath) VALUES ({map_id}, '{video_filepath}');")
    print("Replay generated")

    TABLE_NAME = "Skill"
    query1 = (f"""SELECT COUNT(*) FROM {TABLE_NAME};""")
    execute_sql(query1)
    count = cursor.fetchone()[0]
    if count == 0:
        NUM_ROWS = num_other_records
        for i in range(1, NUM_ROWS + 1):
            research_price = random_integer(100, 1000)
            description = random_string(50)
            image_filepath = random_string(32)
            execute_sql(f"INSERT INTO {TABLE_NAME} (Research_price, Description, Image_filepath) VALUES ({research_price}, '{description}', '{image_filepath}');")
    print("Skill generated")

    TABLE_NAME = "Role"
    query1 = (f"""SELECT COUNT(*) FROM {TABLE_NAME};""")
    execute_sql(query1)
    count = cursor.fetchone()[0]
    if count == 0:
        NUM_ROWS = num_other_records
        for i in range(1, NUM_ROWS + 1):
            description = random_string(50)
            execute_sql(f"INSERT INTO {TABLE_NAME} (Description) VALUES ('{description}');")
    print("Role generated")

    TABLE_NAME = "Crew"
    query1 = (f"""SELECT COUNT(*) FROM {TABLE_NAME};""")
    execute_sql(query1)
    count = cursor.fetchone()[0]
    if count == 0:
        NUM_ROWS = num_other_records
        for i in range(1, NUM_ROWS + 1):
            client_id = random_integer(1, num_main_records)
            name = random_string(10)
            skill_id_1 = random_integer(1, num_other_records)
            skill_id_2 = random_integer(1, num_other_records)
            skill_id_3 = random_integer(1, num_other_records)
            image_filepath = random_string(32)
            role_id = random_integer(1, num_other_records)
            execute_sql(f"INSERT INTO {TABLE_NAME} (Client_ID, Name, Skill_ID_1, Skill_ID_2, Skill_ID_3, Image_filepath, Role_ID) VALUES ({client_id}, '{name}', {skill_id_1}, {skill_id_2}, {skill_id_3}, '{image_filepath}', {role_id});")
    print("Crew generated")

    TABLE_NAME = "Equipment"
    query1 = (f"""SELECT COUNT(*) FROM {TABLE_NAME};""")
    execute_sql(query1)
    count = cursor.fetchone()[0]
    if count == 0:
        NUM_ROWS = num_other_records
        for i in range(1, NUM_ROWS + 1):
            purchase_price = random_integer(100, 1000)
            equip_type = random_enum(['REP', 'MED', 'FIRE'])
            execute_sql(f"INSERT INTO {TABLE_NAME} (Purchase_price, Equip_type) VALUES ({purchase_price}, '{equip_type}');")
    print("Equipment generated")

    TABLE_NAME = "Gun"
    query1 = (f"""SELECT COUNT(*) FROM {TABLE_NAME};""")
    execute_sql(query1)
    count = cursor.fetchone()[0]
    if count == 0:
        NUM_ROWS = num_other_records
        for i in range(1, NUM_ROWS + 1):
            mass = random_integer(1, 100)
            model_filepath = random_string(32)
            damage = random_integer(1, 100)
            image_filepath = random_string(32)
            execute_sql(f"""INSERT INTO {TABLE_NAME} (Mass, "3D_model_filepath", Damage, Image_filepath) VALUES ({mass}, '{model_filepath}', {damage}, '{image_filepath}');""")
    print("Gun generated")

    TABLE_NAME = "Tank"
    query1 = (f"""SELECT COUNT(*) FROM {TABLE_NAME};""")
    execute_sql(query1)
    count = cursor.fetchone()[0]
    if count == 0:
        NUM_ROWS = num_tank_records
        for i in range(1, NUM_ROWS + 1):
            level = random_integer(1, 10)
            mass = random_integer(100, 1000)
            power = random_integer(100, 1000)
            ratio = random_integer(1, 100)
            max_load = random_integer(1000, 2000)
            model_filepath = random_string(32)
            purchase_price = random_integer(1000, 2000)
            research_price = random_integer(1000, 2000)
            image_filepath = random_string(32)
            table_position = random_integer(1, 10)
            table_next_position = random_integer(1, 10)
            execute_sql(f"""INSERT INTO {TABLE_NAME} (Level, Mass, Power, Ratio, Max_load, "3D_model_filepath", Purchase_price, Research_price, Image_filepath, Table_position, Table_next_position) \
                VALUES ({level}, {mass}, {power}, {ratio}, {max_load}, '{model_filepath}', {purchase_price}, {research_price}, '{image_filepath}', {table_position}, {table_next_position});""")
    print("Tank generated")

    TABLE_NAME = "Shell"
    query1 = (f"""SELECT COUNT(*) FROM {TABLE_NAME};""")
    execute_sql(query1)
    count = cursor.fetchone()[0]
    if count == 0:
        NUM_ROWS = num_other_records
        for i in range(1, NUM_ROWS + 1):
            price = random_integer(100, 1000)
            penetration = random_integer(100, 1000)
            shell_type = random_enum(['AP', 'AC', 'HE', 'HEAT'])
            max_ricochet_angle = random_integer(30, 60)
            image_filepath = random_string(32)
            execute_sql(f"INSERT INTO {TABLE_NAME} (Price, Penetration, Shell_type, Max_ricochet_angle, Image_filepath) VALUES ({price}, {penetration}, '{shell_type}', {max_ricochet_angle}, '{image_filepath}');")
    print("Shell generated")

    TABLE_NAME = "Turret"
    query1 = (f"""SELECT COUNT(*) FROM {TABLE_NAME};""")
    execute_sql(query1)
    count = cursor.fetchone()[0]
    if count == 0:
        NUM_ROWS = num_other_records
        for i in range(1, NUM_ROWS + 1):
            research_price = random_integer(1, 1000)
            purchase_price = random_integer(1000, 2000)
            mass = random_integer(1, 100)
            model_filepath = random_string(32)
            image_filepath = random_string(32)
            execute_sql(f"""INSERT INTO {TABLE_NAME} (Research_price, Purchase_price, Mass, "3D_model_filepath", Image_filepath) VALUES ({research_price}, {purchase_price}, {mass}, '{model_filepath}', '{image_filepath}');""")
    print("Turret generated")

    TABLE_NAME = "Login_log"
    query1 = (f"""SELECT COUNT(*) FROM {TABLE_NAME};""")
    execute_sql(query1)
    count = cursor.fetchone()[0]
    if count == 0:
        NUM_ROWS = num_other_records
        for i in range(1, NUM_ROWS + 1):
            time = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d")
            ip = random_ip()
            device_type = random.choice(['LAPTOP', 'PC', 'PHONE'])
            execute_sql(f"INSERT INTO {TABLE_NAME} (Time, IP, Device_type) VALUES ('{time}', '{ip}', '{device_type}');")
    print("Login_log generated")

    TABLE_NAME = "Moderator"
    query1 = (f"""SELECT COUNT(*) FROM {TABLE_NAME};""")
    execute_sql(query1)
    count = cursor.fetchone()[0]
    if count == 0:
        NUM_ROWS = num_other_records
        for i in range(1, NUM_ROWS + 1):
            email = f"{random_string(8)}@example.com"
            password = random_string(8)
            execute_sql(f"INSERT INTO {TABLE_NAME} (Email, Password) VALUES ('{email}', '{password}');")
    print("Moderator generated")

    TABLE_NAME = "Gun_Turret_Tank"
    query1 = (f"""SELECT COUNT(*) FROM {TABLE_NAME};""")
    execute_sql(query1)
    count = cursor.fetchone()[0]
    if count == 0:
        NUM_ROWS = num_tank_records
        for i in range(1, NUM_ROWS + 1):
            for j in range (1, random_integer(2, 4)):
                while True:
                    gun_id = random_integer(1, num_other_records)
                    tank_id = i
                    turret_id = random_integer(1, num_other_records)
                    cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE Gun_ID = {gun_id} AND Tank_ID = {tank_id} AND Turret_ID = {turret_id}")
                    if cursor.fetchone() is None:
                        break
                angle_up = random_integer_array(5, 1, 90)
                angle_down = random_integer_array(5, -90, -1)
                angle_up_str='{'+f"{angle_up[0]},"+f"{angle_up[1]},"+f"{angle_up[2]},"+f"{angle_up[3]},"+f"{angle_up[4]}"+'}'
                angle_down_str='{'+f"{angle_down[0]},"+f"{angle_down[1]},"+f"{angle_down[2]},"+f"{angle_down[3]},"+f"{angle_down[4]}"+'}'
                execute_sql(f"""INSERT INTO {TABLE_NAME} (Gun_ID, Tank_ID, Turret_ID, Angle_up, Angle_down) VALUES ({gun_id}, {tank_id}, {turret_id}, '{angle_up_str}', '{angle_down_str}');""")
    print("Gun_Turret_Tank generated")

    TABLE_NAME = "Gun_equip_status"
    query1 = (f"""SELECT COUNT(*) FROM {TABLE_NAME};""")
    execute_sql(query1)
    count = cursor.fetchone()[0]
    if count == 0:
        NUM_ROWS = num_main_records
        for client_id in range(1, NUM_ROWS + 1):
            for tank_id in range(1, num_tank_records + 1):
                query1 = (f"""SELECT DISTINCT Gun_ID FROM Gun_Turret_Tank WHERE Tank_ID = {tank_id};""")
                execute_sql(query1)
                table = cursor.fetchall()
                guns=[]
                for row in table:
                    guns.append(row[0])
                status_var=1
                for k in guns:
                    gun_id = k

                    status = status_var
                    if status_var==1:
                        status_var=0
                    table_position = random_integer(1, 10)
                    table_prev_position = random_integer(1, 10)
                    execute_sql(f"INSERT INTO {TABLE_NAME} (Gun_ID, Client_ID, Tank_ID, Status, Table_position, Table_prev_position) VALUES ({gun_id}, {client_id}, {tank_id}, {status}, {table_position}, {table_prev_position});")
    print("Gun_equip_status generated")

    TABLE_NAME = "Turret_equip_status"
    query1 = (f"""SELECT COUNT(*) FROM {TABLE_NAME};""")
    execute_sql(query1)
    count = cursor.fetchone()[0]
    if count == 0:
        for client_id in range(1, num_main_records + 1):
            for tank_id in range(1, num_tank_records + 1):
                query1 = (f"""SELECT DISTINCT Turret_ID FROM Gun_Turret_Tank WHERE Tank_ID = {tank_id};""")
                execute_sql(query1)
                table = cursor.fetchall()
                turrets=[]
                for row in table:
                    turrets.append(row[0])
                status_var=1
                for k in turrets:
                    turret_id = k

                    status = status_var
                    if status_var==1:
                        status_var=0
                    table_position = random_integer(1, 10)
                    table_prev_position = random_integer(1, 10)
                    execute_sql(f"INSERT INTO {TABLE_NAME} (Turret_ID, Client_ID, Tank_ID, Status, Table_position, Table_prev_position) VALUES ({turret_id}, {client_id}, {tank_id}, {status}, {table_position}, {table_prev_position});")
    print("Turret_equip_status generated")

    TABLE_NAME = "Tank_status"
    query1 = (f"""SELECT COUNT(*) FROM {TABLE_NAME};""")
    execute_sql(query1)
    count = cursor.fetchone()[0]
    if count == 0:
        for client_id in range(1, num_main_records + 1):
            for tank_id in range(1, num_tank_records + 1):
                experience = random_integer(1, 100)
                status=random_integer(0, 1)
                shell_id = random_integer(1, num_other_records)
                equiped_amount = random_integer(1, 100)
                query1 = (f"""SELECT Gun_ID FROM Gun_equip_status WHERE Tank_ID = {tank_id} AND Client_ID = {client_id} AND Status = 1;""")
                execute_sql(query1)
                gun_id = cursor.fetchone()[0]
                query1 = (f"""SELECT Turret_ID FROM Turret_equip_status WHERE Tank_ID = {tank_id} AND Client_ID = {client_id} AND Status = 1;""")
                execute_sql(query1)
                turret_id = cursor.fetchone()[0]
                crew_id_1 = random_integer(1, num_other_records)
                crew_id_2 = random_integer(1, num_other_records)
                crew_id_3 = random_integer(1, num_other_records)
                crew_id_4 = random_integer(1, num_other_records)
                crew_id_5 = random_integer(1, num_other_records)
                crew_id_6 = random_integer(1, num_other_records)
                equip_id_1 = random_integer(1, num_other_records)
                equip_id_2 = random_integer(1, num_other_records)
                equip_id_3 = random_integer(1, num_other_records)
                execute_sql(f"""INSERT INTO {TABLE_NAME} 
                (Tank_ID, Client_ID, Experience,Status, Shell_ID, Equiped_amount, Gun_ID, Turret_ID, Crew_ID_1, Crew_ID_2, Crew_ID_3, Crew_ID_4, Crew_ID_5, Crew_ID_6, Equip_ID_1, Equip_ID_2, Equip_ID_3) 
                VALUES 
                ({tank_id}, {client_id}, {experience}, {status},{shell_id}, {equiped_amount}, {gun_id}, {turret_id}, {crew_id_1}, {crew_id_2}, {crew_id_3}, {crew_id_4}, {crew_id_5}, {crew_id_6}, {equip_id_1}, {equip_id_2}, {equip_id_3});""")
    print("Tank_status generated")

    TABLE_NAME = "Equipment_status"
    query1 = (f"""SELECT COUNT(*) FROM {TABLE_NAME};""")
    execute_sql(query1)
    count = cursor.fetchone()[0]
    if count == 0:
        NUM_ROWS = num_other_records
        for i in range(1, NUM_ROWS + 1):
            while True:
                equip_id = random_integer(1, num_other_records)
                client_id = random_integer(1, num_main_records)
                cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE Equip_ID = {equip_id} AND Client_ID = {client_id}")
                if cursor.fetchone() is None:
                    break
            equip = random_integer(1, 50)
            general = random_integer(51, 100)
            execute_sql(f"INSERT INTO {TABLE_NAME} (Equip_ID, Client_ID, Equiped_amount, General_amount) VALUES ({equip_id}, {client_id}, '{equip}', {general});")
    print("Equipment_status generated")

    TABLE_NAME = "Client_Replay"
    query1 = (f"""SELECT COUNT(*) FROM {TABLE_NAME};""")
    execute_sql(query1)
    count = cursor.fetchone()[0]
    if count == 0:
        NUM_ROWS = num_other_records
        for i in range(1, NUM_ROWS + 1):
            while True:
                replay_id = random_integer(1, num_other_records)
                client_id = random_integer(1, num_main_records)
                cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE Replay_id = {replay_id} AND Client_id = {client_id}")
                if cursor.fetchone() is None:
                    break
            execute_sql(f"INSERT INTO {TABLE_NAME} (Replay_id, Client_id) VALUES ({replay_id}, {client_id});")
    print("Client_Replay generated")


    TABLE_NAME = "Gun_Shell"
    query1 = (f"""SELECT COUNT(*) FROM {TABLE_NAME};""")
    execute_sql(query1)
    count = cursor.fetchone()[0]
    if count == 0:
        NUM_ROWS = num_other_records
        for i in range(1, NUM_ROWS + 1):
            while True:
                gun_id = random_integer(1, num_other_records)
                shell_id = random_integer(1, num_other_records)
                cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE Gun_ID = {gun_id} AND Shell_ID = {shell_id}")
                if cursor.fetchone() is None:
                    break
            execute_sql(f"INSERT INTO {TABLE_NAME} (Gun_ID, Shell_ID) VALUES ({gun_id}, {shell_id});")
    print("Gun_Shell generated")


    TABLE_NAME = "Moderator_Log"
    query1 = (f"""SELECT COUNT(*) FROM {TABLE_NAME};""")
    execute_sql(query1)
    count = cursor.fetchone()[0]
    if count == 0:
        NUM_ROWS = num_other_records
        for i in range(1, NUM_ROWS + 1):
            while True:
                moderator_id = random_integer(1, num_other_records)
                login_id = random_integer(1, num_other_records)
                cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE Moderator_ID = {moderator_id} AND Login_ID = {login_id}")
                if cursor.fetchone() is None:
                    break
            execute_sql(f"INSERT INTO {TABLE_NAME} (Moderator_ID, Login_ID) VALUES ({moderator_id}, {login_id});")
    print("Moderator_Log generated")

    TABLE_NAME = "Moderator_Replay"
    query1 = (f"""SELECT COUNT(*) FROM {TABLE_NAME};""")
    execute_sql(query1)
    count = cursor.fetchone()[0]
    if count == 0:
        NUM_ROWS = num_other_records
        for i in range(1, NUM_ROWS + 1):
            while True:
                moderator_id = random_integer(1, num_other_records)
                replay_id = random_integer(1, num_other_records)
                cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE Moderator_ID = {moderator_id} AND Replay_ID = {replay_id}")
                if cursor.fetchone() is None:
                    break
            execute_sql(f"INSERT INTO {TABLE_NAME} (Moderator_ID, Replay_ID) VALUES ({moderator_id}, {replay_id});")
    print("Moderator_Replay generated")

    TABLE_NAME = "Skill_Role"
    query1 = (f"""SELECT COUNT(*) FROM {TABLE_NAME};""")
    execute_sql(query1)
    count = cursor.fetchone()[0]
    if count == 0:
        NUM_ROWS = num_other_records
        for i in range(1, NUM_ROWS + 1):
            while True:
                role_id = random_integer(1, num_other_records)
                skill_id = random_integer(1, num_other_records)
                cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE Role_ID = {role_id} AND Skill_ID = {skill_id}")
                if cursor.fetchone() is None:
                    break
            execute_sql(f"INSERT INTO {TABLE_NAME} (Role_ID, Skill_ID) VALUES ({role_id}, {skill_id});")
    print("Skill_Role generated")
    print("Everything generated!")
except (Exception, psycopg2.DatabaseError) as error:
    print(f"Error: {error}")

finally:
    if connection:
        cursor.close()
        connection.close()