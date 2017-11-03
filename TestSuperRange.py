from SuperRangeClass import SuperRange

def testSuperRange():
    sr = SuperRange()
    #print sr.Ranges
    a = ["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx"]
    try:
        testrange = [3, (0,2), (4,7)]
        print 'testrange: ' + str(testrange)
        sr.Ranges = testrange
        print sr.SliceList(a)
        assert(sr.SliceList(a) == ['jkl', 'abc', 'def', 'mno', 'pqr', 'stu'])

    except ValueError as e:
        print str(e)  #"problem with Ranges"

    try:
        testrange = [3, (0,2), [4,7]]   #we should accept both tuple and list items
        print 'testrange: ' + str(testrange)
        sr.Ranges = testrange
        print sr.SliceList(a)
        assert(sr.SliceList(a) == ['jkl', 'abc', 'def', 'mno', 'pqr', 'stu'])

    except ValueError as e:
        print str(e)  #"problem with Ranges"

    try:
        testrange = ['3', (0,2), (4,7)]      #non-integer item in list
        print 'testrange: ' + str(testrange)
        sr.Ranges = testrange
        print sr.Ranges
        print sr.SliceList(a)

    except ValueError as e:
        print str(e)

    try:
        testrange = [3, (0,2), (4,7,1)]     #tuple with length <> 2
        print 'testrange: ' + str(testrange)
        sr.Ranges = testrange
        print sr.SliceList(a)

    except ValueError as e:
        print str(e)

    try:
        sr.ImportPascalRanges('1..23,30,40..43')   #valid pattern
        print sr.Ranges
        assert(sr.Ranges == [(0, 22), 29,(39,42)])

    except ValueError as e:
        print str(e)

    try:
        sr.ImportPascalRanges('1..23..42,81')   #wrong number of arguments for range
        print sr.Ranges
    except ValueError as e:
        print str(e)

    try:
        sr.ImportPascalRanges('1..23,8P')   #non-numeric value in list
        print sr.Ranges
    except ValueError as e:
        print str(e)

    try:
        sr.ImportPascalRanges('1..2E,81')   #non-numeric value in list
        print sr.Ranges
    except ValueError as e:
        print str(e)

    try:
        sr.ImportPascalRanges('1.23,81')   #mal-formed Pascal range
        print sr.Ranges
    except ValueError as e:
        print str(e)

    try:
        sr.ImportHdrNameRanges('hdrD,hdrA..hdrC,hdrF..hdrK', 'hdrA,hdrB,hdrC,hdrD,hdrE,hdrF,hdrG,hdrH,hdrI,hdrJ,hdrK')
        print 'ImportHdrNameRanges: ' + str(sr.Ranges)
    except ValueError as e:
        print str(e)

if __name__ == '__main__':
    testSuperRange()
