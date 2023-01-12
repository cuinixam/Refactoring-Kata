"""Implements the GildedRose requirements. @see requirements.md."""


class GildedRose:

    """Implements the GildedRose requirements. @see requirements.md."""

    def __init__(self, items):
        self.items = items

    def update_quality(self):
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


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


def main():
    my_gilde = GildedRose([])
    while(1):
        my_gilde.update_quality()

if __name__ == "main":
    main()