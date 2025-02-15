import HandTrackingModule as htm

detector = htm.handDetector(detectionCon=0.75)
tipIds = [4, 8, 12, 16, 20]

def direction(img):
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    pose = ""

    if len(lmList) != 0:
        if lmList[8][2] > lmList[7][2] and lmList[8][2] > lmList[6][2] and lmList[8][2] > lmList[5][2] and lmList[8][
            2] > lmList[9][2] and lmList[8][2] > lmList[13][2] and lmList[12][2] > lmList[11][2] and lmList[12][2] > \
                lmList[10][2] and lmList[12][2] > lmList[10][2]:
            pose = "shoot_down"
        elif lmList[8][2] < lmList[7][2] and lmList[8][2] < lmList[6][2] and lmList[8][2] < lmList[5][2] and lmList[8][
            2] < lmList[9][2] and lmList[8][2] < lmList[13][2] and lmList[12][2] < lmList[11][2] and lmList[12][2] < \
                lmList[10][2] and lmList[12][2] < lmList[10][2]:
            pose = "shoot_up"
        elif lmList[8][2] > lmList[7][2] and lmList[8][2] > lmList[6][2] and lmList[8][2] > lmList[5][2] and lmList[8][2] > lmList[9][2] and lmList[8][2] > lmList[13][2]:
            pose = "down"
        elif lmList[8][2] < lmList[7][2] and lmList[8][2] < lmList[6][2] and lmList[8][2] < lmList[5][2] and lmList[8][2] < lmList[9][2] and lmList[8][2] < lmList[13][2] and lmList[10][2] < lmList[3][2]:
            pose = "up"
        elif lmList[8][1] < lmList[10][1] and lmList[8][1] < lmList[7][1] and lmList[8][1] < lmList[6][1] and lmList[8][1] < lmList[5][1]:
            pose = "right"
        elif lmList[8][1] > lmList[2][1] and lmList[8][1] > lmList[7][1] and lmList[8][1] > lmList[6][1] and lmList[8][1] > lmList[5][1]:
            pose = "left"
    return pose

    """
        up_down = "normal"
        right_left = "none"
        total_flipped = 0
        total_right = 0
        total_left = 0
        for i in range(1, 5):
            if lmList[tipIds[i]][2] > lmList[0][2]:
                total_flipped += 1

        if total_flipped > 3:
            up_down = "flipped"

        for i in range(1, 5):
            if lmList[tipIds[i]][1] < lmList[0][1]:
                total_right +=1
            if lmList[tipIds[i]][1] > lmList[0][1]:
                total_left +=1
        if total_left > 3:
            right_left = "left"
        elif total_right > 3:
            right_left = "right"


        if up_down == "normal":
            #Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            for id in range(1,5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            #print (fingers)
            totalFingers = fingers.count(1)
            #print (totalFingers)
        else:
            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            for id in range(1, 5):
                if lmList[tipIds[id]][2] > lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)


            totalFingers = fingers.count(1)
            # print (totalFingers)
        #print(fingers)
        pose = ""
        if totalFingers == 1 and fingers[1]:
            if right_left == "none":
                if up_down == "normal":
                    pose = "up"
                else:
                    pose = "down"
            elif right_left == "right":
                pose = "right"
            elif right_left == "left":
                pose = "left"
        """
