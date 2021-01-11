# ros2_hi6

본 연구과제는 ros2d와 hi6 제어기의 interface를 만드는 과제이다.

# Prerequisite

본 프로젝트는 다음과 같은 third-party library를 필요로 한다.

## Ubuntu 20.04 
본 프로젝트는 ubuntu 20.04 ([우분투](http://releases.ubuntu.com/20.04.1/))를 기본으로 한다.

## ROS2 foxy
ROS는 Robot operating system으로 robot을 구동함에 있어 각 모듈을 유기적으로 연결시켜주는 역할을 한다.
본 프로젝트에서는 ROS2 foxy([ROS](http://wiki.ros.org/foxy))을 기본으로 한다.

    sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
    sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
    sudo apt-get update
    sudo apt-get install ros-foxy-desktop-full
    echo "source /opt/ros/foxy/setup.bash" >> ~/.bashrc
    source ~/.bashrc
    sudo apt install python-rosdep
    sudo rosdep init

## 실행방법
```
$ ros2 launch ros2_hi6 ros2_hi6.launch.py
```

## Folders description
* hyundai_description 
    * consist of robot's urdf and mesh files
    * launch : ros2 launch hyundai_description ros2_hi6.launch.py

* ros2_hi6 
    * build command : colcon build --symlink-install --packages-select ros2_hi6 
    * launch : ros2 launch ros2_hi6 ros2_hi6.launch.py
