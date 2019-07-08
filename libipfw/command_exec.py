"""exec command with ipfw list."""
from libipfw import cmd, errors
import shlex
import subprocess


class IPFW:

    def __init__(self):
        self.LIST_CMD: str = "list"
        self.ADD_CMD: str = "add"

    def all_results(self) -> list:
        all_option: str = "-a"
        command: str = cmd.IPFW_CMD + " " + all_option + " " + self.LIST_CMD
        p = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = p.communicate()
        return [line.decode("UTF-8") for line in output.splitlines()]

    def results(self) -> list:
        command: str = cmd.IPFW_CMD + " " + self.LIST_CMD
        p = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = p.communicate()
        return [line.decode("UTF-8") for line in output.splitlines()]

    def add(self, parameter: str) -> None:
        command: str = cmd.IPFW_CMD + " " + self.ADD_CMD + " " + parameter
        p = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = p.communicate()
        if error.decode("UTF-8"):
            raise errors.AddExecError(message=error.decode("UTF-8"))
