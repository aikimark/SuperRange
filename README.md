# SuperRange
Python list slicer class

You can define slices of a list by three different methods.
* set the Ranges property = list of integers or tuple/list items (of length 2) which are assumed to be list index values
* Use the ImportPascalRanges method to define the slices from a string representing a Pascal range. The string is a comma-delimited list of integers and '..' delimited pairs of integers.  These are assumed to be a one-based numbering system for items.  This method creates a zero-based list.
* use the ImportHdrRanges method to use a character-based reference, similar to the Pascal ranges.  An additional parameter to this method to specify the range, based on a header list, such as the first row of a CSV file.
