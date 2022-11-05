# Task 4 - Exploring existing UI and API Automation Tests
(BY: Muhammad Abdullah)
## Existing Metabase UI Testing
### Metabase uses Javascript language for its frontend development and uses the React Framework as well. 
- First of all, I open the Metabase Documentation from its GitHub Site (https://github.com/metabase/metabase)
- Then for UI exploration, I went to the 'frontend' folder (https://github.com/metabase/metabase/tree/master/frontend)
- Here I selected the 'test' folder (https://github.com/metabase/metabase/tree/master/frontend/test)
- Then I selected the 'metabase' folder inside the test folder (https://github.com/metabase/metabase/tree/master/frontend/test/metabase)
- Here I explore the test case of 'Components' feature (https://github.com/metabase/metabase/tree/master/frontend/test/metabase/components)
- In that folder, the feature is written in 'PasswordReveal.unit.spec.js' file 
           (https://github.com/metabase/metabase/blob/master/frontend/test/metabase/components/PasswordReveal.unit.spec.js)
           
           
- The Only test written in it is of the Revealing the password `describe("password reveal", () => {})`
   
   
- The first implementation of the test is about the visibility state of the password when the 'hide/show' are clicked

  ````
   it("should toggle the visibility state when hide / show are clicked", () => {
    const { getByText } = render(<PasswordReveal />);

    fireEvent.click(getByText("Show"));
    getByText("Hide");
  });
  ````
  
  
- The second implementation of the test is about the rendering of the copy button

  ````
    it("should render a copy button", () => {
    const { getByTestId } = render(<PasswordReveal />);
    // implicit assertion => it will throw an error if element is not found
    getByTestId("copy-button");
  });
  ````
  
  
- So the overall test of the Password Revealing is as follows:

  ```
    describe("password reveal", () => {
  it("should toggle the visibility state when hide / show are clicked", () => {
    const { getByText } = render(<PasswordReveal />);

    fireEvent.click(getByText("Show"));
    getByText("Hide");
  });

  it("should render a copy button", () => {
    const { getByTestId } = render(<PasswordReveal />);
    // implicit assertion => it will throw an error if element is not found
    getByTestId("copy-button");
  });
 });
 ```
 
- For doing this test they import the following, 
      -import the "react" from React
      -import { render, fireEvent } from "@testing-library/react"
      -import PasswordReveal from "metabase/components/PasswordReveal";
      
# Existing Metabase Automation Testing
## Metabase testing was done using clojure language. 
-First of all, I open the Metabase Documentation from its GitHub Site (https://github.com/metabase/metabase)
-Then for API exploration, I went to the 'test/metabase' folder (https://github.com/metabase/metabase/tree/master/test/metabase)
-Then inside this folder I select the 'api' folder (https://github.com/metabase/metabase/tree/master/test/metabase/api)
-Here I have selected the 'premium_features_test.clj' file for API (https://github.com/metabase/metabase/blob/master/test/metabase/api/premium_features_test.clj)
-In order to start the API testing, we have to fetch the API Token first. This can be done as:

    ````
    (ns metabase.api.premium-features-test
  (:require [clojure.test :refer :all]
            [metabase.public-settings.premium-features :as premium-features]
            [metabase.public-settings.premium-features-test :as premium-features-test]
            [metabase.test :as mt]))))
    ````
-Then a function is defined using 'get-token-status-test' which will test the token status. Here, we obviously use fake token for our testing.
-First it will fetch the status of the fake token
   
   ````
   (deftest get-token-status-test
  (testing "GET /api/premium-features/token/status"
    (with-redefs [premium-features/fetch-token-status (fn [_x]
                                                        {:valid    true
                                                         :status   "fake"
                                                         :features ["test" "fixture"]
                                                         :trial    false})])))
   ````
   
-Then, if it satisfy the passing parameters like 'valid','status','features','trials', it should return the "returns correctly" meassage
-Here it will return the 200 as status

  ````
  (mt/with-temporary-setting-values [:premium-embedding-token premium-features-test/random-fake-token]
        (testing "returns correctly"
          (is (= {:valid    true
                  :status   "fake"
                  :features ["test" "fixture"]
                  :trial    false}
                 (mt/user-http-request :crowberto :get 200 "premium-features/token/status")))))
  ````
-If the current user is not the superuser(Admin) it will return the 403 error code
-403 error code means it is forbidding the user to access the valid URL

  ````
  (testing "requires superusers"
          (is (= "You don't have permissions to do that."
                 (mt/user-http-request :rasta :get 403 "premium-features/token/status"))))
  ````
  
-The overall API Test for the permission will be as:

  ````
  (ns metabase.api.premium-features-test
  (:require [clojure.test :refer :all]
            [metabase.public-settings.premium-features :as premium-features]
            [metabase.public-settings.premium-features-test :as premium-features-test]
            [metabase.test :as mt]))

(deftest get-token-status-test
  (testing "GET /api/premium-features/token/status"
    (with-redefs [premium-features/fetch-token-status (fn [_x]
                                                        {:valid    true
                                                         :status   "fake"
                                                         :features ["test" "fixture"]
                                                         :trial    false})]
      (mt/with-temporary-setting-values [:premium-embedding-token premium-features-test/random-fake-token]
        (testing "returns correctly"
          (is (= {:valid    true
                  :status   "fake"
                  :features ["test" "fixture"]
                  :trial    false}
                 (mt/user-http-request :crowberto :get 200 "premium-features/token/status"))))

        (testing "requires superusers"
          (is (= "You don't have permissions to do that."
                 (mt/user-http-request :rasta :get 403 "premium-features/token/status"))))))))
   `````
