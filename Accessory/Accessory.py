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
        self._running = True
        self.water_pump = False

    def terminate(self):
        self._running = False

    def run(self, qCommand):
        """ run is the main thread of the Accessory object.
        It processes commands which control additional threads.

        For example, There is a water pump controlled by one of the relays.
        The water pump is going to cycle on/off repeatedly until the thread
        is terminated.  The thread can be restarted.

        @type: queue
        @param: qCommand
        """

        while self._running:
            if qCommand.empty():
                pass
            else:
                # Get the command.
                command = qCommand.get()
                print("Command: ", command)

                # Process the command.

            # Sleep for a bit.
            time.sleep(2)


if __name__ == "__main__":

    #Create Class
    accessory = Accessory()


    qCommand = queue.Queue(maxsize=0)

    #Create Thread
    accessoryThread = Thread(target=accessory.run, args=(qCommand,))

    #Start Thread
    accessoryThread.start()

    do_continue = True

    while do_continue:
        command = input("Command: ")

        if command == 'h' or command == 'q':
            do_continue = False
        else:
            # Put the command in the queue.
            qCommand.put(command)

    accessory.terminate()
    print ("Thread finished")

