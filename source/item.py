# Item class
#
# Base class for an object with a kind
#
# 2014/6/12
# written by Michael Shawn Redmond

class Item:
    def __init__(self, kind):
        self.kind = kind

    def get_kind(self):
        return self.kind
