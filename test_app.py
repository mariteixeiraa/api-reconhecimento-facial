import unittest
from app import app
from unittest.mock import patch

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'FaceScan', response.data)

    @patch('subprocess.run')
    def test_run_scan(self, mock_subprocess_run):
        response = self.app.post('/run-scan')
        mock_subprocess_run.assert_called_once_with(['python', 'facial.py'])
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, 'http://localhost/')

if __name__ == '__main__':
    unittest.main()
