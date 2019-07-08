import unittest
import os, sys
import subprocess
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from libipfw import command_exec

class TestIPFW(unittest.TestCase):

    def test_ipfw_list(self) -> None:
        CMD: str = "/sbin/ipfw list"
        p = subprocess.Popen(CMD, shell=True, stdout=subprocess.PIPE)
        output, error = p.communicate()
        lists = [line.decode("UTF-8") for line in output.splitlines()]
        test_results = command_exec.IPFW()
        self.assertEqual(lists, test_results.results())
    
    def test_ipfw_add(self) -> None:
        ipfw = command_exec.IPFW()
        ipfw.add("60000 allow ip from any to any")
        CMD: str = "/sbin/ipfw list"
        p = subprocess.Popen(CMD, shell=True, stdout=subprocess.PIPE)
        output, error = p.communicate()
        allow_result = False
        for line in output.splitlines():
          if line.decode("UTF-8") in "60000 allow ip from any to any":
            allow_result = True 
        self.assertTrue(allow_result)

    def test_ipfw_delete(self) -> None:
        ipfw = command_exec.IPFW()
        ipfw.add("60000 allow ip from any to any")
        ipfw.delete("60000 allow ip from any to any")
        CMD: str = "/sbin/ipfw list"
        p = subprocess.Popen(CMD, shell=True, stdout=subprocess.PIPE)
        output, error = p.communicate()
        delete_result = False
        for line in output.splitlines():
          if line.decode("UTF-8") not in "60000 allow ip from any to any":
            delete_result = True
        self.assertTrue(delete_result)

if __name__ == "__main__":
    unittest.main()