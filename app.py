"""
CSE 111 Milestone
Elijah Trent
Weather Request in Python
Please set environment variable before running in Python 3

Requires API Key from OpenWeatherMap.org
If you are with BYU-Idaho, please contact the author for API access.

User inputs city and python returns meteorological info about requested city

(C) Copyright Elijah Trent 2023
"""
import os
import requests
import json
import numpy
from src.config import get_api_key
from src.current_conditions import *
from src.hourly_forecast import *
from src.json_tools import *
from datetime import datetime

#TODO check for response code 200 and write tests

def main():
    API_KEY = get_api_key()
    if API_KEY:
        print('Exists')
       
    else:
        print("API Key failed, please check your environment variables. Goodbye.")
        exit()
    # main_url = current_condition_base()
    
    question_report = 'Do you need the current conditions or hourly forecast? [forecast/current] '
    # question_forecast = 'Do you need hourly (12 hours) or 3-day [hour/day] '
    question_city = 'Please input your desired city: [please no commas/spaces] '
    question_units = 'Do you use imperial units? [y/n] '
    is_imperial = False
    is_hourly = False
    is_forecast = False
    
    print()
    desired_city = input(question_city)
    desired_units = input(question_units)
    if desired_units.lower().strip() == 'y':
        is_imperial = True
    else:
        is_imperial = False
    desired_report = input(question_report)
    
    if desired_report.strip().lower() == 'forecast':
        # desired_forecast = input(question_forecast)
        print()
        # if desired_forecast.lower().strip() == 'hour':
        main_url = hourly_condition_base()
        request_url = hourly_condition_url(main_url, API_KEY, desired_city)
        # print(request_url)
        result = send_request(request_url)
        # print(result)
        weather_information = read_json_data(result)
        # print(read_json['list'])
        if isinstance(weather_information, dict): # check if is a dictionary
            for i in weather_information['list']:
                parse_data = parse_json_data(i)
                print()
                print(i['dt_txt'])
                print_weather_info(parse_data)
        else:
            print("Dictionary not found, please try again.")

    elif desired_report.strip().lower() == 'current': 
        # request for current_conditions
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
if __name__ == "__main__":
    main()