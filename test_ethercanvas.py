# test_ethercanvas.py
"""
Tests for EtherCanvas module.
"""

import unittest
from ethercanvas import EtherCanvas

class TestEtherCanvas(unittest.TestCase):
    """Test cases for EtherCanvas class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EtherCanvas()
        self.assertIsInstance(instance, EtherCanvas)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EtherCanvas()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
