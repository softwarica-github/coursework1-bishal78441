import unittest
from unittest.mock import patch, Mock
from client import send_message

class TestClientFunctions(unittest.TestCase):

    @patch('client.messagebox.showerror')
    def test_send_empty_message(self, mock_showerror):
        # Test sending an empty message
        # Ensure that the showerror function is called
        with patch('client.client') as mock_client:
            mock_sendall = Mock()
            mock_client.return_value.sendall = mock_sendall
            send_message()
            mock_showerror.assert_called_with("Empty message", "Message cannot be empty")
            mock_sendall.assert_not_called()  # Ensure sendall is not called with an empty message

if __name__ == '__main__':
    unittest.main()
