import requests
import json

userinput = input("Anna paikkakunnan nimi: ")


request = f'https://api.openweathermap.org/data/2.5/weather?q={userinput}&appid=fac105958c9a086efd423bc985ee2892&units=metric'
response = requests.get(request).json()

print(f"Sää paikkakunnalla {response['name']}, {response['weather'][0]['main']}, {response['weather'][0]['description']}")
print(f"Lämpötila {response['main']['temp']} astetta")
