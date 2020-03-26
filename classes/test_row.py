import unittest
from row import Row

class TestRow(unittest.TestCase):
    # TODO - put this in a mock statement

    def test_init_row(self):
        testrow = Row([5],"11111")
        self.assertEqual(testrow.numbers,[5])
    def test_init_rowvalue(self):
        testrow = Row([5],"12201")
        self.assertEqual(testrow.rowContent,[1,2,2,0,1])
    def test_init_rowItemCounts0(self):
        testrow0 = Row([5],"00000")
        testresult0 = testrow0.getRowContent()
        self.assertEqual(testresult0,[5])
    def test_init_rowItemCounts1(self):
        testrow1 = Row([0],"11111")
        testresult1 = testrow1.getRowContent()
        self.assertEqual(testresult1,[0])
    def test_init_rowItemCounts2(self):
        testrow2 = Row([5],"22222")
        testresult2 = testrow2.getRowContent()
        self.assertEqual(testresult2,[5])
    def test_init_rowItemCounts3(self):
        testrow3 = Row([2,2],"00100")
        testresult3 = testrow3.getRowContent()
        self.assertEqual(testresult3,[2,2])
    def test_init_rowItemCounts4(self):
        testrow4 = Row([3],"10001")
        testresult4 = testrow4.getRowContent()
        self.assertEqual(testresult4,[3])
    def test_init_rowItemCounts5(self):
        testrow5 = Row([1,2],"21001")
        testresult5 = testrow5.getRowContent()
        self.assertEqual(testresult5,[1,2])
    def test_init_rowItemCounts6(self):
        testrow6 = Row([1,2],"21000")
        testresult6 = testrow6.getRowContent()
        self.assertEqual(testresult6,[1,3])
    def test_init_rowItemCounts7(self):
        testrow7 = Row([3,4],"1000100021")
        testresult7 = testrow7.getRowContent()
        self.assertEqual(testresult7,[3,4])
    def test_init_rowItemCounts8(self):
        testrow8 = Row([1,10,2,1,1],"21200000220011001210")
        testresult8 = testrow8.getRowContent()
        self.assertEqual(testresult8,[1,10,2,1,1])
    def test_init_isRowFull(self):
        testrow = Row([5],"0222220")
        self.assertEqual(testrow.isRowFull(),False)
    def test_init_isRowFull2(self):
        testrow2 = Row([5],"1222221")
        self.assertEqual(testrow2.isRowFull(),True)
    def test_init_countRowNumbers(self):
        testrow = Row([5],"00000")
        testnumber = testrow.countRowNumbers()
        self.assertEqual(testnumber,5)
    def test_init_countRowNumbers2(self):
        testrow2 = Row([5,4],"0000000000")
        testnumber2 = testrow2.countRowNumbers()
        self.assertEqual(testnumber2,10)
    def test_init_countRowNumbers3(self):
        testrow3 = Row([5,4,3,2,1],"0000000000000000000")
        testnumber3 = testrow3.countRowNumbers()
        self.assertEqual(testnumber3,19)
    def test_init_fillRowOnePassFull(self):
        testrow = Row([5],"00000")
        testrow.fillRowOnePass()
        self.assertEqual(testrow.rowContent,[2,2,2,2,2])
    def test_init_fillRowOnePassEmpty(self):
        testrow2 = Row([0],"00000")
        testrow2.fillRowOnePass()
        self.assertEqual(testrow2.rowContent,[1,1,1,1,1])
    def test_init_fillRowOnePassMiscSize(self):
        testrow3 = Row([1,6,1],"0000000000")
        testrow3.fillRowOnePass()
        self.assertEqual(testrow3.rowContent,[2,1,2,2,2,2,2,2,1,2])
    


if __name__ == '__main__':
    unittest.main()
