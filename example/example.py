import pylang
smpl = pylang.Language('file.smpl')
import time
@smpl.add_func
def log(input):
  print(input[0])
smpl.add_func(log)
@smpl.add_func
def gettime():
  print(time.time())

smpl.run()
