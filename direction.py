import cv2
import serial  # Serial communication library
import HandTrackingModule as htm

# Initialize hand detector
detector = htm.handDetector(detectionCon=0.75)

# Initialize serial connection to Arduino (Update 'COM3' to your port)
arduino = serial.Serial(port="COM3", baudrate=9600, timeout=1)

def direction(img):
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    pose = ""
    num = 0

    if len(lmList) != 0:
        if lmList[8][2] > lmList[7][2] and lmList[8][2] > lmList[6][2] and lmList[8][2] > lmList[5][2] and lmList[8][
            2] > lmList[9][2] and lmList[8][2] > lmList[13][2] and lmList[12][2] > lmList[11][2] and lmList[12][2] > \
                lmList[10][2] and lmList[12][2] > lmList[10][2]:
            pose = "shoot_down"
            num = 1
        elif lmList[8][2] < lmList[7][2] and lmList[8][2] < lmList[6][2] and lmList[8][2] < lmList[5][2] and lmList[8][
            2] < lmList[9][2] and lmList[8][2] < lmList[13][2] and lmList[12][2] < lmList[11][2] and lmList[12][2] < \
                lmList[10][2] and lmList[12][2] < lmList[10][2]:
            pose = "shoot_up"
            num = 2
        elif lmList[8][2] > lmList[7][2] and lmList[8][2] > lmList[6][2] and lmList[8][2] > lmList[5][2] and lmList[8][2] > lmList[9][2] and lmList[8][2] > lmList[13][2]:
            pose = "down"
            num = 3
        elif lmList[8][2] < lmList[7][2] and lmList[8][2] < lmList[6][2] and lmList[8][2] < lmList[5][2] and lmList[8][2] < lmList[9][2] and lmList[8][2] < lmList[13][2] and lmList[10][2] < lmList[3][2]:
            pose = "up"
            num = 4
        elif lmList[8][1] < lmList[10][1] and lmList[8][1] < lmList[7][1] and lmList[8][1] < lmList[6][1] and lmList[8][1] < lmList[5][1]:
            pose = "right"
            num =5
        elif lmList[8][1] > lmList[2][1] and lmList[8][1] > lmList[7][1] and lmList[8][1] > lmList[6][1] and lmList[8][1] > lmList[5][1]:
            pose = "left"
            num = 6

    return pose,num

def main():
    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        detected_pose,num = direction(img)

        if detected_pose:
            print(f"Detected Gesture: {detected_pose} Index: {num}")
            arduino.write('num'.encode() + b'\n')  # Send command to Arduino

        cv2.imshow("Hand Tracking", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()
