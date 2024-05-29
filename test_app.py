import unittest
from unittest.mock import patch
from app import app

class TestRunScan(unittest.TestCase):

    @patch('my_module.subprocess.run')
    def test_run_scan(self, mock_subprocess_run):
        # Arrange

        # Act
        with app.test_client() as client:
            client.post('/run-scan')

        # Assert
        mock_subprocess_run.assert_called_once_with(['python', 'facial2.py'])

if __name__ == '__main__':
    unittest.main()
