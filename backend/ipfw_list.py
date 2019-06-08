import json
import subprocess

class ipfw_list:
  def __init__(self):
    self.cmd =  "/sbin/ipfw"
  def all(self) -> list:
    ALL: str = "-a list"
    p = subprocess.Popen(self.cmd + " " + ALL, shell=True, stdout=subprocess.PIPE)
    output, error =p.communicate()
    lists = []
    for line in output.splitlines():
      lists.append(line.decode("UTF-8"))
    return lists
