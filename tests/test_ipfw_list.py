import unittest
import os, sys
import subprocess
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from libipfw import command_exec

class TestIPFWList(unittest.TestCase):

    def test_ipfw_list(self):
        CMD: str = "/sbin/ipfw list"
        p = subprocess.Popen(CMD, shell=True, stdout=subprocess.PIPE)
        output, error = p.communicate()
        lists = [line.decode("UTF-8") for line in output.splitlines()]
        test_results = command_exec.IPFW()
        self.assertEqual(lists, test_results.results())


if __name__ == "__main__":
    unittest.main()