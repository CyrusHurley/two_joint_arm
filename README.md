# ROS2 Two-Joint Robotic Arm Simulator 🤖

## 🔧 Technical Overview
This is a ROS2 package named `two_joint_arm` that simulates movement in a 2-joint robotic arm using Python and the `rclpy` client library.

The `joint_publisher` node:
- Publishes sine/cosine-based angles to two topics: `/joint1_angle` and `/joint2_angle`
- Uses a timer to publish messages at regular intervals (0.5s)
- Simulates motion using `math.sin()` and `math.cos()`
- Implements basic **collision detection logic** by checking angle thresholds and logging warnings if values exceed safe bounds

### ROS2 Tools Used:
- ✅ `rclpy` (ROS2 Python Client)
- ✅ `Float64` messages from `std_msgs`
- ✅ Custom publisher node with `create_timer` and `create_publisher`

---

## 👵 Plain-English Summary (for Grandma)
This code makes a pretend robot arm move back and forth. It sends out messages that say “move this joint to this angle.” If the angles get too big (like if the arm might hit something), it warns us.

You can think of this like early training wheels for a robot’s brain — just teaching it how to move safely in a virtual space.

---

## 🧪 Run It

After building your workspace:
```bash
source install/setup.bash
ros2 run two_joint_arm joint_publisher