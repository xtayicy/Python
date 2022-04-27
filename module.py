# -*- coding: utf-8 -*-

import sys

def test():
    args = sys.argv
    print(args)

test()

from datetime import datetime
print(datetime.now())
print(datetime(2015, 4, 19, 12, 20))
