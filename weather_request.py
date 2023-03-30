"""
CSE 111 Milestone
Elijah Trent
Weather Request in Python
Please set environment variable before running in Python 3

Requires API Key from OpenWeatherMap.org

$Env:WEATHERKEY="<api_key>"
User inputs city and python returns meteorological info about requested city


"""
import os
import requests
import json
import numpy
from config import get_api_key
from current_conditions import *
from hourly_forecast import *
from json_tools import *


def main():
    API_KEY = get_api_key()
    if API_KEY:
        print(API_KEY)
       
    else:
        print("API Key failed, please check your environment variables. Goodbye.")
        exit()
    # main_url = current_condition_base()
    
    question_report = 'Do you need the current conditions or a forecast? [forecast/current] '
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
        print(request_url)
        result = send_request(request_url)
        print(result)
        result_as_dict = read_json_data(result)
        for i in result_as_dict.items():
                print(i)
        json_check = not_json(result)
        if not_json:
            # print("Sanitizing JSON data")
            print()
            sanitized_data = sanitize_json_data(result_as_dict) 

            for i in sanitized_data.items():
                print(i)            
            # weather_info = parse_json_data(sanitized_data)
            # for i in weather_info:
                    # print(i)
                # if weather_info != None:
                #     print(f"The weather for {desired_city.capitalize()} right now:")
                #     print_weather_info(weather_info, is_imperial)
                # else:
                #     print("The service could not find your city, please try again.")
        # elif desired_forecast.lower().strip() == 'day':
        #     # main_url = day_condition_base()
        #     # request_url = day_condition_url
        #     ...
        # else:
        #     print('Input not recognized, please try again.')


        
    elif desired_report.strip().lower() == 'current': 
        # request for current_conditions
        main_url = current_condition_base()
        request_url = current_condition_url(main_url, API_KEY, desired_city)



    

    result = send_request(request_url)
    # print(result)
    result_as_dict = read_json_data(result)
    # print(result_as_json)
    json_check = not_json(result_as_dict)
    # print(type(result))
    # yes_val = check_for_json(result)
    # print(yes_val)

    # make sure the data is not in JSON format so Python can understand and print accordingly
    if not_json:
        # print("Sanitizing JSON data")
        print()
        sanitized_data = sanitize_json_data(result_as_dict) 
        # for i in sanitized_data.items():
        #     print(i)            
        weather_info = parse_json_data(sanitized_data)
        if weather_info != None:
            print(f"The weather for {desired_city.capitalize()} right now:")
            print_weather_info(weather_info, is_imperial)
        else:
            print("The service could not find your city, please try again.")
            
    else:
        print("Failed to convert JSON to a Python-readable dictionary.")
        print("Please check your input and try again.")



if __name__ == "__main__":
    main()