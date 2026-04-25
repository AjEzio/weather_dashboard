import requests
import os 
import sqlite3
def save_city(city,lat_long):
    with sqlite3.connect("app.db") as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS favcity (city TEXT NOT NULL, lat REAL, lon REAL )")
        cursor.execute("SELECT * FROM favcity")
        rows = cursor.fetchall()
        for row in rows:
            if row["city"] == city:
                return
        cursor.execute("INSERT INTO favcity VALUES(?, ?, ?)",(city, lat_long[0], lat_long[1]))
        db.commit()

def look_city():
    with sqlite3.connect("app.db") as db:
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS favcity (city TEXT NOT NULL, lat REAL, lon REAL )")
        cursor.execute("SELECT * FROM favcity")
        rows = cursor.fetchall()
        for i, row in enumerate(rows, start=1):
            print(f"{i}. {row[0]}")
        choice = int(input("Choose the number from above or Press 0 for new city: "))
        if choice == 0:
            return 0
        given_city = rows[choice-1]
        weather_det([given_city[1],given_city[2]])
        return 1

def city_cord(city):
    response = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}")
    if response.status_code == 200:
        data = response.json()
        for item in data["results"]:
            if item["name"] == city:
                save_city(city,[item["latitude"], item["longitude"]])
                return [item["latitude"], item["longitude"]]
    else:
        print("Error: ", response.status_code)

def weather_det(coord):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={coord[0]}&longitude={coord[1]}&current_weather=true&daily=temperature_2m_max,temperature_2m_min")
    if response.status_code == 200:
        data = response.json() 
        print(f"Current Temperature is: {data["current_weather"]["temperature"]} {data["current_weather_units"]["temperature"]}")
        print(f"Current Wind speed is: {data["current_weather"]["windspeed"]} {data["current_weather_units"]["windspeed"]}")
        print("Max and Min temperature for the next seven days:")
        for i in range(len(data["daily"]["temperature_2m_max"])):
            print(f"{data["daily"]["time"][i]}",end = " ")
            print(f"Max:{data["daily"]["temperature_2m_max"][i]}",end = " ")
            print(f"Min:{data["daily"]["temperature_2m_min"][i]}",end = " ")
            print("")
    else:
        print("Error: ", response.status_code)

def main():
    print("Welcome to Weather Dashboard\n")
    if not look_city():
        city = input("Enter the city name for weather details or use from saved cities: ")
        lat_long = city_cord(city)
        weather_det(lat_long)

if __name__ == "__main__":
    main()

