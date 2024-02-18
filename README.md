# ROS Teaching resources 

## examples folder 

### mrt_ws 

The ROS2 workspace mrt_ws contains the code of a package named my_robot_control. 
To build it, check before that ROS2 is installed on your system, the code was tested with Foxy (ubuntu 20.04) and then execute this command:

```
git clone https://github.com/gdherbom/ros_teaching.git
cd ros_teaching/examples/mrt_ws
colcon build --symlink-install
```

If succesful, you can run the node:
```
source install/setup.bash
ros2 run my_robot_control speed_controller 
```

To test the behavior, on a second terminal, launch this command: 
```
ros2 topic pub /input_cmd std_msgs/msg/Float32 'data: 10.0'
```

The speed_controller node will output this result @1Hz: 
```
[INFO] [1708244230.255081257] [speed_controller]: speed_msg = std_msgs.msg.Float32(data=5.529227441006103)
[INFO] [1708244231.248648663] [speed_controller]: speed_msg = std_msgs.msg.Float32(data=10.48259983330316)
[INFO] [1708244232.248713128] [speed_controller]: speed_msg = std_msgs.msg.Float32(data=15.848672227582284)
```
data values may differ due to the random number generation in the equation : y(t) = y(t-1) + x(t) + ran(-10,10)




