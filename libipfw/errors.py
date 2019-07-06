class Error(Exception):
    pass

class AddExecError(Error):
    def __init__(self, message):
      self.message = message
      print(self.message)