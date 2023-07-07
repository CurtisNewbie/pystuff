import unittest
import pystuff


class Tester(unittest.TestCase):

    def test_rev_idx(self):
        idx = pystuff.rev_idx(["one", "two", "three", "four"], set(["three", "four"]))
        print(idx)
        self.assertEqual(len(idx.keys()), 2)

        idx = pystuff.rev_idx(["one", "two", "three", "four"])
        print(idx)
        self.assertEqual(len(idx.keys()), 4)


    def test_completer(self):
        pystuff.setup_completer()
        cand = pystuff.completer_candidates

        self.assertEqual(len(cand), 0)
        pystuff.feed_completer('yo')
        self.assertEqual(len(cand), 1)
        print(cand)



if __name__ == "__main__":
    unittest.main()
