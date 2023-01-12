"""Implements the GildedRose requirements. @see requirements.md."""

from abc import ABC, abstractmethod
from typing import Dict


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class ItemUpdater(ABC):
    
    def __init__(self, item: Item) -> None:
        self.item = item
    
    @abstractmethod
    def update_quality(self, item: Item):
        """Updates the Item quality"""
        
    def increase_quality(self, amount: int = 1):
        self.item.quality += amount
        if self.item.quality > 50:
            self.item.quality = 50
            
    def decrease_quality(self, amount: int = 1):
        self.item.quality -= amount
        if self.item.quality < 0:
            self.item.quality = 0
        
    def decrease_sell_in(self):
        if self.item.quality > -1:
            self.item.sell_in -= 1
        
    def is_expired(self) -> bool:
        return self.item.sell_in < 0
        

class TrivialItemUpdater(ItemUpdater):
    def update_quality(self):
        self.decrease_sell_in()
        self.decrease_quality(2 if self.is_expired() else 1)


class OldCheeseItemUpdater(ItemUpdater):
    def update_quality(self):
        self.decrease_sell_in()
        self.increase_quality(2 if self.is_expired() else 1)


class TicketItemUpdater(ItemUpdater):
    def update_quality(self):
        self.decrease_sell_in()
        if self.is_expired():
            self.item.quality = 0
        else:
            self.increase_quality()
            if self.item.sell_in < 11:
                self.increase_quality()
            if self.item.sell_in < 6:
                self.increase_quality()

class LegendaryItemUpdater(ItemUpdater):
    def update_quality(self):
        pass


class GildedRose:
    """Implements the GildedRose requirements. @see requirements.md."""
    
    item_updaters_mapping: Dict[str, ItemUpdater] = {
        "Sulfuras, Hand of Ragnaros": LegendaryItemUpdater,
        "Backstage passes to a TAFKAL80ETC concert": TicketItemUpdater,
        "Aged Brie": OldCheeseItemUpdater
    }

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        """called once at the end of each day"""
        for item in self.items:
            if self.item_updaters_mapping.get(item.name, None) is not None:
                self.item_updaters_mapping.get(item.name)(item).update_quality()
            else: # all other items are trivial
                TrivialItemUpdater(item).update_quality()


def main():
    my_gilde = GildedRose([])
    while(1):
        my_gilde.update_quality()


if __name__ == "main":
    main()
