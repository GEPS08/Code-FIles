from pynput.mouse import Button, Controller
import time
mouse = Controller()

time.sleep(10)

print('The current pointer position is {0}'.format(
    mouse.position))

mouse.position = (0, 0)
