import unittest
from unittest.mock import patch
from facial2 import send_sms

class TestSendSMS(unittest.TestCase):

    @patch('my_module.Client')
    def test_send_sms(self, mock_client):
        # Arrange
        mock_instance = mock_client.return_value
        mock_message = mock_instance.messages.create.return_value
        mock_message.sid = "mock_sid"

        # Act
        send_sms()

        # Assert
        mock_instance.messages.create.assert_called_once_with(
            body="Rosto detectado por mais de 30 segundos.",
            from_='+17083152521',
            to='+55 31985702668'
        )
        self.assertEqual(mock_message.sid, "mock_sid")

if __name__ == '__main__':
    unittest.main()
