
# actuate_test/url_shortener_test

## Instructions on how to run the tests

### 1. **Setup**

Before running the tests, ensure you have the following installed:

- **Python** (version 3.7 or higher)
- **Allure** (for generating test reports)

#### Installing Dependencies

1. **Install Python** (if not already installed): [Python Downloads](https://www.python.org/downloads/)
2. Clone this repository to your local machine:
   ```bash
   git clone git@github.com:devraoniferreira/actuate_test.git
   cd actuate_url_shortener-main
   ```
3. Install the dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```
   This will install the following libraries:
   - `selenium` – for automating browser interactions
   - `behave` – for behavior-driven development (BDD) testing
   - `requests` – for making HTTP requests in tests
   - `pytest` – for running tests and test discovery
   - `allure` – for generating test reports

4. Install Allure Commandline (if not already installed):
   - Download the latest Allure release from [GitHub Allure Releases](https://github.com/allure-framework/allure2/releases).
   - Extract the downloaded archive to a directory of your choice (e.g., `C:\allure`).
   - Add the extracted directory to your system’s `PATH` to run Allure from the command line.

### 2. **Running the Tests**

- **Run Behave Tests**:
  After installing the dependencies, run your tests using Behave with the following command:
  ```bash
  behave --format allure_behave.formatter:AllureFormatter --outfile ./allure-results
  ```
  Replace `C:\path\to\your\allure-results` with the desired location for storing the test results.

- **Run Tests with Pytest** (Optional):
  If you prefer to run tests with `pytest`, use the following command:
  ```bash
  pytest
  ```
  This will discover and run all tests in the project.

### 3. **Generate Allure Report**

After running the tests, generate the Allure report by running:
```bash
allure serve ./allure-results --output ./allure-report
```


### 4. **Viewing the Allure Report**

After running the `allure serve` command, Allure will automatically open a browser window displaying the test report.




The approach used was to perform manual tests to identify buses and explore the possibilities. Later, the BDD was written, 
which made it possible to develop automation using the 'Page Object Model'.

Then, the API test was performed, which was initially explored in Postman and later the automation was coded with Python.

To finish, I implemented CI/CD to run the tests and ensure continuous execution and software quality.
With the integration of CI/CD, the tests were automated in the pipeline, 
ensuring rapid feedback on possible failures and facilitating project maintenance.