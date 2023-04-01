"""
CSE 111 Milestone
Elijah Trent
Weather Request in Python
Please set environment variable before running in Python 3

Requires API Key from OpenWeatherMap.org
If you are with BYU-Idaho, please contact the author for API access.

User inputs city and python returns meteorological info about requested city

(C) Copyright Elijah Trent 2023
Apache License
"""
import os
import requests
import json
import numpy
from datetime import datetime

def main():
    API_KEY = get_api_key()
    if API_KEY:
        print('Exists')
       
    else:
        print("API Key failed, please check your environment variables. Goodbye.")
        exit()
    
    question_report = 'Do you need the current conditions or hourly forecast? [forecast/current] '
    question_city = 'Please input your desired city: [please no commas/spaces] '
    question_units = 'Do you use imperial units? [y/n] '
    is_imperial = False

    
    print()
    desired_city = input(question_city)
    while True:
        desired_units = input(question_units)
        if desired_units.lower().strip() == 'y':
            is_imperial = True
            break
        elif desired_units.lower().strip() == 'n':
            is_imperial = False
            break
        else:
            print("I Didn't recognize that, please try again.")    
            continue
    while True:
        desired_report = input(question_report)
        if desired_report.lower().strip() == 'forecast':
            print()
            break
        elif desired_report.lower().strip() == 'current':
            print()
            break
        else:
            print("I didn't catch that, please try again.")
            continue
    if desired_report.strip().lower() == 'forecast':
        print()
        main_url = hourly_condition_base()
        request_url = hourly_condition_url(main_url, API_KEY, desired_city)
        result = send_request(request_url)
        weather_information = read_json_data(result)
        if isinstance(weather_information, dict): # check if is a dictionary
            for i in weather_information['list']:
                parse_data = parse_json_data(i)
                print()
                print(i['dt_txt'])
                print_weather_info(parse_data)
        else:
            print("Dictionary not found, please try again.")

    elif desired_report.strip().lower() == 'current': 
        main_url = current_condition_base()
        request_url = current_condition_url(main_url, API_KEY, desired_city)
        result = send_request(request_url)
        weather_information = read_json_data(result)
        
        if isinstance(weather_information, dict): # check if is a dictionary
            parse_data = parse_json_data(weather_information)
            print_weather_info(parse_data, is_imperial)
        else:
            print("Dictionary not found, please try again.")
    else:
        ("An error occurred or the server is inaccessible, please try again.")

def get_api_key():
    try:
        #get api key from environment variables
        KEY = os.getenv('WEATHERKEY')
        if KEY is not None:
            return KEY
        else:
            return False
    except Exception as e:
        print(f"Your error: {e}")

def from_kelvin_fahrenheit(kelvin):
    return round(kelvin * 1.8 - 459.67, 2)

def from_kelvin_celsius(kelvin):
    return round(kelvin - 273.15, 2)

def from_hpa_psi(hpa):
    return round(hpa * 0.0145037738 , 2)

def from_ms_mph(m_s):
    return round(m_s * 2.2369362920544025, 2)

def from_ms_kph(m_s):
    return round(m_s * 3.6, 2)

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
        temp = from_kelvin_fahrenheit(weather[0])
        pressure = from_hpa_psi(weather[1])
        wind = from_ms_mph(weather[4])
        print(f"Temperature: {temp:.2f} F")
        print(f"Humidity: {weather[2]}%")
        print(f"Pressure: {pressure:.2f} PSI")
        print(f"Weather Description: {weather[3]}")
        print(f"Wind: {wind:.2f} MPH")
    else:
        temp = from_kelvin_celsius(weather[0])
        wind = from_ms_kph(weather[4])
        print(f"Temperature: {temp} C")
        print(f"Pressure: {weather[1]} HPA")
        print(f"Humidity: {weather[2]}%")
        print(f"Weather Description: {weather[3]}")
        print(f"Wind: {wind:.2f} KM/H")

def hourly_condition_base():
    # return base URL for weather API
    return 'https://api.openweathermap.org/data/2.5/forecast?'

def hourly_condition_url(base_url, api_key, name_of_city):
    # return request url with API Key and name of city
    return f"{base_url}appid={api_key}&q={name_of_city}"
    
def send_request(requested_url):
    #returns requested data with given url
    return requests.get(requested_url)

def read_json_data(input_data):
    #uses input data and returns it to main program
    return input_data.json()

if __name__ == "__main__":
    main()