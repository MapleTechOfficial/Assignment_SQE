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
- There are several status code on the site such as 404, 403, which all means, in simple terms, that the post request field except the status code 200.
# Task 4 - Exploring existing UI and API Automation Tests
## Existing Metabase UI Testing
- The metabase front end tests were done in js. The source code of the tests is on the following folder: [Metabase UI Automation](https://github.com/metabase/metabase/blob/master/frontend/test/metabase)
- I explored the test case of collections feature which is written in `BaseItemsTable.unit.spec.js` file
- The first test is of opening the dashboard: A sample Item object is created `const ITEM = {...}` which has data like id, name, model.
- The item is inserted into the dashboard url ` getUrl: () => "/dashboard/1"`
- Then a test is written in it( which expects the result John Doe which was inserted using the Item Object and checks its date and time
 ```
  it("displays item data", () => {
    const { getByText } = setup();
    const lastEditedAt = moment(timestamp).format("MMMM DD, YYYY");

    expect(getByText(ITEM.name)).toBeInTheDocument();
 ```
 - The test below it checks the format and last edit time.

## Existing Metabase Automation Testing
- Metabase testing was done using clojure language. 
- We can find many examples which are similar to the explanations above on the following link: [Metabase API Automation](https://github.com/metabase/metabase/blob/master/test/metabase/api)
- For task 4, I am using the `slack_test.clj` which is explained below
  - The first few lines are of required test cases which is to obtain the session token:
  ```
    (:require [clojure.string :as str]
            [clojure.test :refer :all]
            [java-time :as t]
            [metabase.config :as config]
            [metabase.integrations.slack :as slack]
            [metabase.test :as mt]))
  ```
  
  - Then a function is defined using `deftest update-slack-settings-test` which will test the settings for slack. This test is about setting the slack api token in metabase settings. The following lines are conditions to be true for running the test which is a prerequirement.
  ```
   (with-redefs [slack/valid-token?                                (constantly true)
                    slack/channel-exists?                             (constantly true)
                    slack/refresh-channels-and-usernames!             (constantly nil)
                    slack/refresh-channels-and-usernames-when-needed! (constantly nil)]
  ```
  - It then assigns a token named "Fake token" which is ofcourse an invalid token to test the field. It must show an error with status code 400 which will pass the test.
```
slack-token     "fake-token"]
          (mt/user-http-request :crowberto :put 200 "slack/settings" {:slack-app-token "fake-token"})
          (is (= "fake-token" (slack/slack-app-token)))
          (is (= nil (slack/slack-token))))))

    (testing "A 400 error is returned if the Slack app token is invalid"
```
Similarly, other test cases for running on slack settings are given below in the file.
