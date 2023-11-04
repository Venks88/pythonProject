import pytest
import requests


test_tuples = [("us", "90210", "Beverly Hills"),
    ("ca", "B2A", "North Sydney South Central"),
    ("it", "50123", "Firenze")]


def test_get_locations_for_us_90210_check_status_code_equals_200():
    response = requests.get("http://api.zippopotam.us/us/90210")
    assert response.status_code == 200
    response1 = response.json();
    assert response1["places"][0]["place name"] == "Beverly Hills"


@pytest.mark.parametrize("country_code, zipcode, expected_place_name", test_tuples)
def test_usingTuples(country_code, zipcode, expected_place_name):
    response = requests.get(f"http://api.zippopotam.us/{country_code}/{zipcode}")
    out = response.json()
    assert out["places"][0]["place name"] == "Torino"
