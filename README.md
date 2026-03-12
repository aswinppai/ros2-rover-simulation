# 🚀 ROS2 Rover Simulation (Gazebo)

## 1. Project Overview
This project implements a **4-wheel rover simulation using ROS2 and Gazebo**.  
The rover is modeled in **URDF**, spawned into Gazebo, and controlled via **ROS2 topics (`/cmd_vel`)**.

The rover can be driven using **keyboard teleoperation**, demonstrating a basic **robotics simulation pipeline**.

---

## 2. Technologies Used
- ROS2 Humble  
- Gazebo 11  
- URDF (Robot Description)  
- Python Launch Files  
- teleop_twist_keyboard  

---

## 3. Project Structure
The repository contains a ROS2 package named **`rover_sim`**.

```
rover_sim/
├── launch/
│   └── rover.launch.py
├── urdf/
│   └── rover.urdf
├── resource/
├── rover_sim/
│   └── __init__.py
├── test/
├── package.xml
├── setup.cfg
├── setup.py
└── README.md
```

### Folder Description

| Folder/File | Description |
|-------------|-------------|
| launch/ | ROS2 launch files to start the simulation |
| urdf/ | URDF robot model definition |
| resource/ | ROS2 package resource identifier |
| rover_sim/ | Python module for the ROS2 package |
| test/ | Test scripts for the package |
| package.xml | ROS2 package metadata and dependencies |
| setup.py | Python package configuration |
| setup.cfg | Package build configuration |
| README.md | Documentation and usage instructions |

---

## 4. Robot Model

The rover consists of the following links:

- `base_link` → robot body  
- `front_left_wheel`  
- `front_right_wheel`  
- `rear_left_wheel`  
- `rear_right_wheel`  

All wheels are connected using **continuous joints**.

Movement is controlled using the **Gazebo Differential Drive Plugin**.

---

## 5. Launch File

Main launch file:

```
launch/rover.launch.py
```

This launch file performs the following:

1. Kills old Gazebo processes  
2. Starts Gazebo with ROS plugins  
3. Publishes robot state using `robot_state_publisher`  
4. Spawns the rover model in Gazebo  
5. Starts keyboard teleoperation  

---

## 6. System Workflow

```
Keyboard Input
      ↓
teleop_twist_keyboard
      ↓
    /cmd_vel
      ↓
Gazebo Diff Drive Plugin
      ↓
Wheel joints rotate
      ↓
Rover moves in simulation
```

---

## 7. Installation

Clone the repository:

```bash
git clone https://github.com/aswinppai/ros2-rover-simulation.git
```

Move to your ROS2 workspace:

```bash
cd ros2_ws
```

Build the workspace:

```bash
colcon build
```

Source the workspace:

```bash
source install/setup.bash
```

---

## 8. Running the Simulation

Start the rover simulation:

```bash
ros2 launch rover_sim rover.launch.py
```

This will launch:

- Gazebo simulator  
- Rover robot model  
- Keyboard teleoperation  

---

## 9. Keyboard Controls

```
i  → move forward
k  → stop
j  → turn left
l  → turn right
,  → move backward
```

Control layout:

```
   u   i   o
   j   k   l
       ,
```

---

## 10. ROS Topics Used

Main control topic:

```
/cmd_vel
```

Message type:

```
geometry_msgs/Twist
```

Example manual command:

```bash
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.5}, angular: {z: 0.0}}"
```

---

## 11. Key Files

| File | Purpose |
|------|--------|
| rover.urdf | Robot model definition |
| rover.launch.py | Launch Gazebo and spawn rover |
| package.xml | ROS2 package metadata |
| setup.py | Python package configuration |

---

## 12. Future Improvements

- Add **Camera sensor**  
- Add **LiDAR sensor**  
- Visualize robot in **RViz**  
- Implement **SLAM**  
- Add **Autonomous navigation**

---

## 13. Author

**Aswin P Pai**  
CSE Student  

---

⭐ This project demonstrates a **basic robotics simulation pipeline using ROS2 and Gazebo**.
