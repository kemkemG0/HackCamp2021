import cv2
colorset = "MWN$@%#&B89EGA6mK5HRkbYT43V0JL7gpaseyxznocv?jIftr1li*=-~^`':;,. "


def convertToASCII(img, n):
    # resize image
    # determine resize scale with respect to the width = 400
    height, width, _ = img.shape
    scale_percent = width / 400 * 100

    scale_percent = 12  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)

    dim = (width, height)

    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    output = ""

    for gray2 in gray:
        output += "\n"
        for dark in gray2:
            output += colorset[dark // 4] * 2

    with open(f"Output/output{str(n)}.txt", mode="w") as f:
        f.write(output)
