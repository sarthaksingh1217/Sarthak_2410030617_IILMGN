import requests

def fetch_weather(city_name, api_key):
    # The API endpoint for current weather, using metric units (Celsius)
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # The parameters we are sending to the API
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric" 
    }
    
    try:
        # Sending the GET request to OpenWeatherMap
        response = requests.get(base_url, params=params)
        data = response.json()
        
        # Check if the request was successful (HTTP Status Code 200)
        if response.status_code == 200:
            # Extracting the data we want from the JSON dictionary
            temp = data['main']['temp']
            description = data['weather'][0]['description']
            
            print(f"✅ Success! The current weather in {city_name} is:")
            print(f"🌡️ Temperature: {temp}°C")
            print(f"☁️ Conditions: {description.capitalize()}")
            return True
        else:
            print(f"❌ Error fetching data: {data.get('message', 'Unknown error')}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Connection Error: {e}")
        return False

# --- Run the Test ---
if __name__ == "__main__":
    # ⚠️ PASTE YOUR ACTUAL API KEY HERE
    MY_API_KEY = "6c4d30e05d269d3632e8e27c4437e661" 
    
    print("Testing SmartTransit API Integration...\n")
    
    # Let's test it with a few cities
    test_cities = ["Mumbai", "Delhi", "London"]
    
    for city in test_cities:
        fetch_weather(city, MY_API_KEY)
        print("-" * 30)