import os
import requests

def main():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is not set")

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=Paris&aqi=no"

    response = requests.get(url)
    data = response.json()

    print("Weather in Paris:")
    print(f"Temperature: {data['current']['temp_c']}°C")
    print(f"Condition: {data['current']['condition']['text']}")
    print(f"Wind: {data['current']['wind_kph']} kph")


if __name__ == "__main__":
    main()
