"""Implements the GildedRose requirements. @see requirements.md."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Item:
    """Holds data for an item."""

    name: str
    sell_in: int
    quality: int

    def __repr__(self):
        """Make a custom string representation."""
        return f"{self.name}, {self.sell_in}, {self.quality}"


class ItemUpdater(ABC):
    """Item updater base class."""

    def __init__(self, item: Item) -> None:
        """I have no idea why anyone would document the __init__ method.

        Args:
            item (Item): _description_
        """
        self.item = item

    @abstractmethod
    def update_quality(self):
        """Updates the Item quality."""

    def increase_quality(self, amount: int = 1):
        """Req 007."""
        self.item.quality = min(self.item.quality + amount, 50)

    def decrease_quality(self, amount: int = 1):
        """Req 005."""
        self.item.quality = max(self.item.quality - amount, 0)

    def decrease_sell_in(self):
        """Decrease sell in."""
        if self.item.quality > -1:
            self.item.sell_in -= 1

    def is_expired(self) -> bool:
        return self.item.sell_in < 0


class TrivialItemUpdater(ItemUpdater):
    """Updater for trivial items."""

    def update_quality(self):
        self.decrease_sell_in()
        self.decrease_quality(2 if self.is_expired() else 1)


class OldCheeseItemUpdater(ItemUpdater):
    """Updater for old cheese."""

    def update_quality(self):
        self.decrease_sell_in()
        self.increase_quality(2 if self.is_expired() else 1)


class TicketItemUpdater(ItemUpdater):
    """Updater for tickets."""

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
    """Updater for legendary items."""

    def update_quality(self):
        pass


class GildedRose:
    """Implements the GildedRose requirements. @see requirements.md."""

    item_updaters_mapping: Dict[str, ItemUpdater] = {
        "Sulfuras, Hand of Ragnaros": LegendaryItemUpdater,
        "Backstage passes to a TAFKAL80ETC concert": TicketItemUpdater,
        "Aged Brie": OldCheeseItemUpdater
    }

    def __init__(self, items: List[Item]):
        """I have no idea why anyone will document the __init__ method.

        Args:
            items (_type_): _description_
        """
        self.items = items

    def update_quality(self):
        """Called once at the end of each day."""
        for item in self.items:
            if self.item_updaters_mapping.get(item.name, None) is not None:
                self.item_updaters_mapping.get(item.name)(item).update_quality()
            else:  # all other items are trivial
                TrivialItemUpdater(item).update_quality()


def main():
    """Why would anyone document the main method."""
    my_gilde = GildedRose([])
    while True:
        my_gilde.update_quality()


if __name__ == "main":
    main()
