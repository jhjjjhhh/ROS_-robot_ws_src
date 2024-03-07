import rclpy,serial
from rclpy.node import Node

from std_msgs.msg import String 

sp  = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
class Sub_Led_Msg(Node):

    def __init__(self):
        super().__init__('sub_led_msg')
        sub = self.create_subscription(String, 'led_ctrl', self.get_led_msg,10)

    def get_led_msg(self, msg):
        if msg.data == "LED ON!!!":
            #send serial 1
            print("Send STM32 -> 1")
            sp.write(b'1')
        elif msg.data == "LED OFF!!!":
            #send serial 1
            print("Send STM32 -> 0")
            sp.write(b'0')
        else:
            print("Other Key Press!!!")
            pass


def main(args=None):
    rclpy.init(args=args)

    node = Sub_Led_Msg()

    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
