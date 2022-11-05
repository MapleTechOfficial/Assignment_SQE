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
 - Both scenarios were passed upon running the test case.
 - The results from terminl are here: 
  ![Test Case Result](https://i.ibb.co/wdDNSFs/Screenshot-from-2022-11-05-14-16-30.png)
  
 - The average *execution time was 89.78s*
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


## Email testing 

(Author: Hassan Rehman)

### Send email

- Send a test email using the SMTP Settings. You must be a superuser or have setting permission to do this. Returns {:ok true} if we were able to send the message successfully, otherwise a standard 400 error response.

The code for this is 

```
(deftest test-email-settings-test
  (testing "POST /api/email/test -- send a test email"
    (mt/with-temporary-setting-values [email-from-address "notifications@metabase.com"
                                       email-from-name    "Sender Name"
                                       email-reply-to     ["reply-to@metabase.com"]]
      (mt/with-fake-inbox
        (testing "Non-admin -- request should fail"
          (is (= "You don't have permissions to do that."
                 (mt/user-http-request :rasta :post 403 "email/test")))
          (is (= {}
                 @mt/inbox)))
        (is (= {:ok true}
               (mt/user-http-request :crowberto :post 200 "email/test")))
        (is (= {"crowberto@metabase.com"
                [{:from     "Sender Name <notifications@metabase.com>",
                  :to       ["crowberto@metabase.com"],
                  :reply-to ["reply-to@metabase.com"]
                  :subject  "Metabase Test Email",
                  :body     "Your Metabase emails are working — hooray!"}]}
               @mt/inbox))))))

```

- The first two test is for non admin setting and fake email test it must return 403. 

- Then it will return ok true in case email is send successfully. In function we set the from too replytoo and other parameters for the email 

### Update email setting

- Update multiple email Settings. You must be a superuser or have setting permission to do this. 
   -This include changing password and port 

```
            (is (= default-email-settings
                         (email-settings)))))))))))
  (testing "Updating values with obfuscated password (#23919)"
    (mt/with-temporary-setting-values [email-from-address  "notifications@metabase.com"
                                       email-from-name     "Sender Name"
                                       email-reply-to      ["reply-to@metabase.com"]
                                       email-smtp-host     "www.test.com"
                                       email-smtp-password "preexisting"]
      (with-redefs [email/test-smtp-connection (fn [settings]
                                                 (let [obfuscated? (str/starts-with? (:pass settings) "****")]
                                                   (is (not obfuscated?) "We received an obfuscated password!")
                                                   (if obfuscated?
                                                     {::email/error (ex-info "Sent obfuscated password" {})}
                                                     settings)))]
```
This is updating setting with the obfuscatedpassword

- Then there is code to check if SMTP connection is valid

```
 (testing "If we don't change the password we don't see the password"
          (let [payload  (-> (email-settings)
                             ;; user changes one property
                             (assoc :email-from-name "notifications")
                             ;; the FE will have an obfuscated value
                             (update :email-smtp-password setting/obfuscate-value))
                response (mt/user-http-request :crowberto :put 200 "email" payload)]
            (is (= (setting/obfuscate-value "preexisting") (:email-smtp-password response)))))
        (testing "If we change the password we can receive the password"
          (let [payload  (-> (email-settings)
                             ;; user types in a new password
                             (assoc :email-smtp-password "new-password"))
                response (mt/user-http-request :crowberto :put 200 "email" payload)]
            (is (= "new-password" (:email-smtp-password response)))))))))
```

This is code for changing password these are all setting about the changing setting or default setting for sending email

### Deleting all Email setting 

- This is code for setting all emails setting to nil

```
(deftest clear-email-settings-test
  (testing "DELETE /api/email"
    (tu/discard-setting-changes [email-smtp-host email-smtp-port email-smtp-security email-smtp-username
                                 email-smtp-password email-from-address email-from-name email-reply-to]
      (with-redefs [email/test-smtp-settings (constantly {::email/error nil})]
        (is (= (-> default-email-settings
                   (assoc :with-corrections {})
                   (update :email-smtp-security name))
               (mt/user-http-request :crowberto :put 200 "email" default-email-settings)))
        (let [new-email-settings (email-settings)]
          (is (nil? (mt/user-http-request :crowberto :delete 204 "email")))
          (is (= default-email-settings
                new-email-settings))
          (is (= {:email-smtp-host     nil
                  :email-smtp-port     nil
                  :email-smtp-security :none
                  :email-smtp-username nil
                  :email-smtp-password nil
                  :email-from-address  "notifications@metabase.com"
                  :email-from-name     nil
                  :email-reply-to      nil}
                 (email-settings))))))))

```



