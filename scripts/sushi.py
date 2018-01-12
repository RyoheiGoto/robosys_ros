#!/usr/bin/env python

import math
import rospy
from std_msgs.msg import String
from std_msgs.msg import UInt32

SUSHI = u"\U0001F363"
BEER = u"\U0001F37A"
msg = None

def is_prime(n):
    if n < 2:
        return False

    if n == 2 or n == 3 or n == 5:
        return True

    if not(n % 2) or not(n % 3) or not(n % 5):
        return False

    prime = 7
    step = 4

    while prime <= math.sqrt(n):
        if not(n % prime):
            return False
        
        prime += step
        step = 6 - step

    return True

def is_mersenne_prime(n):
    for i in range(n):
        mp = 2 ** i - 1
        
        if n == mp:
            return True
        elif mp > n:
            break

    return False

def cb(message):
    global msg

    if is_prime(message.data):
        if is_mersenne_prime(message.data):
            msg = message.data * BEER
        else:
            msg = message.data * SUSHI
    else:
        msg = None

if __name__ == '__main__':
    rospy.init_node('sushi')
    sub = rospy.Subscriber('rand_int', UInt32, cb)
    pub = rospy.Publisher('hey', String, queue_size = 1)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        if msg:
            pub.publish(msg)
        rate.sleep()
