import requests

def home():
    print("🏠 Welcome to the Weather App!")
    city=input("Enter the City you want to know about the Weather: ")
    getweather(city)
    findother()
    
def getweather(cityname):
    print("This is Weather information of " + cityname)

    try: 
        location_url = f"https://geocoding-api.open-meteo.com/v1/search?name={cityname}&count=1&language=en&format=json"
        location_response = requests.get(location_url)
        location_data = location_response.json()
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}\n")
        home()

    results = location_data.get("results", [])

    if len(results) == 0:
        print("Couldn't find the city " + cityname)
        home()
    else: 
        first_result = results[0]
        print(f"ID: {first_result.get('id','N/A')}")
        print(f"City: {first_result.get('name','N/A')}")
        print(f"Country Code: {first_result.get('country_code','N/A')}")
        print(f"Longitude: {first_result.get('longitude','N/A')}")
        print(f"Latitude: {first_result.get('latitude','N/A')}")
        print(f"Time Zone: {first_result.get('timezone','N/A')}")

        # Only proceed if city matches
        api_weather = f"https://api.open-meteo.com/v1/forecast?latitude={first_result['latitude']}&longitude={first_result['longitude']}&hourly=temperature_2m&models=gem_seamless"
        weather_response = requests.get(api_weather)
        weather_data = weather_response.json()

        # Extract hourly temperatures
        hourly = weather_data.get("hourly", {})
        times = hourly.get("time", [])
        temperatures = hourly.get("temperature_2m", [])

        print("\n🌡️ Hourly Temperature Forecast:")
        # Show first 6 hours as example
        for t, temp in zip(times[:6], temperatures[:6]):
            #ZIP IS USED TO PAIR THE TWO LISTS TOGETHER INDEX BY INDEX
            print(f"{t} -> {temp}°C")


        
        
        
def findother():
    again=input("Do you want to check weather of another city? (y/n): ").lower()
    if again=='y':
        home()
    else:
        print("Thank you for using the Weather App! Goodbye! 👋")
        exit()     
        
home()