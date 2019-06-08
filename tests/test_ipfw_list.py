import unittest
import sys
import pathlib
import subprocess
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append( str(current_dir) + '/../backend/' )
import ipfw_list

class TestIPFWList(unittest.TestCase):

    def test_ipfw_list(self):
        print(sys.path)
        CMD: str = "/sbin/ipfw -a list"
        p = subprocess.Popen(CMD, shell=True, stdout=subprocess.PIPE)
        output, error = p.communicate()
        lists = []
        for line in output.splitlines():
            lists.append(line.decode("UTF-8"))
        test_results = ipfw_list.IPFW_List()
        self.assertEqual(lists, test_results.all_results())


if __name__ == "__main__":
    unittest.main()