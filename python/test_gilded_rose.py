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

        # Preconditions
        sell_in__before = 1
        quality__before = 10
        items = [Item("trivial", sell_in__before, quality__before)]
        gilded_rose = GildedRose(items)

        # Call item-under-test
        gilded_rose.update_quality()

        # Assert expectations
        self.assertEquals(sell_in__before - 1, items[0].sell_in)
        self.assertEquals(quality__before - 1, items[0].quality)

        # Call item-under-test
        gilded_rose.update_quality()

        # Assert expectations
        self.assertEquals(sell_in__before - 2, items[0].sell_in)
        self.assertEquals(quality__before - 3, items[0].quality)

    def test_item_neg_quality(self):
        """Tested: Req-005"""

        # Preconditions
        sell_in__before = 1
        quality__before = 0
        items = [Item("trivial", sell_in__before, quality__before)]

        # Call item-under-test
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        # Assert expectations
        self.assertEquals(quality__before, items[0].quality)

    def test_aged_brie(self):
        """Tested: Req-006"""

        # Preconditions
        sell_in__before = 1
        quality__before = 10
        items = [Item("Aged Brie", sell_in__before, quality__before)]
        gilded_rose = GildedRose(items)

        # call iut
        gilded_rose.update_quality()

        # Assertions
        self.assertEquals(sell_in__before - 1, items[0].sell_in)
        self.assertEquals(quality__before + 1, items[0].quality)

        # call iut
        gilded_rose.update_quality()

        # Assertions
        self.assertEquals(sell_in__before - 2, items[0].sell_in)
        self.assertEquals(quality__before + 3, items[0].quality)

    def test_item_max_quality(self):
        """Tested: Req-007"""

        # Preconditions
        sell_in__before = 1
        quality__before = 49
        items = [Item("Aged Brie", sell_in__before, quality__before)]
        gilded_rose = GildedRose(items)

        # Call item-under-test
        gilded_rose.update_quality()

        # Assert expectations
        self.assertEquals(quality__before + 1, items[0].quality)

        # Call item-under-test
        gilded_rose.update_quality()

        # Assert expectations
        self.assertEquals(quality__before + 1, items[0].quality)

    def test_xx(self):
        """Tested: Req-008"""

        # Preconditions
        name = "Sulfuras, Hand of Ragnaros"
        sell_in__before = 1
        quality__before = 1

        items = [Item(name, sell_in__before, quality__before)]
        gilded_rose = GildedRose(items)

        # Call item-under-test
        gilded_rose.update_quality()

        # Assert expectations
        self.assertEquals(quality__before, items[0].quality)
        self.assertEquals(sell_in__before, items[0].sell_in)

    def test_backstagePass(self):
        """Tested: Req-009"""

        # Preconditions
        name = "Backstage passes to a TAFKAL80ETC concert"
        sell_in__before = 11
        quality__before = 1

        item = Item(name, sell_in__before, quality__before)
        gilded_rose = GildedRose([item])

        # Call item-under-test
        gilded_rose.update_quality()

        # Assert expectations
        self.assertEquals(quality__before + 1, item.quality)
        self.assertEquals(sell_in__before - 1, item.sell_in)

        # Call item-under-test
        gilded_rose.update_quality()

        # Assert expectations
        self.assertEquals(quality__before + 3, item.quality)
        self.assertEquals(sell_in__before - 2, item.sell_in)

        # Call item-under-test
        for _ in range(4):
            gilded_rose.update_quality()

        # Assert expectations
        self.assertEquals(12, item.quality)
        self.assertEquals(5, item.sell_in)

        # Call item-under-test
        gilded_rose.update_quality()

        # Assert expectations
        self.assertEquals(15, item.quality)
        self.assertEquals(4, item.sell_in)
    
    def test_backstagePass(self):
        """Tested: Req-010"""

        # Preconditions
        name = "Backstage passes to a TAFKAL80ETC concert"
        sell_in__before = 1
        quality__before = 20

        item = Item(name, sell_in__before, quality__before)
        gilded_rose = GildedRose([item])

        # Call item-under-test
        gilded_rose.update_quality()

        # Assert expectations
        self.assertEquals(quality__before + 3, item.quality)
        self.assertEquals(0, item.sell_in)
        
        # Call item-under-test
        gilded_rose.update_quality()

        # Assert expectations
        self.assertEquals(0, item.quality)
        self.assertEquals(-1, item.sell_in)


if __name__ == '__main__':
    unittest.main()
