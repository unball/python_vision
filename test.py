import cv2
import numpy as np

raw = cv2.imread('test.png', 0)

teste = raw[0:500, 0:100]

cv2.imshow("teste", teste)
cv2.waitKey(0)

'''
#contours, _ = cv2.findContours(raw, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#contours, _ = cv2.findContours(raw, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#contours, _ = cv2.findContours(raw, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)
contours, _ = cv2.findContours(raw, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_KCOS)

raw = cv2.cvtColor(raw, cv2.COLOR_GRAY2BGR)

for contour in contours:
    M = cv2.moments(contour)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])

    cv2.circle(raw,(cx, cy), 10, (0, 0 ,255), 1)

cv2.imshow("raw", raw)
cv2.waitKey(0)
'''
