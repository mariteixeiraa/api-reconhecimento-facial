import unittest
from unittest.mock import MagicMock, patch
import cv2
import numpy as np
from facial import send_sms, detect_faces

class TestFacialDetection(unittest.TestCase):

    @patch('facial.Client')
    def test_send_sms(self, MockClient):
        mock_client = MockClient.return_value
        mock_message = MagicMock()
        mock_client.messages.create.return_value = mock_message
        mock_message.sid = '12345'

        sid = send_sms(mock_client, 'from', 'to')

        mock_client.messages.create.assert_called_once_with(
            body="Rosto detectado por mais de 30 segundos.",
            from_='from',
            to='to'
        )
        
        self.assertEqual(sid, '12345')

    def test_detect_faces(self):
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        test_img = np.zeros((100, 100), dtype=np.uint8)
        cv2.rectangle(test_img, (30, 30), (70, 70), (255, 255, 255), -1)

        faces = detect_faces(face_cascade, test_img)

        self.assertEqual(len(faces), 1)
        x, y, w, h = faces[0]
        self.assertEqual((x, y, w, h), (30, 30, 40, 40))

if __name__ == '__main__':
    unittest.main()
