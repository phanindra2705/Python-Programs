import requests


def get_weather(city_name):
    # Replace 'your_api_key' with your actual OpenWeatherMap API key
    api_key = "your_api_key"
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Build the request URL
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    # Send the GET request to the OpenWeatherMap API
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        print(f"Weather in {city_name}: {weather.capitalize()}")
        print(f"Temperature: {temp}°C (Feels like {feels_like}°C)")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print(f"City not found or API error! Status Code: {response.status_code}")


# Prompt the user for a city name
city = input("Enter the name of the city: ")
get_weather(city)
