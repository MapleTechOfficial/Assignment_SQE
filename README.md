# Software Quality Engineering - Project - Phase 2
![Metabase](https://i.ibb.co/g98Tdbw/metabase.png)
 ## About Metabase
 Metabase is an open-source project for managing companies data and get future prospects or business insights from it.
 - It uses clojure language with REST API as their backend framework and Javascript, HTML and css for their web interface.
 - It uses SQL for its own database.
 - To setup a testing environment of the framework, you will need to run both:
   - Frontend using: 
    ```
    $ javascript dependencies
    $ yarn
    $ yarn build-hot
    ```
   - Backend using:
   ```
    $ clojure -M:run
   ```          
 - It uses cypress testing which can be run using `yarn test`

## About this Assignment
This assignment phase was done on PyCharm IDE and it uses python language as its main framework. It also has BDD Testing which includes Gerkin Langauge.
 To Setup the project:
 - Clone or Download this project and extract the zip file
 - Simply Download PyCharm IDE
 - Go to File > Open > path/to/assignment
  - For using the BDD testing, you will need to add the behave & selenium library to the project settings:
    - Go to File > New Project Setup > Settings For New Project > Python Interpreter.
    - Here choose your python version and click the + icon and add two libraries: 
      1. Selenium
      2. Behave

## Metabase Selenium Testing
- The selenium testing files are in `Selenium Automation/` Folder.
- You can run the test file in Terminal using the command `behave filename.feature`
- Before running the test, make sure to add your chrome driver path in the `executable_path= path/to/chromedriver`

## Metabase Web API Testing
- The web api testing files are in `Web API Automation/` Folder.
- Before doing any action on metabase, you will need an access token of the account which is the first part of the code in python:
```
API = 'http://localhost:3000/api/session'
USERDATA = {'username': 'admin@metabase.com', 'password': 'admin@123'}
HEADERS = {'Content-Type': 'application/json'}

token = requests.post(url=API, json=USERDATA, headers=HEADERS)
```
- The token is received in the following format: ` {"id":"e7863c39-d5af-4862-b135-d8e2bd3ca939"}` and it has to be added in all the next request headers using `X-Metabase-Session: {token}`. Be advised that this token will get expired after 14 days.
- The next part is of Posting request to do an action on the site such as: add a database:
```
x = requests.post(url=API_DB, json=DATA_DB, headers=HEADERS_DB)
if x.status_code == 200:
    print("Database Added Successfully!")
else:
    print("Error Occurred, Status Code: " + str(x.status_code))
```
- There are several status code on the site such as 404, 403, which all means, in simple terms, that the post request field except the status code 200.
- For other requests type, you can visit the following link: [Metabase Database API](https://www.metabase.com/docs/latest/api/database)
