from styx_msgs.msg import TrafficLight
import numpy as np
import cv2

class TLClassifier(object):
    def __init__(self):
        #TODO load classifier
        pass

    def get_classification(self, image):
        """Determines the color of the traffic light in the image

        Args:
            image (cv::Mat): image containing the traffic light

        Returns:
            int: ID of traffic light color (specified in styx_msgs/TrafficLight)

        """
        # convert the received image to HSV colorspace
        hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

        # The hue range of any color can be found as described in openCV documentation -
        # https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html # noqa

        # Hue range of Red is between 0 -10 & 160 - 180
        lower_red_1 = np.array([0, 100, 100],np.uint8)
        upper_red_1 = np.array([10, 255, 255],np.uint8)        

        lower_red_2 = np.array([160, 100, 100],np.uint8)
        upper_red_2 = np.array([180, 255, 255],np.uint8)

        mask_red_1 = cv2.inRange(hsv_image, lower_red_1, upper_red_1) 
        mask_red_2 = cv2.inRange(hsv_image, lower_red_2, upper_red_2) 

        if cv2.countNonZero(mask_red_1) + cv2.countNonZero(mask_red_2) > 50:
            return TrafficLight.RED
        
        # Hue range of yellow is between 20 - 30
        lower_yellow = np.array([20, 100, 100],np.uint8)
        upper_yellow = np.array([30, 255, 255],np.uint8)

        mask_yellow = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

        if cv2.countNonZero(mask_yellow) > 50:
            return TrafficLight.YELLOW
        
        # Hue range of green is between 50 - 70
        lower_green = np.array([50, 100, 100],np.uint8)
        upper_green = np.array([70, 255, 255],np.uint8)

        mask_green = cv2.inRange(hsv_image, lower_green, upper_green)

        if cv2.countNonZero(mask_green) > 50:
            return TrafficLight.GREEN

        return TrafficLight.UNKNOWN
