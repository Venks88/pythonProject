import requests

query_company_ceo_coo_name = """
{
    company {
        ceo
    }
}
"""

def test_graphQL():
    response =requests.post("https://studio.apollographql.com/public/SpaceX-pxxbxen/variant/current/explorer", json={'query': query_company_ceo_coo_name})
    assert response.status_code == 200
    jsonOut = response.json()
    assert jsonOut != ""
