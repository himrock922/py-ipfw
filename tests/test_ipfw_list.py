import unittest
import sys
import pathlib
import subprocess
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append( str(current_dir) + '/../libipfw/' )
import ipfw_list

class TestIPFWList(unittest.TestCase):

    def test_ipfw_list(self):
        CMD: str = "/sbin/ipfw list"
        p = subprocess.Popen(CMD, shell=True, stdout=subprocess.PIPE)
        output, error = p.communicate()
        lists = []
        lists = [line.decode("UTF-8") for line in output.splitlines()]
        test_results = ipfw_list.IPFW_List()
        self.assertEqual(lists, test_results.results())


if __name__ == "__main__":
    unittest.main()