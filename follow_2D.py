import time
import numpy as np
from mbot_bridge.api import MBot


def find_min_dist(ranges, thetas):
    """Finds the length and angle of the minimum ray in the scan.

    Make sure you ignore any rays with length 0! Those are invalid.

    Args:
        ranges (list): The length of each ray in the Lidar scan.
        thetas (list): The angle of each ray in the Lidar scan.

    Returns:
        tuple: The length and angle of the shortest ray in the Lidar scan.
    """
    min_dist, min_angle = None, None

    # TODO: Find the length and angle of the shortest distance in the ray.

    return min_dist, min_angle


robot = MBot()
setpoint = 0  # TODO: Pick your setpoint.

try:
    while True:
        # Read the latest Lidar scan.
        ranges, thetas = robot.read_lidar()

        # Get the distance and angle to the wall.
        dist_to_wall, angle_to_wall = find_min_dist(ranges, thetas)

        # TODO: Implement the 2D Follow Me controller
        # Hint: Look at your code from follow_1D
        # Hint: When you compute the velocity command, you might find the functions
        # np.sin(value) and np.cos(value) helpful!

        # Optionally, sleep for a bit before reading a new scan.
        time.sleep(0.1)
except:
    # Catch any exception, including the user quitting, and stop the robot.
    robot.stop()
