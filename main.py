import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
file = open("iss.txt", "w")
file.write("There are currently" + " " + str(result["number"]) + " astronauts on the ISS: \n\n")
people = result["people"]
for p in people:
    file.write(p['name'] + " - on board" + "\n")
g = geocoder.ip('me')
file.write("\n Your current Latitude / Longitude is: " + str(g.latlng))
file.close()
webbrowser.open("iss.txt")

screen = turtle.Screen()
screen.setup(1380, 700, 0, 0)
screen.setworldcoordinates(-180, -90, 180, 90)

screen.bgpic("World Map.gif")
screen.register_shape("ISS.gif")
iss = turtle.Turtle()
iss.shape("ISS.gif")
iss.setheading(45)
iss.penup()

while True:
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    location = result["iss_position"]
    lat = location['latitude']
    lon = location['longitude']

    lat = float(lat)
    lon = float(lon)
    print("\nLatitude: " + str(lat))
    print("\nLongitude: " + str(lon))

    iss.goto(lon, lat)

    time.sleep(5)
