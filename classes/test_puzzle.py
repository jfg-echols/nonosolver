import unittest
from puzzle import Puzzle

class TestPuzzle(unittest.TestCase):
    # TODO - put this in a mock statement
    def test_init_actual(self):
        testpuzzle = Puzzle('C:\\Users\\Jono-work\\Git\\personal\\nonosolver\\puzzles\\upright.json')
        self.assertEqual(testpuzzle.puzzleactual,[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
    def test_init_rows(self):
        testpuzzle = Puzzle('C:\\Users\\Jono-work\\Git\\personal\\nonosolver\\puzzles\\upright.json')
        self.assertEqual(testpuzzle.rows,[[3],[2],[1,1],[1,1]])
    def test_init_cols(self):
        testpuzzle = Puzzle('C:\\Users\\Jono-work\\Git\\personal\\nonosolver\\puzzles\\upright.json')
        self.assertEqual(testpuzzle.columns,[[1],[1,1],[2],[4]])
    def test_printPuzzle(self):
        testpuzzle = Puzzle('C:\\Users\\Jono-work\\Git\\personal\\nonosolver\\puzzles\\upright.json')
        testpuzzle.printPuzzle()

if __name__ == '__main__':
    unittest.main()