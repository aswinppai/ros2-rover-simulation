from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        # Kill any running Gazebo processes
        ExecuteProcess(
            cmd=['pkill', '-9', 'gzserver'],
            shell=True
        ),

        ExecuteProcess(
            cmd=['pkill', '-9', 'gzclient'],
            shell=True
        ),

        # Small delay to free ports
        ExecuteProcess(
            cmd=['sleep', '2'],
            shell=True
        ),

        # Start Gazebo with ROS2 factory plugin
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),

        # Publish robot model
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{
                'robot_description': open(
                    '/home/yogau/ros2_ws/src/rover_sim/urdf/rover.urdf'
                ).read()
            }],
            output='screen'
        ),

        # Spawn robot in Gazebo
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-entity', 'rover',
                '-topic', 'robot_description'
            ],
            output='screen'
        ),


	#KEY board shotcut
Node(
    package='teleop_twist_keyboard',
    executable='teleop_twist_keyboard',
    output='screen',
    prefix='xterm -e'
),

    ])
