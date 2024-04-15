import unittest
from unittest.mock import patch
import io
import time
import sys
import select
from timer import main

class TestTimer(unittest.TestCase):
    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('select.select', return_value=([sys.stdin], [], []))
    def test_timer(self, mock_select, mock_stdout, mock_input):
        with patch('time.time', side_effect=[0, 5]):
            main()
        self.assertEqual(mock_stdout.getvalue(), '\rElapsed Time: 00:00:05\nElapsed Time: 00 hours 00 minutes 05 seconds\n')
        
if __name__ == "__main__":
    unittest.main()