import unittest
from unittest.mock import patch
from reconhecimento import identify_face

class TestIdentifyFace(unittest.TestCase):

    @patch('my_module.facial_recognition')
    def test_identify_face_no_faces(self, mock_facial_recognition):
        # Arrange
        mock_facial_recognition.return_value = (False, [])

        # Act
        result = identify_face()

        # Assert
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
