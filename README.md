# CSE 111 Milestone
Elijah Trent
This program requests weather data for a user-specified city in Python 3 using the OpenWeatherMap API.

## Prerequisites
Before running this program, make sure to set the environment variable for your API key from OpenWeatherMap.org. If you are with BYU-Idaho, please contact the author for API access.

## Usage
To use this program, run the main function in your Python 3 environment. The program will prompt the user to enter the desired city, units (imperial or metric), and whether to retrieve current conditions or hourly forecast.

If the user selects the hourly forecast, they will be prompted to choose between a 12-hour and 3-day forecast. The program will then display the requested weather information for the desired city.

## Dependencies
This program requires the following dependencies:

os
requests
json
numpy
config
current_conditions
hourly_forecast
json_tools
datetime
Testing
The program includes a TODO to check for response code 200 and write tests.

### License
This program is licensed under the MIT License.
