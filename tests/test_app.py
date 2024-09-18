import unittest
from faker import Faker
from app import app

class TestAPI(unittest.TestCase):#inheriting test case functionality from unittest

    def setUp(self):
        self.app = app.test_client()

    #need to be able to receive two nums and return the sum of the those nums

    def test_sum(self):
        payload = {'num1': 3 , 'num2': 5} #stubbing : create a predefined payload and associate response
        response = self.app.post('/sum', json=payload)
        data = response.json
        self.assertEqual(data['result'], 8)

    def test_random_sum(self): #mocking a payload(random data)
        fake = Faker()
        num1 = fake.random_number(digits=3)
        num2 = fake.random_number(digits=3)
        payload = {'num1': num1, 'num2': num2}
        response = self.app.post('/sum', json=payload)
        data = response.json
        self.assertEqual(data['result'],num1 + num2)

if __name__ == '__main__':
    unittest.main()
