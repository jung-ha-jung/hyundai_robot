import rclpy
from rclpy.node import Node
import requests
import json
import web_service
import math
import time
from rclpy.duration import Duration
from rclpy.time import Time

from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

url_joint_trajectory = '/project/robot/joint_trajectory'

class JointTrajectoryHi6(Node):

    def __init__(self):
        super().__init__('joint_trajectory')
        self.http = web_service.http_client()
        self.data = dict()
        self.subscription = self.create_subscription(JointTrajectory, 'joint_trajectory', self.listener_joint_trajectory, 10)
        self.subscription  # prevent unused variable warning

    def listener_joint_trajectory(self, msg):

        # header
     #   self.data['seq'] = msg.header.seq
        self.data['sec'] = msg.header.stamp.sec
        self.data['nsec'] = msg.header.stamp.nanosec
        self.data['frame_id'] = msg.header.frame_id

        # joint names
        joint_no = len(msg.joint_names)
        #for i in range(0, joint_no):
        #    self.data['joint_name_%d' % (1+i)] = msg.joint_names[i]

        # points
        point_no = len(msg.points)
        print('joint_no=%d, point_no=%d' % (joint_no, point_no))

        for i in range(0, point_no):
            for j in range(0, joint_no):
                self.data['pos_%d_%d' % (1+i, 1+j)] = msg.points[i].positions[j]
                self.data['vel_%d_%d'] = msg.points[i].velocities[j]
                self.data['acc_%d_%d'] = msg.points[i].accelerations[j]
                # self.data['eff_%d_%d'] = msg.points[i].effort[j]
            self.data['time_from_start'] = self.seconds(msg.points[i].time_from_start)

        json_data = json.dumps(self.data)
        print(json_data)
 #       response = self.http.service_request('POST', url_joint_trajectory, json_data, "")
 #       if (response == False):
 #           return

    def seconds(self, duration):
        return (duration.sec + (duration.nanosec / 1e9))

def main(args=None):
    rclpy.init(args=args)

    joint_trajectory = JointTrajectoryHi6()

    rclpy.spin(joint_trajectory)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    joint_trajectory.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
