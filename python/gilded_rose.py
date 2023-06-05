"""Implements the GildedRose requirements. @see requirements.md."""

"""

Data (what kind of data this class needs and/or processes):
* 

Behavior(Actions) - what does it do with the data:
* changes the quality
* changes the sell_in
* 

To be clarified:

* why should the GildedRose know that the sell_in should be updated before the quality?
* 

"""

from abc import ABC, abstractmethod
from enum import Enum, auto



class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class ItemUpdater(ABC):
    @abstractmethod
    def update(self, item):
        """Updates the item properties."""

class TrivialItemUpdater(ItemUpdater):
    def update(self, item):
        pass

class ItemUpdaterFinder:
    """What kind of item is it.
    Identifies the item, find the appropriate updater.
    """
    def find_updater(self, item) -> ItemUpdater:
        return TrivialItemUpdater()

class GildedRose:

    """Implements the GildedRose requirements. @see requirements.md.
    This is our business class.
    """

    def __init__(self, items):
        self.items = items
        self.finder = ItemUpdaterFinder()

    def update_quality(self):
        """This is the method called every day to make sure the items stay updated."""
        for item in self.items:            
            self.finder.find_updater(item).update(item)

    def _update_quality(self):
        """called once at the end of each day"""
        for item in self.items:
            if item.name != "Sulfuras, Hand of Ragnaros": # Req-008
                self.update_item_quality(item)
                self.update_item_sell_in(item)
                self.update_expired_item_quality(item)

    def update_expired_item_quality(self, item):
        if item.sell_in < 0:
            if item.name != "Aged Brie":
                if item.name != "Backstage passes to a TAFKAL80ETC concert":
                    if item.quality > 0:
                        item.quality = item.quality - 1
                else:
                    item.quality = item.quality - item.quality
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1

    def update_item_sell_in(self, item):
        item.sell_in = item.sell_in - 1

    def update_item_quality(self, item):
        if item.quality > 0 and item.quality < 50 : # Req-005 and Req-007
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                item.quality = item.quality - 1
            else:
                item.quality = item.quality + 1
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 11:
                        item.quality = item.quality + 1
                    if item.sell_in < 6:
                        item.quality = item.quality + 1
                        
    def dummy(self):
        print('test')


def main():
    my_gilde = GildedRose([])
    while(1):
        my_gilde.update_quality()

if __name__ == "main":
    main()