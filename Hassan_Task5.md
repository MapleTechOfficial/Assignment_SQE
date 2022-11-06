# Task 5
(author: Hassan Rehman)
## Unit test

### Logs.unit.spec.js

- The code for this is available in [log unit test](https://github.com/metabase/metabase/blob/master/frontend/test/metabase/admin/tasks/containers/Logs.unit.spec.js)

for explanation the code is 

```
import React from "react";
import { render, screen } from "@testing-library/react";
import mock from "xhr-mock";
import Logs from "metabase/admin/tasks/containers/Logs";

import { UtilApi } from "metabase/services";

describe("Logs", () => {
  describe("log fetching", () => {
    beforeEach(() => mock.setup());
    afterEach(() => mock.teardown());

    it("should call UtilApi.logs after 1 second", () => {
      jest.useFakeTimers();
      mock.get("/api/util/logs", {
        body: JSON.stringify([]),
      });
      render(<Logs />);
      const utilSpy = jest.spyOn(UtilApi, "logs");

      screen.getByText("Loading...");
      jest.advanceTimersByTime(1001);
      expect(utilSpy).toHaveBeenCalled();
    });
  });
});

```
- This code is written in js and import react so it is also using react
- It also include UPI API because it need some data for UTILAPI
- Describe is used to group together the test cases 
  - At the start we use before each which is use to mock.setup, it means before every it mock will setup and will tear down after it
- In first it, we use a timer to get logs after 1 sec through api 
  - After this we use JSON.stringify which will convert the json in string
- for jest.spy on what i found on net was

```
jest.spyOn(object, methodName, accessType?)
Since Jest 22.1.0+, the jest.spyOn method takes an optional third argument of accessType that can be either 'get' or 'set', which proves to be useful when you want to spy on a getter or a setter, respectively.
```
It will compare with getter in this case 

- It is then waiting for loading on screen and then wait for sometime
- In the last line, it expects what need to be done

## RESULTS

![image](https://user-images.githubusercontent.com/82565130/200183522-a7bb671c-45d3-410d-bbd5-049343b31f99.png)


