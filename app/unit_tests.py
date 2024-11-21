import unittest

from app import app

class UnitTests(unittest.TestCase):
    # Initialises the test client, so it can be used to make requests in the app instead of starting a server.
    def setUp(self):
        self.client = app.test_client()

    def test_routes(self):
        # Method to test if app routes works.
        with open(r'C:\Users\Fyl\Downloads\technical_assessment\data.csv', 'rb') as f:
            response_transactions = self.client.post('/transactions', data={'file': (f, 'data.csv')}) # Check if the '/transactions' route works
        response_report = self.client.get('/report') # Check if the '/report' route works
        self.assertEqual(response_transactions.status_code, 200) # Validate the correct response from '/transactions' route
        self.assertEqual(response_report.status_code, 200) # Validate the correct response from the '/report' route


    def test_post_requests(self):
        # Method to test if 'POST' request for CSV file works.
        response = self.client.post('/transactions', data={'file':(open(r'C:\Users\Fyl\Downloads\technical_assessment\data.csv', 'rb'), 'data.csv')}) # Verify the csv file is uploaded
        self.assertEqual(response.status_code, 200) # Verify the upload is successful
        self.assertIn("File uploaded successfully", response.get_json().get("message")) # Verify the transaction page message
        # displays the according message

    def test_get_report(self):
        # Method to test if 'GET' request for the report works.
        response = self.client.get('/report')
        self.assertEqual(response.status_code, 200)  # Verify '/report' route is successful
        self.assertIn("gross-revenue", response.get_json()) # Verify 'gross-revenue' value is presented
        self.assertIn("expenses", response.get_json()) # Verify 'expenses' value is presented
        self.assertIn("net-revenue", response.get_json()) # Verify 'net-revenue' value is presented


if __name__ == '__main__':
    unittest.main()

