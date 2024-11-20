# Project Overview
This Flask app enables upload of CSV files of financial transactions, for generating reports on income and expenses.

You can test this app using the 
(Unit Tests) unit_tests.py file
(Automated, API testing) Postman
(End-to-End Testing) through entering the server URL into your browser to use the .html page.

I have provided instructions for all, in the sections below.

## Instructions for Environment Setup and Running Your Code and Tests
You do not need to set up a virtual environment, as it has already been done.

Setting up the project:
1. Download the 'API' folder and Unzip the file and open `app.py` to view the code base.
2. Open Command Prompt or Terminal as Administrator.
3. Navigate to the folder containing `app.py` using `cd <path>`. Example: `cd C:\Users\MyLap\Downloads\API\app.py`. Make sure it's not the folder with the same name but the .py file.
4. Start the server by entering `python app.py`.
5. Copy the server URL (e.g., `http://127.0.0.1:5000`) from Command Prompt and paste it into a browser.
6. On the page, click “Choose File” to upload the 'data' CSV file located in the 'API' project folder and select “Upload.”
7. Transactions will display in the browser.
8. To view the report, replace `/transactions`' with `/report` in the URL to see expenses, gross revenue, and net revenue.

## Testing
1. **Postman - Automated API Testing:** I used this, but there’s no way to send off a ready-made test for you to execute. To test using this method as I did, you must:
   - Download the Postman app and create an account to test the code using Postman. Download Postman here: [Postman Downloads](https://www.postman.com/downloads/) (Below the Windows option, there are downloads for MAC and Linux).
   - You need to send a ‘POST’ request of the file and a ‘GET’ request for the report.
   - Follow this 3-minute tutorial to test for API (‘POST’ and ‘GET’) requests: [YouTube Tutorial](https://www.youtube.com/watch?v=8mBmLDbpIH8).

2. **End-to-End Testing:** To view this test, follow the 8-step process found in the initial section.

3. **To Run the Unit Tests:** You need to install ‘PYTEST’ and ‘SetupTools’. Follow these instructions:
   1. **Install Requirements:**
      - Open a command or terminal window and navigate to your project folder (e.g., `C:\Users\MyLap\Downloads\API`).
   2. **Activate the Virtual Environment:**  
      Run:
      ```bash
      <Project folder location>\venv\Scripts\activate
      ```
   3. **Install `pytest` and `setuptools`:**
      ```bash
      pip install pytest
      pip install pytest setuptools
      ```
   4. **Update File Paths:** In `unit_tests.py`, update the path to the `data.csv` file located in the project folder (e.g. `C:\Users\MyLap\Downloads\API\data.csv`):
      - Line 12: Change the file path to the location of `data.csv` in your project folder.
      - Line 21: Do the same update for line 21.
   5. **Run the Tests:** Run the test on your IDE (Make sure the cursor has last been clicked at the top of the code base, before you run a test, so it tests for all 3 cases). If you can’t run the test in your IDE:
      - In the command line or terminal, navigate to the directory containing `unit_tests.py`.
      - Run the test by entering:
      ```bash
      pytest unit_tests.py
      ```

## Additional Context
- Created a simple HTML page for end-to-end testing. Navigate by following the 8 steps in the initial section.
- I did not need to do unit testing, as I have already done automated API testing using Postman first. I did it to demonstrate skills.
