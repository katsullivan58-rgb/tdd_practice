import unittest
from read_toys import read
from item import Item

class TestReadToys(unittest.TestCase):
    def test_can_read_json(self):
        items = read('toyinventory.json')
        #make sure we got a list
        self.assertIsInstance(items, list)
        #make sure there’s at least one item
        self.assertGreater(len(items), 0)
        #make sure the first thing is an Item
        self.assertIsInstance(items[0], Item)

if __name__ == '__main__':
    unittest.main()
