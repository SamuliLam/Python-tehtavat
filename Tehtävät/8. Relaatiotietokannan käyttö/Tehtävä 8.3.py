from geopy.distance import geodesic as GD
import mysql.connector

dbconn = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='test1',
    autocommit=True
)

icao1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ")

icao2 = input("Anna toisen lentokentän ICAO-koodi: ")
def calculate_distance(country_code, country_code2):
    cursor = dbconn.cursor()
    cursor.execute(f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident = '{icao1}'")
    result1 = cursor.fetchone()
    cursor.close()

    cursor = dbconn.cursor()
    cursor.execute(f"SELECT longitude_deg, latitude_deg FROM airport WHERE ident = '{icao2}'")
    result2 = cursor.fetchone()
    cursor.close()

    if result1 and result2:

        airport1_coords = (result1[1], result1[0])
        airport2_coords = (result2[1], result2[0])

        distance = GD(airport1_coords, airport2_coords).kilometers

        return distance
    else:
        return None


distance = calculate_distance(icao1, icao2)

if distance is not None:
    print(f"Etäisyys lentokenttien {icao1} ja {icao2} välillä on {distance} kilometriä.")
else:
    print("Lentokenttien tietoja ei löytynyt.")


