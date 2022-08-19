from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='nao_lola',
            executable='nao_lola',
        ),
        Node(
            package='nao_ik',
            executable='ik_node',
        ),
        Node(
            package='nao_phase_provider',
            executable='nao_phase_provider',
            remappings=[
                ('fsr', '/sensors/fsr'),
            ]
        ),
        Node(
            package='walk',
            executable='walk',
        ),
    ])
