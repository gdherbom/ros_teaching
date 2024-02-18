import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Float32
import random


class SpeedController(Node):

    def __init__(self):
        super().__init__('speed_controller')
        self.last_value_ = 0
        self.subscription = self.create_subscription(
            Float32,
            '/input_cmd',
            self.cmd_callback,
            10)
        self.publisher_ = self.create_publisher(Float32, '/speed', 10)

    def cmd_callback(self, msg):
        # Suppose the received message contains the desired speed
        # Here you would process the message to determine the speed
        # system is modelized by y(t+1) = y(t) + x + 1 

        speed_msg = Float32()
        speed_msg.data = self.last_value_ + msg.data + random.uniform(-10, 10)
        self.last_value_ = speed_msg.data

        # node.get_logger().info(f'speed_msg= {speed_msg}')

        self.get_logger().info(f'speed_msg = {speed_msg}')

        self.publisher_.publish(speed_msg)

def main(args=None):
    rclpy.init(args=args)
    speed_controller = SpeedController()
    rclpy.spin(speed_controller)
    speed_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
