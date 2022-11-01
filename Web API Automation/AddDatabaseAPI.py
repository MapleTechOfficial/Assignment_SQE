import requests
API = 'http://localhost:3000/api/session'
USERDATA = {'username': 'admin@metabase.com', 'password': 'admin@123'}
HEADERS = {'Content-Type': 'application/json'}

token = requests.post(url=API, json=USERDATA, headers=HEADERS)
bearer = token.json()['id']
print("Token Generated: " + bearer)

API_DB = 'http://localhost:3000/api/database'
DATA_DB = {'engine': 'mysql', 'name': 'MyNewAPIDatabase', 'details': {'host': 'qvti2nukhfiig51b.cbetxkdyhwsb.us-east-1.rds.amazonaws.com', 'port': '3306', 'db': 'j0uf2qniu2pa8oo4', 'user': 'g87uxt2ng0i5bnlg', 'password': 'jqszjdxvgdcotq9a'}}
HEADERS_DB = {'Content-Type': 'application/json', 'X-Metabase-Session': bearer}

x = requests.post(url=API_DB, json=DATA_DB, headers=HEADERS_DB)
db_id = x.json()['id']
if x.status_code == 200:
    assert True, "Test Scenario Passed"
    print("Test Scenario Passed")
    API_DB = 'http://localhost:3000/api/database/%s' % db_id #Delete the added database to reset
    r = requests.delete(url=API_DB, json=DATA_DB, headers=HEADERS_DB)
else:
    assert False, "Test Scenario Failed"
    print("Test Scenario Failed")

