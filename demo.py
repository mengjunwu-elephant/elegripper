from elegripper import Gripper
import time
if __name__=="__main__":
    g=Gripper("COM8",115200,1)##填写实际的串口号和波特率和夹爪ID
    print("夹爪的实际ID为:",g.get_gripper_Id())
    g.set_gripper_value(100,100)
    time.sleep(2)
    g.set_gripper_value(0,100)
    time.sleep(2)
    

