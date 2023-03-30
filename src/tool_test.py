from convert_tools import *
import pytest

num=0

temp_list = [250,270,300,330]

def test_from_k_farenheit():
    assert from_kelvin_farenheit(temp_list[0]) == -9.67
    assert from_kelvin_farenheit(temp_list[1]) == 26.33
    assert from_kelvin_farenheit(temp_list[2]) == 80.33
    assert from_kelvin_farenheit(temp_list[3]) == 134.33
    
def test_from_kelvin_celcius():
    assert from_kelvin_celcius(temp_list[0]) == -23.15
    assert from_kelvin_celcius(temp_list[1]) == -3.15
    assert from_kelvin_celcius(temp_list[2]) == 26.85
    assert from_kelvin_celcius(temp_list[3]) == 56.85
    
hpa_list = [1000,1500,2000,2500]

def test_from_hpa_psi():
    assert from_hpa_psi(hpa_list[0]) == 14.50
    assert from_hpa_psi(hpa_list[1]) == 21.76
    assert from_hpa_psi(hpa_list[2]) == 29.01
    assert from_hpa_psi(hpa_list[3]) == 36.26

def test_from_ms_mph():
    assert from_ms_mph(12) == 26.84
    assert from_ms_mph(25) == 55.92
    assert from_ms_mph(36) == 80.53
    assert from_ms_mph(50) == 111.85

def test_from_ms_kph():
    assert from_ms_kph(5) == 18
    assert from_ms_kph(8) == 28.8
    assert from_ms_kph(13) == 46.8
    assert from_ms_kph(16) == 57.6