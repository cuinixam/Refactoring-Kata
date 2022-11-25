# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_item_trivial(self):
        """Tested: Req-001, Req-003"""
        items = [Item("trivial", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("trivial", items[0].name)
        self.assertEquals(-1, items[0].sell_in)
        
    def test_item_trivial_expired(self):
        """Tested: Req-002,Req-003,Req-004"""
        items = [Item("trivial", 1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(9, items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(7, items[0].quality)
    

        
if __name__ == '__main__':
    unittest.main()
