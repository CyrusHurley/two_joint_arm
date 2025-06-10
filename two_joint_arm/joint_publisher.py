import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import math
import time

class JointPublisher(Node):
    def __init__(self):
        super().__init__('joint_publisher')
        self.pub1 = self.create_publisher(Float64, 'joint1_angle', 10)
        self.pub2 = self.create_publisher(Float64, 'joint2_angle', 10)
        self.timer = self.create_timer(0.5, self.publish_angles)
        self.angle = 0.0

    def publish_angles(self):
        msg1 = Float64()
        msg2 = Float64()
        msg1.data = math.sin(self.angle)
        msg2.data = math.cos(self.angle)

        # Collision detection thresholds
        if abs(msg1.data) > 1.0:
            self.get_logger().warn(f'Joint1 in collision range: {msg1.data:.2f}')
        if abs(msg2.data) > 1.0:
            self.get_logger().warn(f'Joint2 in collision range: {msg2.data:.2f}')

        self.pub1.publish(msg1)
        self.pub2.publish(msg2)
        self.get_logger().info(f'Published joint1: {msg1.data:.2f}, joint2: {msg2.data:.2f}')
        self.angle += 0.1

def main(args=None):
    rclpy.init(args=args)
    node = JointPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
