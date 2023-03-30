def hourly_condition_base():
    # return base URL for weather API
    return 'https://api.openweathermap.org/data/2.5/forecast?'

def hourly_condition_url(base_url, api_key, name_of_city):
    return f"{base_url}appid={api_key}&q={name_of_city}"
    # lat={lat}&lon={lon}&appid={API key}