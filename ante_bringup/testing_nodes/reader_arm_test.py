#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray

import math


class ReaderArmTest(Node):

    def __init__(self):
        super().__init__('reader_arm_test')
        self.publisher_ = self.create_publisher(Float64MultiArray, '/arm_position_controller/commands', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Float64MultiArray()
        arm_pos = (self.i * 0.1) % 2
        msg.data = [arm_pos, arm_pos]
        self.publisher_.publish(msg)
        self.get_logger().info(f"Published arm position at {arm_pos} radians")
        self.i += 1


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