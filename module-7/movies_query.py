import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",	
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
    }

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)



cursor = db.cursor()
cursor.execute("SELECT studio_id, studio_name FROM studio")
studios = cursor.fetchall()
for studio in studios:
    print("Studio ID: {}\n Studio Name:{}\n".format(studio[0], studio[1], studio[2]))
    
cursor = db.cursor()
cursor.execute("SELECT genre_id, genre_name FROM genre")
genres = cursor.fetchall()
for genre in genres:
    print("Genre ID: {}\n Genre Name:{}\n".format(genre[0], genre[1], genre[2]))


