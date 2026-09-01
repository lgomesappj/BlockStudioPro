# test_blockstudiopro.py
"""
Tests for BlockStudioPro module.
"""

import unittest
from blockstudiopro import BlockStudioPro

class TestBlockStudioPro(unittest.TestCase):
    """Test cases for BlockStudioPro class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockStudioPro()
        self.assertIsInstance(instance, BlockStudioPro)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockStudioPro()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
