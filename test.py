import unittest
import pystuff

class Tester(unittest.TestCase):

    def test_rev_idx(self):
        idx = pystuff.rev_idx(["one", "two", "three", "four"], set(["three", "four"]))
        print(idx)
        assert len(idx.keys()) == 2

        idx = pystuff.rev_idx(["one", "two", "three", "four"])
        print(idx)
        assert len(idx.keys()) == 4


if __name__ == "__main__":
  unittest.main()
