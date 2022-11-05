# Task 5 - Existing Unit Test Exploration
- In this task, I am going to explore the test case `frontend/test/metabase/query_builder/selectors.unit.spec.js`
- The test case is written in JavaScript and uses React as well
- It further imports the metabase's own question library which has an import of "icepick" library which is used to deal with *frozen JavaScript objects as persistent immutable collections*
- The code also imports and intitializes a sample database
- The first function is starting from `line: 34     describe("getQuestion"`
- This is for getting the question from database and has 4 tests which start from `it`
- The first test case is to test that if there are no cards it should return a null result. `line 35:     it("should be nothing if card data is missing", () `
  ```
  line 36:    const state = getBaseState({ card: null });
  line 37:    expect(getQuestion(state)).toBe(undefined);
  ```
  - As stated in the code, if card state is null then we should expect the question to be undefined which will pass the test.
- The second test is a sample card which have a data such as an id, type or query `line 40:     it("should return question instance correctly", ()`
```
const card = {
      id: 5,
      dataset_query: {
        database: 1,
        type: "query",
        query: {
          "source-table": 1,
        },
      },
    };
```
  - In this case a sample card with data was sent to a question and upon the return from getquestion we should expect it to be equal to card. `xpect(question.card()).toEqual(card);`
- Similarly the other two test cases test the outputs when dataset is enabled.

# Execution
- The test case can be executed by running `yarn test-unit selectors.unit.spec.js`. *Prerequistes are given in MEETING3.md*
- Attached below are the results of execution:

  ![Test Result](https://i.ibb.co/GFgjQLF/Screenshot-from-2022-11-05-16-11-01.png)
- Upon running the test case 3 times: **the average exectuion time was 57.78 seconds**
