import os
import xacro

from launch import LaunchDescription
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.actions import Node
from launch.substitutions import Command
from ament_index_python import get_package_share_path

def generate_launch_description():
    urdf_path = os.path.join(get_package_share_path("ante_description"), "robots", "ante.urdf.xacro")
    rviz_config_path = os.path.join(get_package_share_path("ante_bringup"), "config", "view.rviz")
    controllers_file = os.path.join(get_package_share_path("ante_description"), 'config', 'controllers.yaml')

    urdf = ParameterValue(Command(["xacro ", urdf_path]), value_type=str)

    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description": urdf}]
    )

    rviz2_node = Node(
        package="rviz2",
        executable="rviz2",
        arguments=["-d", rviz_config_path]
    )

    control_node = Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[{'use_sim_time': False }, controllers_file],
        output="screen",
    )

    diff_drive_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["forward_position_controller"],
    )

    joint_state_publisher_gui_node = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui"
    )

    return LaunchDescription([
        robot_state_publisher_node,
        control_node,
        rviz2_node,
        diff_drive_spawner,
        joint_state_publisher_gui_node
    ])