from convert_tools import *

def current_condition_base():
    #return base url for weather API
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    return base_url

def current_condition_url(base_url, api_key, name_of_city):
    #uses base url, adds api key and name of reuqested city to build proper URL
    return f"{base_url}appid={api_key}&q={name_of_city}"

def parse_json_data(from_json):
    try:
        temperature_as_k = from_json['main']['temp']
        pressure_in_hpa = from_json['main']['pressure']
        humidity_in_percent = from_json['main']['humidity']
        weather_description = from_json['weather'][0]['description']
        wind = from_json['wind']['speed']
        result_list = [temperature_as_k, pressure_in_hpa, humidity_in_percent, weather_description, wind]
        
    except (ValueError, KeyError) as e:
        return None
    return result_list

def print_weather_info(weather, imperial=True):
    if imperial == True:
        temp = from_kelvin_farenheit(weather[0])
        pressure = from_hpa_psi(weather[1])
        wind = from_ms_mph(weather[4])
        print(f"Temperature: {temp:.2f} F")
        print(f"Humidity: {weather[2]}%")
        print(f"Pressure: {pressure:.2f} PSI")
        print(f"Weather Description: {weather[3]}")
        print(f"Wind: {wind:.2f} MPH")
    else:
        temp = from_kelvin_celcius(weather[0])
        wind = from_ms_kph(weather[4])
        print(f"Temperature: {temp} C")
        print(f"Pressure: {weather[1]} HPA")
        print(f"Humidity: {weather[2]}%")
        print(f"Weather Description: {weather[3]}")
        print(f"Wind: {wind:.2f} KM/H")