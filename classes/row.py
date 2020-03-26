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

# 0 == null
# 1 == empty
# 2 == filled
    def getRowContent (self):
        currentRowNumbers = []
        rowItemCount = 0
        # for each item in row... if 0 or 2 count goes up, if 1, count resets to 0 and is added to currentRowNumbers
        for i in range(0,len(self.rowContent)):
            if self.rowContent[i] == 0 or self.rowContent[i] == 2:
                rowItemCount += 1
            elif self.rowContent[i] == 1:
                if rowItemCount != 0:
                    currentRowNumbers.append(rowItemCount)
                rowItemCount = 0
        if rowItemCount > 0:
            currentRowNumbers.append(rowItemCount)
        if currentRowNumbers == []:
            currentRowNumbers = [0]
        return currentRowNumbers
    def isRowFull(self):
        if 0 not in self.rowContent:
            return True
        else:
            return False
    def countRowNumbers(self):
        count = 0
        for i in range(0,len(self.numbers)):
            count += self.numbers[i]
            if i != len(self.numbers)-1:
                count+=1
        return count
    def fillRowOnePass(self):
        numCount = len(self.numbers)
        if numCount == 1:
            if self.numbers[0] == len(self.rowContent):
                for i in range(0,len(self.rowContent)):
                    self.rowContent[i] = 2
            elif self.numbers[0] == 0:
                for i in range(0,len(self.rowContent)):
                    self.rowContent[i] = 1
        if self.countRowNumbers() == len(self.rowContent):
            contentstring = ""
            for i in range(0,len(self.numbers)):
                thisblock = "2"*self.numbers[i]
                contentstring += thisblock
                if i != len(self.numbers)-1:
                    contentstring += "1"
            self.rowContent = list(contentstring)
        
                

# this is something else
#         elif self.numbers == self.getRowContent():
#             for cell in self.rowContent:
#                 if cell == 0:
#                     cell = 2
