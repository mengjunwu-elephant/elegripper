from elegripper import Gripper
import time
if __name__=="__main__":
    g=Gripper("COM8")##Enter the actual serial port number
    g.set_gripper_value(100,100)
    time.sleep(2)
    g.set_gripper_value(0,100)
    time.sleep(2)
    print(g.get_gripper_value())

