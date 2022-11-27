# Task 5 - Exploring existing Unit Testing
(BY: Muhammad Abdullah)
## Unit test
### validate.unit.spec.js
#### Metabase uses Javascript language for its frontend development and uses the React Framework as well. 
- First of all, I open the Metabase Documentation from its GitHub Site (https://github.com/metabase/metabase)
- Then for UI exploration, I went to the 'frontend' folder (https://github.com/metabase/metabase/tree/master/frontend)
- Here I selected the 'test' folder (https://github.com/metabase/metabase/tree/master/frontend/test)
- Then I selected the 'metabase' folder inside the test folder (https://github.com/metabase/metabase/tree/master/frontend/test/metabase)
- Here I selected 'lib' folder (https://github.com/metabase/metabase/tree/master/frontend/test/metabase/lib)
- Here I selected the unit test of 'validate.unit.spec.js' (https://github.com/metabase/metabase/blob/master/frontend/test/metabase/lib/validate.unit.spec.js)
- The code for this test case is available on [validate unit test](https://github.com/metabase/metabase/blob/master/frontend/test/metabase/lib/validate.unit.spec.js)

- First of all it import the validate as 'import validate, { validators } from "metabase/lib/validate"'
- This unit test check 2 test cases.
 #### Test 1 (checking Required)
- This test is enclosed in the Test of validator as its purpose is to validate the required date

  ```
  describe("required", () => {
      ---------
      });
  ```
- Inside it, there is a test case for validation which validate the required things like
  - should return an error if the value is null
   ```
   it("should return an error if the value is null", () => {
      expect(validators.required()(null)).toBe("required");
    });
   ```
  - should return an error if the value is undefined
  ```
  it("should return an error if the value is undefined", () => {
      expect(validators.required()(undefined)).toBe("required");
    });
  ```
  - should return an error if the value is an empty string
  ```
  it("should return an error if the value is an empty string", () => {
      expect(validators.required()("")).toBe("required");
    });
  ```
  - should return an error if the value is a non-empty string
  ```
  it("should return an error if the value is a non-empty string", () => {
      expect(validators.required()("asdf")).toBeFalsy();
    });
  ```
  - should return an error if the value is a number
  ```
   xit("should return an error if the value is a number", () => {
      expect(validators.required()(0)).toBeFalsy();
    });
  ```
- The overall code for first test case is:
```
describe("validators", () => {
  describe("required", () => {
    it("should return an error if the value is null", () => {
      expect(validators.required()(null)).toBe("required");
    });
    it("should return an error if the value is undefined", () => {
      expect(validators.required()(undefined)).toBe("required");
    });
    it("should return an error if the value is an empty string", () => {
      expect(validators.required()("")).toBe("required");
    });
    it("should return an error if the value is a non-empty string", () => {
      expect(validators.required()("asdf")).toBeFalsy();
    });
    xit("should return an error if the value is a number", () => {
      expect(validators.required()(0)).toBeFalsy();
    });
  });
});
```

 #### Test 2 (checking validate)  
- This test check for 2 test cases and 1 Test
  - should have the validators as methods
  ```
  it("should have the validators as methods", () => {
    expect(validate.required()()).toBe("required");
  });
  ```
  - should return chainable validators that returns the first error by default
  ```
  it("should return chainable validators that returns the first error by default", () => {
    expect(validate.required().email()()).toBe("required");
    expect(validate.required().email()("asdf")).toBe(
      "must be a valid email address",
    );
   ```
- The other test in this test case is for checking all  
```
describe("all", () => {
    expect(validate.required().email().all()()).toEqual([
      "required",
      "must be a valid email address",
    ]);
  });
 ```
 ##  The overall code for validate is 
 ```
 describe("validators", () => {
  describe("required", () => {
    it("should return an error if the value is null", () => {
      expect(validators.required()(null)).toBe("required");
    });
    it("should return an error if the value is undefined", () => {
      expect(validators.required()(undefined)).toBe("required");
    });
    it("should return an error if the value is an empty string", () => {
      expect(validators.required()("")).toBe("required");
    });
    it("should return an error if the value is a non-empty string", () => {
      expect(validators.required()("asdf")).toBeFalsy();
    });
    xit("should return an error if the value is a number", () => {
      expect(validators.required()(0)).toBeFalsy();
    });
  });
});

describe("validate", () => {
  it("should have the validators as methods", () => {
    expect(validate.required()()).toBe("required");
  });
  it("should return chainable validators that returns the first error by default", () => {
    expect(validate.required().email()()).toBe("required");
    expect(validate.required().email()("asdf")).toBe(
      "must be a valid email address",
    );
  });
  describe("all", () => {
    expect(validate.required().email().all()()).toEqual([
      "required",
      "must be a valid email address",
    ]);
  });
});
```
## Output
 ![Test Case Result]([https://i.imgur.com/zOW0tVB.jpg](https://drive.google.com/file/d/1_tgCuG4iQlOOrXFNrapmY9fmLGVmeEqL/view))
 
