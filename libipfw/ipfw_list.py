"""exec command with ipfw list."""
import ipfw_cmd
import subprocess


class IPFW_List:

    def __init__(self):
        self.LIST_CMD: str = "list"

    def all_results(self) -> list:
        all_option: str = "-a"
        p = subprocess.Popen(ipfw_cmd.IPFW_CMD + " " + all_option +
                             " " + self.LIST_CMD,
                             shell=True, stdout=subprocess.PIPE)
        output, error = p.communicate()
        return [line.decode("UTF-8") for line in output.splitlines()]

    def results(self) -> list:
        p = subprocess.Popen(ipfw_cmd.IPFW_CMD + " " + self.LIST_CMD,
                             shell=True, stdout=subprocess.PIPE)
        output, error = p.communicate()
        return [line.decode("UTF-8") for line in output.splitlines()]
