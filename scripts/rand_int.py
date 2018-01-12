#!/usr/bin/env python

import random
import rospy
from std_msgs.msg import UInt32

if __name__ == '__main__':
    random.seed()

    rospy.init_node('random')
    pub = rospy.Publisher('rand_int', UInt32, queue_size = 1)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        pub.publish(random.randint(0, 1000))
        rate.sleep()
