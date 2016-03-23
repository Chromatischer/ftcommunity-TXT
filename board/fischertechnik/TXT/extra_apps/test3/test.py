#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
from TxtStyle import *

class FtcGuiApplication(TxtApplication):
    def __init__(self, args):
        TxtApplication.__init__(self, args)

        # create the empty main window
        w = TxtWindow("Test 3")
        w.show()
        self.exec_()        
 
if __name__ == "__main__":
    FtcGuiApplication(sys.argv)
