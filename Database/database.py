import mysql.connector
from mysql.connector.errors import ProgrammingError
import asyncio

host = "localhost" # name of database server
database = "smart" # database name
user = "root" # username
password = ""


async def connect():
    connection = mysql.connector.connect(
        host = host,    
        database = database,
        user = user,
        password = password
    )
    return connection


def Initial_main_table() -> None:

    # Create the main table by name users
    try:
        connection = mysql.connector.connect(
            host = host,   
            database = database, 
            user = user, 
            password = password
        )
        cursor = connection.cursor()
        create_main_table = f"""
            CREATE TABLE `{database}`.`users` (`id` INT(12) NOT NULL DEFAULT '0' , `username` VARCHAR(255) NOT NULL , `channels` VARCHAR(255) NOT NULL ) ENGINE = InnoDB;"""
        cursor.execute(create_main_table)
        connection.commit()
        cursor.close()
        connection.close()
    except ProgrammingError:
        return
    

async def check_new_user(user_id: int) -> bool:
    
    # check bot new user
    connection = await connect()
    cursor = connection.cursor()
    target_id = user_id
    query = "SELECT EXISTS(SELECT 1 FROM users WHERE id = %s)"
    cursor.execute(query, (target_id,))
    exists = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    if exists:
        return True
    else:
        return False
