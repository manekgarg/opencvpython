import cv2
print("Package Imported")

img = cv2.imread("Resources/khali.png")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray Image",imgGray)
cv2.waitKey(0)

# cap = cv2.VideoCapture(0)
# cap.set(3,1280)
# cap.set(4,720)
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break