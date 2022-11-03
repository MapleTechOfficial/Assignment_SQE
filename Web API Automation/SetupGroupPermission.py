import requests

API = 'http://localhost:3000/api/session'
USERDATA = {'username': 'abdullah@123.com', 'password': 'abdullah@123'}
HEADERS = {'Content-Type': 'application/json'}

token = requests.post(url=API, json=USERDATA, headers=HEADERS)
bearer = token.json()['id']
print("Token Generated: " + bearer)

API_DB = 'http://localhost:3000/api/permissions/group'
DATA_DB ={ 'group_id': '2', 'user_id': '2', 'is_group_manager': 'false'}
HEADERS_DB = {'Content-Type': 'application/json', 'X-Metabase-Session': bearer}

x = requests.get(url=API_DB, json=DATA_DB, headers=HEADERS_DB)
if x.status_code == 200:
    assert True, "Test Scenario Passed"
    print("Test Scenario Passed")
    print("Successfuly")
    print(x.json())
else:
    print("Error Occurred, Status Code: " + str(x.status_code))
    assert False, "Test Scenario Failed"
    print("Test Scenario Failed")