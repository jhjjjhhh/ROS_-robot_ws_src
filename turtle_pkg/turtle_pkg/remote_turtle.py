import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from .getchar import Getchar

msg = '''

Remote Control Turtle
'w' for forward
's' for backward
'd' for Right Turn
'a' for Left Turn
' ' for STOP
'z' for END PRG
'1' for circle
'2' for R_circle
'''

class Remote_Turtle(Node):

    def __init__(self):
        super().__init__('remote_turtle')
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel',10)

def main(args=None):
    rclpy.init(args=args)
    
    node = Remote_Turtle()
    kb = Getchar()
    tw = Twist()
    try:
        print("Start Remote_Turtle Prg")
        while rclpy.ok():
            key = kb.getch()
            if key == 'w':
                print("Foward")
                tw.linear.x = tw.angular.z = 0.0
                tw.linear.x = 2.0
            elif key == 's':
                print("Backward")
                tw.linear.x = tw.angular.z = 0.0
                tw.linear.x = -2.0
            elif key == 'd':
                print("Right Turn")
                tw.linear.x = tw.angular.z = 0.0
                tw.angular.z = -2.0
            elif key == 'a':
                print("Left Turn")
                tw.linear.x = tw.angular.z = 0.0
                tw.angular.z = 2.0
            elif key == ' ':
                print("STOP!")
                tw.linear.x = tw.angular.z = 0.0
            elif key == 'z':
                print("END Prg")
                break
            elif key == '1':
                tw.linear.x = tw.angular.z = 0.0
                tw.angular.z = 2.0
                tw.linear.x = 2.0                
            elif key == '2':
                tw.linear.x = tw.angular.z = 0.0
                tw.angular.z = -2.0
                tw.linear.x = 2.0                  
            elif key == '`':
                print(msg)
            else:
                pass
            node.pub.publish(tw)
    except KeyboardInterrupt:
        node.destroy_node()
        
if __name__ == '__main__':
    main()

