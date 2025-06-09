# two_joint_arm

A ROS2 (Humble) simulation package for publishing joint angles of a 2-joint robotic arm using `Float64` messages.

## Features
- Simulates sine and cosine angle movement for two joints
- Publishes joint values to `joint1_angle` and `joint2_angle` topics
- Modular Python node with periodic publishing via ROS2 timers

## Run Instructions

```bash
cd ~/ros2_ws
colcon build
source install/setup.bash
ros2 run two_joint_arm joint_publisher

