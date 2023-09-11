import mysql.connector
userinput = input("Anna lentokentä ICAO-koodi: ")


dbconn = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='root',
         password='test1',
         autocommit=True
         )

def searchAirportInfo(icao):
    sql = "SELECT municipality, name FROM airport"

    sql += " WHERE ident='" + icao + "'"
    kursori = dbconn.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print("Lentokentän sijaintikunta on "+rivi[0] + " ja sen nimi on " + rivi[1])
    return


searchAirportInfo(userinput)