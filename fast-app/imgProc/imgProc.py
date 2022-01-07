import cv2

colorset = "MWN$@%#&B89EGA6mK5HRkbYT43V0JL7gpaseyxznocv?jIftr1li*=-~^`':;,. "


def convertToASCII(img):
    height, width, _ = img.shape
    scale_ratio = 1  # ratio of original size
    if(width >= 400):
        scale_ratio = 400/width

    width = int(width * scale_ratio)
    height = int(height * scale_ratio)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    output = []
    for gray2 in gray:
        for dark in gray2:
            output.append(colorset[dark // 4] * 2)
        output.append("<br>")
    return ''.join(output)
