import cv2
import numpy as np

def find_template_on_screen(screen_path, template_path, threshold=0.8):
    screen = cv2.imread(screen_path)
    template = cv2.imread(template_path)

    res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)

    points = list(zip(*loc[::-1]))
    return points
