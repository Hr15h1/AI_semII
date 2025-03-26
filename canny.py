import cv2

img = cv2.imread("images/flower1.png", cv2.IMREAD_GRAYSCALE)
resized_image = cv2.resize(img, (img.shape[1]//3, img.shape[0]//3))
cv2.namedWindow("canny", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.imshow("Original Image", resized_image)

cv2.createTrackbar("min", "canny", 0, 255, lambda x: None)
cv2.createTrackbar("max", "canny", 0, 255, lambda x: None)

while True:
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    min_position = cv2.getTrackbarPos("min", "canny")
    max_position = cv2.getTrackbarPos("max", "canny")
    canny = cv2.Canny(resized_image, min_position, max_position)
    # print(canny.shape)
    # cv2.resizeWindow("canny", canny.shape[1]//3, canny.shape[0]//3)
    cv2.imshow("canny", canny)


cv2.destroyAllWindows()