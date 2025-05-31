import pytest
from names import extract_family_name, extract_given_name, make_full_name

family_name = "Brown"
given_name = "Sally"
full_name = f"{family_name}; {given_name}" 

def test_make_full_name():
  assert make_full_name(given_name=given_name, family_name=family_name) == full_name

def test_extract_family_name():
  assert extract_family_name(full_name) == family_name

def test_extract_given_name():
  assert extract_given_name(full_name) == given_name


pytest.main(["-v", "--tb=line", "-rN", __file__])