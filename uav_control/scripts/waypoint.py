
#!/usr/bin/env python

import rospy
from mavros.msg import *
from mavros.srv import *

def logWayPoint(data):
	rospy.loginfo("Got waypoint: %s", data)

def main():
	rospy.init_node('wayPoint')
	rospy.Subscriber('/mavros/mission/waypoints ', wayPointList, logWayPoint)
	
	# pull waypoints
	rospy.loginfo("Waiting for Mavros service PULL...")
	rospy.wait_for_service('/mavros/mission/pull', timeout=None)
	rospy.ServiceProxy('/mavros/mission/pull', wayPointPull)
	rospy.loginfo("Pulled wayPoints %s", wayPointPull)
	
	# push waypoints
	rospy.loginfo("Waiting for Mavros service PUSH...")
	rospy.wait_for_service('/mavros/mission/push', timeout=None)
	
	waypoints = [
		Waypoint(frame=Waypoint.FRAME_GLOBAL_REL_ALT,
			command=Waypoint.NAV_WAYPOINT,
			is_current=True,
			x_lat=44.57, y_long=-123.27, z_alt=3.0)
		]
	rospy.ServiceProxy('/mavros/mission/push', wayPointPush)
	rospy.loginfo("Pushed wayPoints %s", wayPointPush(waypoints))
	
if __name__ == '__main__':
    main()






# def  (data):
    # rospy.loginfo("Got waypoints: %s", data)

# def main():
    # rospy.init_node('waypoint')
    # rospy.Subscriber('/mavros/mission/waypoints', WaypointList, handle_waypoints)

    # # Send a waypoint
    # rospy.loginfo("Waiting for MAVROS service...")
    # rospy.wait_for_service('/mavros/mission/push')

    # waypoints = [
            # Waypoint(frame=Waypoint.FRAME_GLOBAL_REL_ALT,
                # command=Waypoint.NAV_WAYPOINT,
                # is_current=True,
                # x_lat=44.57, y_long=-123.27, z_alt=3.0),
            # Waypoint(frame=Waypoint.FRAME_GLOBAL_REL_ALT,
                # command=Waypoint.NAV_WAYPOINT,
                # is_current=True,
                # x_lat=44.58, y_long=-123.27, z_alt=6.0)
        # ]
    # waypoint_push = rospy.ServiceProxy('/mavros/mission/push', WaypointPush)

    # resp = waypoint_push(waypoints)
    # rospy.loginfo(resp)

    # # Call the WaypointPull service
    # rospy.wait_for_service('/mavros/mission/pull')

    # rospy.loginfo("Calling WaypointPull service")
    # waypoint_pull = rospy.ServiceProxy('/mavros/mission/pull', WaypointPull)

    # resp = waypoint_pull()
    # rospy.loginfo(resp)

    # rospy.spin()


# if __name__ == '__main__':
    # main()