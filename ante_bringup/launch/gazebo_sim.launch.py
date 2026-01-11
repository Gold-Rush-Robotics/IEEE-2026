import os
import xacro

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.actions import Node
from launch.substitutions import Command
from ament_index_python import get_package_share_path, get_package_share_directory

def generate_launch_description():
    urdf_path = os.path.join(get_package_share_path("ante_description"), "robots", "ante.urdf.xacro")
    rviz_config_path = os.path.join(get_package_share_path("ante_bringup"), "config", "view.rviz")

    print(rviz_config_path)

    urdf = ParameterValue(Command(["xacro ", urdf_path]), value_type=str)

    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description": urdf}]
    )

    rviz2_node = Node(
        package="rviz2",
        executable="rviz2",
        arguments=[{"-d", rviz_config_path}]
    )

    joint_state_publisher_gui_node = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui"
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory("ros-gz-sim"), "launch", "gz_sim.launch.py")]
        ),
    )

    return LaunchDescription([
        robot_state_publisher_node,
        rviz2_node,
        joint_state_publisher_gui_node,
        gazebo
    ])