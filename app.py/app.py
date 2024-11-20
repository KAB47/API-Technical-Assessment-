"""
Portfolio Link (Anonymous): Contains projects relevant to this role, including APIs, websites/web applications, and more.
View here: https://drive.google.com/drive/folders/1N0sGpquz38ap66RjcvVWaUVMfzkRENh3
I use GitHub but currently revamping my profile.
I would be happy to discuss this API project and any of the additional projects I have done, relevant to this position
and apply the interactions/improvements in real time.

Since applying, I've started a Software and Web Developer internship at a finance company,
contributing to APIs, production-ready code, and enhancing large web applications.
I’m available to transition to this role, at Canonical on short notice.
"""

# Development Checklist:
# - Execute Postman testing - COMPLETED
# - Implement unit tests - COMPLETED
# - Conduct end-to-end testing - COMPLETED
# - Prepare documentation - COMPLETED

"""
Testing Methods: 
(Refer to README.md file for full instructions for testing.)
Postman (API and automated testing)
Unit tests
End-to-end testing - (Through creating .html pages that you can use yourself.) 
Use the .html code base in the project template folder -
After booting up the server, paste the server URL into your browser to access the .html files.)

Extra:
Created simple html pages for end2end testing
Added a get report button to easily navigate to report instead of changing url.
"""

from flask import Flask, request, render_template, jsonify, Response
import csv

app = Flask(__name__)
print(__name__)

# List to store validated CSV transactions, for use in the 'upload_file' method
transactions = []

# Route to render .html page for CSV file uploads (end-to-end tested)
@app.route('/')
def index():
    return render_template('upload.html', transactions_uploaded=False)

@app.route('/transactions', methods=['POST'])
def upload_file():
    """Method for uploading CSV files containing transaction data.
    The data is validated, processed, and stored for reporting.
    """

    # Define the uploaded file
    file = request.files.get('file')

    # Process and read the uploaded CSV file
    upload_file = file.read().decode('utf-8').splitlines()
    read_file = csv.reader(upload_file)

    # Validate each line, ensuring only correctly formatted lines are added to the transactions list.
    for line in read_file:
        # Criteria: Skip empty lines or those with fewer than 4 columns (e.g., line 4 in the CSV, "# new spark plugs I think," is invalid).
        if len(line) < 4:
            continue

        # Append validated lines to the transactions list.
        transactions.append({
            'Date': line[0],
            'Type': line[1].strip(),
            'Amount': float(line[2]),
            'Memo': line[3]
        })



    # Return confirmation message and validated transactions as a JSON object.
    return jsonify({"message": "File uploaded successfully", "transactions": transactions}), 200,


@app.route('/report', methods=['GET'])
def get_report():

    """
    Method to generate a report, summarising total gross income, expenses, and net revenue.
    This method utilises data from the validated 'transactions' list produced in the 'upload_file' method.
    """

    # Initialise lists to store income and expense totals.
    gross = []
    expense = []

    # Populate gross and expense lists based on transaction type.
    for line in transactions:
        if line.get("Type") == "Expense":
            expense.append(line.get("Amount", 0))
        elif line.get("Type") == "Income":
            gross.append(line.get("Amount", 0))

    # Calculate net revenue by subtracting expenses from gross income.
    revenue = float(sum(gross) - sum(expense))

    # Return computed totals in a JSON format.
    return jsonify({"gross-revenue": sum(gross), "expenses": sum(expense), "net-revenue": revenue})

"""
Potential iteration:  
Aim: Create a function(s) and route(s) to locate, replace, update and delete a transaction 
by its attributes (e.g. dates, expenses, incomes or price threshold) to search within large datasets.
"""

if __name__ == "__main__":
    app.run(port=5000)



"""
Improvements that could be made:
•	Create a function(s) and route(s) to locate, replace, update and delete a transaction by its attributes 
(e.g. dates, expenses, incomes or price threshold)
•	Add responses to give out more Fine-Grained error handling
•	Edge cases for wrong or faulty file upload
•	edge cases e.g. if no file or the wrong type of file was uploaded



draft:
def correct_list(transactions):
    i = 0
    for line in transactions:
        if not ("Date" in line and "Type" in line and "Amount" in line and "Memo" in line):
            transactions.pop(i)
            response = Response("", status=204)
            return response
        i += 1
        corrected_list = {
            "error": "Some rows in your file did not contain exactly four fields (Date, Type, Amount, Memo). "
                     "These rows have been removed for consistency."
        }
        response = Response(json.dumps(corrected_list), status=404, mimetype='application/json')
    return response 
    
    """