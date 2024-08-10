import mysql.connector
from mysql.connector.errors import ProgrammingError


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


def Initial_main_table():
    try:
        connection = mysql.connector.connect(
            host = host,   
            database = database, 
            user = user, 
            password = password
        )
        cursor = connection.cursor()
        create_main_table = f"""
            CREATE TABLE `{database}`.`usaser` (`id` INT NOT NULL DEFAULT '0' , `username` VARCHAR(255) NOT NULL , `channels` VARCHAR(255) NOT NULL ) ENGINE = InnoDB;"""
        cursor.execute(create_main_table)
        connection.commit()
        cursor.close()
        connection.close()
    except ProgrammingError:
        return