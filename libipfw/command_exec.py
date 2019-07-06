"""exec command with ipfw list."""
from libipfw import cmd, errors
import subprocess


class IPFW:

    def __init__(self):
        self.LIST_CMD: str = "list"
        self.ADD_CMD: str = "add"

    def all_results(self) -> list:
        all_option: str = "-a"
        p = subprocess.Popen(cmd.IPFW_CMD + " " + all_option +
                             " " + self.LIST_CMD,
                             shell=True, stdout=subprocess.PIPE)
        output, error = p.communicate()
        return [line.decode("UTF-8") for line in output.splitlines()]

    def results(self) -> list:
        p = subprocess.Popen(cmd.IPFW_CMD + " " + self.LIST_CMD,
                             shell=True, stdout=subprocess.PIPE)
        output, error = p.communicate()
        return [line.decode("UTF-8") for line in output.splitlines()]

    def add(self) -> None:
        p = subprocess.Popen(cmd.IPFW_CMD + " " + self.ADD_CMD,
                            shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = p.communicate()
        if error is not None:
            raise errors.AddExecError(message=error.decode("UTF-8"))
