
import requests
API_KEY = "a1ab34073871a6518be290636f62e2f2"

url = "https://api.openweathermap.org/data/2.5/weather"
city = input("Enter city name: ")
params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()

    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Weather:", data["weather"][0]["description"])

else:
    print("City not found. Please enter a valid city name.")

# print(response.json())
# data = response.json()

# print("City:", data["name"])
# print("Temperature:", data["main"]["temp"], "°C")
# print("Humidity:", data["main"]["humidity"], "%")
# print("Weather:", data["weather"][0]["description"])