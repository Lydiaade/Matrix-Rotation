import unittest

from main import rotate_clockwise

class BasicTests(unittest.TestCase):
    def basic_tests(self):
        basic_tests = [
        # Insert your own tests here with the following format:
        # ("input", "solution")
        ([], []),
        (["abc"], ["a", "b", "c"]),
        (["cba"], ["c","b","a"]),
        (["c","b","a"], ["abc"]),
        (
            [   "abc",
                "def"
            ],
            [   "da",
                "eb",
                "fc"
            ]
        ),
        ([""], []),
        (["", "", ""], []),
        (
            [   "###.....",
                "..###...",
                "....###.",
                ".....###",
                ".....###",
                "....###.",
                "..###...",
                "###.....",
            ],
            [   "#......#",
                "#......#",
                "##....##",
                ".#....#.",
                ".##..##.",
                "..####..",
                "..####..",
                "...##...",
            ]
        )
    ]
    from copy import deepcopy
    for matrix, expected in basic_tests:
        m2 = deepcopy(matrix)
        self.assertEqual(rotate_clockwise(matrix), expected)
        self.assertEqual(matrix, m2, "You modified the input! (matrix should stay the same after calling rotate_clockwise)")

if __name__ == '__main__':
    unittest.main()