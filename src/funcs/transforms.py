from cv2 import cv2

def transformVectors(files):
    vectors = []
    images = []

    for f in files:
        images.append(cv2.imread(f))

    for i in images:
        img = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
        img = cv2.bitwise_not(img)
        image = img.flatten()
        image = image/255
        vectors.append(image)

    for j in vectors:
        for i in range(j.shape[0]):
            if j[i] == 0:
                j[i] = -1
            elif j[i] > 0.0001 and j[i] < 0.50:
                j[i] = -1
            elif j[i] > 0.80 and j[i] < 1:
                j[i] = 1

    return vectors


def transformVector(file):
    # vector = []
    test = cv2.imread(file)
    img = cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)
    img = cv2.bitwise_not(img)
    imgTest = img.flatten()
    imgTest = imgTest/255

    for i in range(imgTest.shape[0]):
        if imgTest[i] == 0:
            imgTest[i] = -1
        elif imgTest[i] > 0.0001 and imgTest[i] < 0.50:
            imgTest[i] = -1
        elif imgTest[i] > 0.80 and imgTest[i] < 1:
            imgTest[i] = 1

    return imgTest

