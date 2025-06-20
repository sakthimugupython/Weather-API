import requests

def get_weather(city):
    API_KEY = '68aaf59551b3ba7fd02ae1655ab04c3c'
    BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

    params = {
        'q': city,
        'appid': API_KEY,
    }

    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print(f"\nWeather in {data['name']}, {data['sys']['country']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Condition: {data['weather'][0]['description'].title()}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s\n")
    else:
        print("City not found or API error!")


city = input("Enter city name: ")
get_weather(city)