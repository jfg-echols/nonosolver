class Row:
    # numbers is a list of ints
    # rowvalues is the ow as displayed (0=null,1=empty,2=full)
    def __init__ (self,numbers,rowValues):
        if not all(isinstance(x,int) for x in numbers):
            raise ValueError('should be array of ints')
        intRowValue = list(rowValues)
        try:
            for i in range(0,len(intRowValue)):
                intRowValue[i] = int(intRowValue[i])
                if intRowValue[i] not in range(0,3):
                    raise ValueError("rowValues should be 0,1, or 2 as ints")
        except ValueError:
            raise ValueError('rowValues should be 0,1, or 2 as ints')
        self.numbers = numbers
        # string row values input converted to list[int]
        # (intRowValue)
        self.rowContent = intRowValue

    # need to split this into available slots and create an array based on ints
    # 10001 needs to be 3
    # 00001 needs to be 4
    # 10100 needs to be 1,2
    def getRowContent (self):
        currentRowNumbers = []
        rowItemCount = 0
        # for each item in row... if 0 or 2 count goes up, if 1, count resets to 0 and is added to currentRowNumbers
        for i in range(0,len(self.rowContent)):
            if self.rowContent[i] == 0 or self.rowContent[i] ==2:
                rowItemCount += 1
            elif self.rowContent[i] == 1:
                currentRowNumbers.append(rowItemCount)
                rowItemCount = 0
        return currentRowNumbers
    # if row is full with no numbers
    def isfull(self):
        numCount = len(self.numbers)
        if numCount == 1:
            if self.numbers[0] == len(self.rowContent):
                for i in range(0,len(self.rowContent)):
                    self.rowContent[i] = 2
