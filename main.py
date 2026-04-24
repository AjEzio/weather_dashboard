import requests

def city_cord(city):
    response = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}")
    if response.status_code == 200:
        data = response.json()
        for item in data["results"]:
            if item["name"] == city:
                return [item["latitude"], item["longitude"]]
    else:
        print("Error: ", response.status_code)

def weather_det(coord):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={coord[0]}&longitude={coord[1]}&current_weather=true")
    if response.status_code == 200:
        data = response.json() 
        print(f"Current Temperature is: {data["current_weather"]["temperature"]} {data["current_weather_units"]["temperature"]}")
        print(f"Current Wind speed is: {data["current_weather"]["windspeed"]} {data["current_weather_units"]["windspeed"]}")
    else:
        print("Error: ", response.status_code)
def main():
    print("Welcome to Weather Dashboard\n")
    city = input("Enter The city name for weather details: ")
    lat_long = city_cord(city)
    weather_det(lat_long)

if __name__ == "__main__":
    main()

