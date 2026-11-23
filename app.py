
import streamlit as st
import requests

API_KEY = st.secrets["API_KEY"]
url = "https://api.openweathermap.org/data/2.5/weather"

st.title("Weather App")
st.write("Welcome to my Weather App!")
st.divider()

city = st.text_input("Enter city name")

if st.button("Get Weather"):
    if city.strip() == "":
        st.warning("Please enter a city name.")
    else:

        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(url, params=params)
        

        if response.status_code == 200:
            data = response.json()
            st.divider()

            st.subheader(data["name"])
            col1, col2,col3,col4 = st.columns(4)
            col1.metric("Temperature", f'{data["main"]["temp"]} °C')
            col2.metric("Humidity", f'{data["main"]["humidity"]} %')
            col3.metric("Feels Like", f'{data["main"]["feels_like"]} °C')
            col4.metric("Wind Speed", f'{data["wind"]["speed"] * 3.6:.1f} km/h')
            st.subheader("Weather Condition")

            weather = data["weather"][0]["main"]

            weather_icons = {
                "Clear": "☀️",
                "Clouds": "☁️",
                "Rain": "🌧️",
                "Drizzle": "🌦️",
                "Thunderstorm": "⛈️",
                "Snow": "❄️",
                "Mist": "🌫️",
                "Fog": "🌫️",
                "Haze": "🌫️"
            }

            icon = weather_icons.get(weather, "🌤️")

            st.write(icon, data["weather"][0]["description"].title())
            
        else:
            st.error("City not found. Please enter a valid city name.")
