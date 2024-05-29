import unittest
from unittest.mock import patch
from cadastro_facial import facial_recognition

class TestFacialRecognition(unittest.TestCase):

    @patch('my_module.take_picture')
    @patch('my_module.fr.load_image_file')
    @patch('my_module.fr.face_encodings')
    def test_facial_recognition(self, mock_face_encodings, mock_load_image_file, mock_take_picture):
        # Arrange
        mock_take_picture.return_value = None
        mock_load_image_file.return_value = None
        mock_face_encodings.return_value = []

        # Act
        result, faces = facial_recognition()

        # Assert
        self.assertFalse(result)
        self.assertEqual(faces, [])

if __name__ == '__main__':
    unittest.main()
