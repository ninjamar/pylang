class Language:
  def __init__(self,fname):
    self.func_map = {}
    self.fname = fname
  def add_func(self,func):
    def inner():
      pass
    self.func_map[str(func.__name__)] = {"name":func.__name__,"call":func,"args_num":func.__code__.co_argcount,"args_names":func.__code__.co_varnames}
    return inner

  def run(self):
    with open(self.fname) as f:
      contents = f.readlines()
    for line in contents:
      func = self.func_map[line.split()[0]]
      params = [i for i in line.split()][1:]
      if func['args_num']>0:
        func['call'](params)
      else:
        func['call']()
