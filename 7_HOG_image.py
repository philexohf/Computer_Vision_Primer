# https://github.com/philexohf/Computer_Vision_Primer
import cv2

img = cv2.imread('./image/mercy2.jpg')
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
found, w = hog.detectMultiScale(img)


def is_inside(o, i):
    ox, oy, ow, oh = o
    ix, iy, iw, ih = i
    return ox > ix and oy > iy and ox + ow < ix + iw and oy + oh < iy + ih


def draw_person(image, person):
    x, y, w, h = person
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)


found_filter = []
for ri, r in enumerate(found):
    for qi, q in enumerate(found):
        if ri != qi and is_inside(r, q):
            break
        else:
            found_filter.append(r)

for person in found_filter:
    draw_person(img, person)

cv2.namedWindow('person_detector', 0)
cv2.imshow('person_detector', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
