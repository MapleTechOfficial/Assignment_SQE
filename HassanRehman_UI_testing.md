
## UI testing 
(Author: hassan rehman)
- Metabase UI tesing is available on the [Metabase End to End testing guideline](https://www.metabase.com/docs/latest/developers-guide/e2e-tests)
  - When you open this link it will provide you step to step points for UI testing. I have explore this testing but failed to deploy them. The error i faced was that module not found. I attached the screen shot for this purpose
 ![image](https://user-images.githubusercontent.com/82565130/200124875-207158d8-8519-4b5c-8f10-00867272f124.png)
  - It take me hour to setup the project but the UI testing fails 
  - The text case I selected for the UI testing is named as [Query external](https://github.com/metabase/metabase/blob/master/frontend/test/metabase/scenarios/question/query-external.cy.spec.js)
  - You can open this link for detailed code
 
### Code 

```
import { restore, startNewQuestion, visualize } from "__support__/e2e/helpers";

const supportedDatabases = [
  {
    database: "Mongo",
    snapshotName: "mongo-4",
    dbName: "QA Mongo4",
  },
  {
    database: "MySQL",
    snapshotName: "mysql-8",
    dbName: "QA MySQL8",
  },
];

supportedDatabases.forEach(({ database, snapshotName, dbName }) => {
  describe("scenarios > question > query > external", () => {
    beforeEach(() => {
      cy.intercept("POST", "/api/dataset").as("dataset");

      restore(snapshotName);
      cy.signInAsAdmin();
    });

    it(`can query ${database} database`, () => {
      startNewQuestion();
      cy.findByText(dbName).click();
      cy.findByText("Orders").click();

      visualize();
      cy.contains("37.65");
    });
  });
});

```

- The first import is importing of already written test cases
  - Then we save values in a hash map and store values on which we want to execute test case
  - In the first line there is loop which is for each database, there are mainly two databases
  - Then there is a describe word that is used to group together the test case
  - We sign in as admin using our existing test case signin as admin 
  - The before each will run before every it 
  - Then in it we run start new question test case and using cypass we find dbname declare in the hash above
  - Then we click on order 
  - Then we call the test case of visualize 
  - We use cyphass.contain that is used for "Get the DOM element containing the text. DOM elements can contain more than the desired text and still match. Additionally, Cypress prefers some DOM elements over the deepest element found."
  
