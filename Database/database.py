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


def initial_main_table() -> None:

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
            CREATE TABLE `{database}`.`users` (`id` DECIMAL(13) NOT NULL DEFAULT '0' , `username` VARCHAR(255) NOT NULL , `channels` VARCHAR(255) NOT NULL ) ENGINE = InnoDB;"""
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
    query_exist = "SELECT EXISTS(SELECT 1 FROM users WHERE id = %s)"
    cursor.execute(query_exist, (target_id,))
    exists = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    if exists:
        return True
    else:
        return False
    

async def add_new_user(user_id: int) -> None:

    # add bot new user to database
    connection = await connect()
    cursor = connection.cursor()
    new_id = user_id
    query_insert = "INSERT INTO users (id, `username`, `channels`) VALUES (%s, '', '')"
    cursor.execute(query_insert, (new_id,))
    connection.commit()
    cursor.close()
    connection.close()


async def initial_user_table(user_id: int) -> None:
    # Create the user table by name user_id
    connection = await connect()
    cursor = connection.cursor()
    query_create_table_user = f"""CREATE TABLE `smart`.`{user_id}` 
    (`channels` VARCHAR(255) NOT NULL , `files` MEDIUMTEXT NOT NULL , `time` FLOAT NULL DEFAULT NULL , `repeated sending` VARCHAR(255) NOT NULL DEFAULT 'off' , `random sending` VARCHAR(255) NOT NULL DEFAULT 'off' ) ENGINE = InnoDB;"""
    cursor.execute(query_create_table_user)
    connection.commit()
    cursor.close()
    connection.close()


async def add_channel(user_id: int, channel_id: str) -> None:
    connection = await connect()
    cursor = connection.cursor()
    query_insert_channel = f"""INSERT INTO `{user_id}` (`channels`, `files`, `time`, `repeated sending`, `random sending`) VALUES ('{channel_id}', '', NULL, 'off', 'off');"""
    cursor.execute(query_insert_channel)
    connection.commit()
    cursor.close()
    connection.close()


async def remove_channel(user_id: int, channel_id: str) -> None:
    connection = await connect()
    cursor = connection.cursor()
    query_remove_channel = f"""DELETE FROM `{user_id}` WHERE channels = '{channel_id}'"""
    cursor.execute(query_remove_channel)
    connection.commit()
    cursor.close()
    connection.close()


async def check_new_channel(user_id: int, channel_id: str) -> bool:
    # check bot new user
    connection = await connect()
    cursor = connection.cursor()
    query_exist = f"SELECT EXISTS(SELECT 1 FROM `{user_id}` WHERE channels = {channel_id})"
    cursor.execute(query_exist)
    exists = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    if exists:
        return True
    else:
        return False


async def get_channels(user_id: int) -> list:
    # get channels from database
    connection = await connect()
    cursor = connection.cursor()
    get_channel_query = f"""SELECT `channels` FROM `{user_id}` WHERE 1"""
    cursor.execute(get_channel_query)
    result = cursor.fetchall() 
    list_channels = []
    for channel in result:
        list_channels.append(channel[0])
    cursor.close()
    connection.close()
    return list_channels

async def get_time(user_id: int, channel_id: str) -> float | None:
    # get repeated sending time from database
    connection = await connect()
    cursor = connection.cursor()
    get_time_query = f"""SELECT `time` FROM `{user_id}` WHERE channels = {channel_id}"""
    cursor.execute(get_time_query)
    result = cursor.fetchall()
    return result[0][0]
