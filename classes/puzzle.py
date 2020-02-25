import json

class Puzzle:
    # def __init__(self,rows,columns):
    #     self.rows = rows
    #     self.columns = columns
    #     self.rowcount = len(rows)
    #     self.colcount = len(columns)

    def __init__(self,jsonfile):
        #TODO: check if file exists
        with open(jsonfile,'r') as inputfile:
            jsonraw=inputfile.read()
        jsonobj = json.loads(jsonraw)
        self.rows = jsonobj['rows']
        self.columns = jsonobj['cols']
        self.rowcount = len(self.rows)
        self.colcount = len(self.columns)
        singlerow = [0]*self.colcount
        self.puzzleactual = [singlerow]*self.rowcount
        if 'solution' in jsonraw:
            self.solution = jsonobj['solution']
        else:
            self.solution = None

    def printPuzzle(self):
        for row in self.puzzleactual:
            for col in row:
                print(col,end = '')
            print()
    
    def printSolution(self):
        if self.solution != None:
            for row in self.solution:
                newrow = row.replace('0',' ').replace('1','#')
                print(newrow)
        else:
            print("No Solution")


    