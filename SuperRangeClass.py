#-------------------------------------------------------------------------------
# Name:        SuperRange
# Purpose:     A multi-range slicer for lists and tuples.
#
# Author:      Mark Hutchinson
#
# Created:     11/1/2017
# Copyright:   (c) Mark Hutchinson 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class SuperRange(object):
    def __init__(self):
        self._Ranges = []
        #print "__init__"

    def SliceList(self, RangeList):
        #print("Getting SliceList")
        SL = []
        for x in self._Ranges:
            if type(x) is int:
                SL.append(RangeList[x])
            elif type(x) in [tuple, list]:
                SL.extend(RangeList[x[0]:x[1]])
        return SL

    def getRange(self):
        #print("Getting property value")
        return self._Ranges

    def setRange(self, value):
        #print("Setting property value")
        #validate the parameter
        for x in value:
            if type(x) is int:
                pass
            elif type(x) in [tuple, list]:
                if len(x) == 2 and all(type(y) is int for y in x):
                    pass
                else:
                    raise ValueError("tuple/list items must be len=2 and type=int")
            else:
                raise ValueError("Range items must be int or tuple or list")

        #print("Setting value")
        self._Ranges = value

    Ranges = property(getRange, setRange, None, "I'm the 'Ranges' property.")

    def ImportPascalRanges(self, value):
        if type(value) is str:
            o = []
            rs = value.split(',')
            for r in rs:
                s = r.split('..')
                if len(s) == 1:
                    intVal = int(s[0])-1
                    o.append(intVal)
                elif len(s) == 2:
                    intLowVal = int(s[0])
                    intHighVal = int(s[1])
                    o.append((intLowVal-1, intHighVal-1))
                else:
                    raise ValueError("Wrong number of values in range: " + str(s))

            self.setRange(o)

        else:
            raise ValueError("Parameter must be type string")

    def ImportHdrNameRanges(self, value, headers):
        if type(headers) is str:
            hdr = str(headers).split(",")
        elif type(headers) in (list, tuple):
            hdr = headers
        else:
            raise ValueError("Parameter must be type string, tuple, or list")

        if type(value) is str:
            o = []
            rs = value.split(',')
            for r in rs:
                s = r.split('..')
                if len(s) == 1:
                    intVal = hdr.index(s[0])
                    o.append(intVal)
                elif len(s) == 2:
                    intLowVal = hdr.index(s[0])
                    intHighVal = hdr.index(s[1])
                    o.append((intLowVal, intHighVal))
                else:
                    raise ValueError("Wrong number of values in range: " + str(s))

            self.setRange(o)

        else:
            raise ValueError("Parameter value must be type string")
