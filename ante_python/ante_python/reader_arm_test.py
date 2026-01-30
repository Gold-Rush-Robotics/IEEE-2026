#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray

import math
PI = math.pi


class ReaderArmTest(Node):
    def __init__(self):
        super().__init__('reader_arm_test')
        self.publisher_ = self.create_publisher(Float64MultiArray, '/arm_position_controller/commands', 10)
        timer_period = 5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Float64MultiArray()
        match self.i:
            # case 0: msg.data = [0, 0]
            # case 1: msg.data = [PI, 0]
            # case 2: msg.data = [PI/2, PI]

            case 0: msg.data = [PI/2, 0]
            case 1: msg.data = [0, 2*PI]
            case 2: msg.data = [PI, PI/2]
        self.publisher_.publish(msg)
        self.get_logger().info(f"Moving arm to {msg.data}")
        self.i += 1
        self.i %= 3


def main(args=None):
    rclpy.init(args=args)

    node = ReaderArmTest()

    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()