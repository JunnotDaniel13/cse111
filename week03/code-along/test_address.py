import pytest
from address import extract_city, extract_state, extract_zipcode

number_street = "16 Washington Mews"
city = "New York"
state = "NY"
zipcode = "10003"
full_address = f"{number_street}, {city}, {state} {zipcode}"

def test_extract_city():
  assert extract_city(full_address) == city

def test_extract_state():
  assert extract_state(full_address) == state

def test_extract_zipcode():
  assert extract_zipcode(full_address) == zipcode

pytest.main(["-v", "--tb=line", "-rN", __file__])
