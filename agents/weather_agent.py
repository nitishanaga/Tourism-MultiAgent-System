import requests

class WeatherAgent:
    def handle(self, location):
        try:
            # Step 1: Geocoding (latitude and longitude lookup)
            geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={location}&count=1&language=en&format=json"
            geo_response = requests.get(geo_url).json()

            if not geo_response.get("results"):
                return f"Sorry, I couldn't find weather data for {location}. I don't know this place exists."

            lat = geo_response["results"][0]["latitude"]
            lon = geo_response["results"][0]["longitude"]

            # Step 2: Fetch Weather Forecast
            weather_url = (
                f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
                f"&daily=precipitation_probability_max&timezone=auto"
            )
            weather_response = requests.get(weather_url).json()

            current_temp = weather_response["current_weather"]["temperature"]
            chance_of_rain = weather_response["daily"]["precipitation_probability_max"][0]

            # Output format: Plain text for degree symbol
            return (
                f"In {location.title()} it's currently {current_temp}°C with a chance of {chance_of_rain}% to rain."
            )

        except Exception as e:
            return f"⚠ Error fetching weather for {location.title()}: {e}"