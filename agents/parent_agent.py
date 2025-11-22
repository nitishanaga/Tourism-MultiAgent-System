from .weather_agent import WeatherAgent
from .places_agent import PlacesAgent
import re

class ParentAgent:
    def __init__(self):
        # Child Agent 1: Weather Agent
        self.weather_agent = WeatherAgent()
        # Child Agent 2: Places Agent
        self.places_agent = PlacesAgent()

    def process(self, message):
        message = message.lower()
        response_parts = []
        location = self.extract_location(message)
        
        # Error Handling: If no location is found
        if not location:
            # Handles non-existent places and general lack of location
            return "Please specify a location (e.g., 'What is the weather in Paris?'). I don't know this place exists."

        # --- Intent Detection ---
        is_weather_query = "weather" in message or "temperature" in message
        is_places_query = "place" in message or "visit" in message or "tourist" in message or "plan my trip" in message

        # Scenario: User gave a location but no specific question (e.g., "I'm going to Paris")
        # We default to assuming the user wants both weather and places (combined query).
        if not is_weather_query and not is_places_query:
            is_weather_query = True
            is_places_query = True

        # --- Process Weather (Child Agent 1) ---
        if is_weather_query:
            weather_response = self.weather_agent.handle(location)
            response_parts.append(weather_response)

        # --- Process Places (Child Agent 2) ---
        if is_places_query:
            places_response = self.places_agent.handle(location)
            
            # If weather was also asked for (Example 3), format is "And these are..."
            if is_weather_query and not places_response.startswith("⚠ Error"):
                response_parts.append(f"And these are the places you can go:\n{places_response}")
            
            # If ONLY places was asked for (Example 1), format is "In [City] these are..."
            elif not is_weather_query and not places_response.startswith("⚠ Error"):
                response_parts.append(f"In {location.title()} these are the places you can go,\n{places_response}")
            
            # Handle error messages regardless of intent
            elif places_response.startswith("⚠ Error"):
                 response_parts.append(places_response)


        # --- Finalize Response ---
        # Join parts with a single space. Newlines within the response parts handle formatting.
        return " ".join(response_parts)

    def extract_location(self, text):
        # 1. Look for location after common travel prepositions (e.g., "going to go to Bangalore")
        match_travel_phrase = re.search(r'(going to go to|plan my trip to|in)\s+(\w+)', text)
        if match_travel_phrase:
            return match_travel_phrase.group(2)
        
        # 2. Look for location immediately preceding a comma or question mark before a query (e.g., "Bangalore, what is...")
        match_question = re.search(r'(\w+)[?,]\s*(what is the temperature|what are the places)', text)
        if match_question:
            return match_question.group(1)

        # 3. Fallback: Find the last viable word that is all alpha and reasonably long
        words = text.split()
        for word in words[::-1]:
            if word.isalpha() and len(word) > 3:
                return word
        return None
    
    

