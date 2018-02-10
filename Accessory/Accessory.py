#/usr/bin/python

import sys
sys.path.append("/home/pi/pythondev/RelayPiPy/RelayPiPy")


import time
from threading   import Thread
from collections import deque
import queue
import pdb



class Accessory():
  """Accessory documentation"""

  def __init__(self):
    super( Accessory, self ).__init__()
#    print ("Accessory constructor")
    self._running = True

  def terminate(self):
    self._running = False

  def run(self, _qDistance):

    while self._running:
      pass


if __name__ == "__main__":

    #Create Class
    accessory = Accessory()


    qDistance = queue.Queue(maxsize=0)

    #Create Thread
    accessoryThread = Thread(target=accessory.run, args=(qDistance,))

    #Start Thread
    accessoryThread.start()

    while True:
      distance = qDistance.get()
      print ("Distance: ", distance)

    accessory.terminate()
    print ("Thread finished")

