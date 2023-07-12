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


    def test_dict_get(self):
        d = {
            "name": {
                "first" : "yongjie",
                "last" : "zhuang"
            }
        }
        got = pystuff.dict_get(d, "name.last")
        self.assertEqual(got, "zhuang")

        d = {
            "name": {
                "first" : "yongjie",
                "last" : "zhuang"
            }
        }
        got = pystuff.dict_get(d, "age", "unknown")
        self.assertEqual(got, "unknown")

        d = {
            "name": {
                "first" : "yongjie",
                "last" : "zhuang"
            }
        }
        got = pystuff.dict_get(d, "name.middle", "unknown")
        self.assertEqual(got, "unknown")

        d = None
        got = pystuff.dict_get(d, "name.middle", "unknown")
        self.assertEqual(got, "unknown")

        d = None
        got = pystuff.dict_get(d, "")
        self.assertEqual(got, None)


    def test_dwalker(self):
        d = {
            "name": {
                "first" : "yongjie",
                "last" : "zhuang"
            }
        }
        walker = pystuff.DickWalker(d)
        got = walker.get("name.last")
        self.assertEqual(got, "zhuang")

        d = {
            "name": {
                "first" : "yongjie",
                "last" : "zhuang"
            }
        }
        walker = pystuff.DickWalker(d)
        got = walker.get("age", "unknown")
        self.assertEqual(got, "unknown")

        d = {
            "name": {
                "first" : "yongjie",
                "last" : "zhuang"
            }
        }
        walker = pystuff.DickWalker(d)
        got = walker.get("name.middle", "unknown")
        self.assertEqual(got, "unknown")

        d = None
        walker = pystuff.DickWalker(d)
        got = walker.get("name.middle", "unknown")
        self.assertEqual(got, "unknown")

        d = None
        walker = pystuff.DickWalker(d)
        got = walker.get("")
        self.assertEqual(got, None)


if __name__ == "__main__":
    unittest.main()
