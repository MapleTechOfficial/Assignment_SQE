# This is a sample Python script.
import requests

def main():
    API = 'http://localhost:3000/api/session'
    USERDATA = {'username': 'hassan210302@gmail.com', 'password': 'hassan210302'}
    HEADERS = {'Content-Type': 'application/json'}

    token = requests.post(url=API, json=USERDATA, headers=HEADERS)
    bearer = token.json()['id']
    print("Token Generated: " + bearer)

    API_DB = 'http://localhost:3000/api/user/current'
    HEADERS_DB = {'Content-Type': 'application/json', 'X-Metabase-Session': bearer}

    x = requests.get(url=API_DB, headers=HEADERS_DB)
    if x.status_code == 200:
        print("User information is get succesfully")
        print("Information of user is as follow:")
        print(x.json())
    else:
        print("Error Occurred, Status Code: " + str(x.status_code))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
