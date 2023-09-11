import mysql.connector

userinput = input("Anna maakoodi: ")

dbconn = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='test1',
    autocommit=True
)


def my_function(country):
    sql = "SELECT type, count(*) AS amount FROM airport WHERE iso_country = '" + userinput + "' GROUP BY type"

    kursori = dbconn.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print("Lentokenttä tyyppiä " + rivi[0] + " on " + str(rivi[1]))
        return


my_function(userinput)
