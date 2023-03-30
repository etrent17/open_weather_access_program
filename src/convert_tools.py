def from_kelvin_farenheit(kelvin):
    return round(kelvin * 1.8 - 459.67, 2)

def from_kelvin_celcius(kelvin):
    return round(kelvin - 273.15, 2)

def from_hpa_psi(hpa):
    return round(hpa * 0.0145037738 , 2)

def from_ms_mph(m_s):
    return round(m_s * 2.2369362920544025, 2)

def from_ms_kph(m_s):
    return round(m_s * 3.6, 2)