import cv2
import serial  # Handles communication with the Arduino
import HandTrackingModule as htm
import time  # Used to manage timing for serial communication

# Initialize the hand detection model
detector = htm.handDetector(detectionCon=0.75)

# Establish serial communication with the Arduino (ensure port is correct)
arduino = serial.Serial(port="COM5", baudrate=115200, timeout=1)


def direction(img):
    """Determines hand gesture and assigns a corresponding number."""
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    pose = ""
    num = 0

    if len(lmList) != 0:
        if (
            lmList[8][2] > lmList[7][2]
            and lmList[8][2] > lmList[6][2]
            and lmList[8][2] > lmList[5][2]
            and lmList[8][2] > lmList[9][2]
            and lmList[8][2] > lmList[13][2]
            and lmList[12][2] > lmList[11][2]
            and lmList[12][2] > lmList[10][2]
        ):
            pose = "shoot_down"
            num = 1
        elif (
            lmList[8][2] < lmList[7][2]
            and lmList[8][2] < lmList[6][2]
            and lmList[8][2] < lmList[5][2]
            and lmList[8][2] < lmList[9][2]
            and lmList[8][2] < lmList[13][2]
            and lmList[12][2] < lmList[11][2]
            and lmList[12][2] < lmList[10][2]
        ):
            pose = "shoot_up"
            num = 2
        elif (
            lmList[8][2] > lmList[7][2]
            and lmList[8][2] > lmList[6][2]
            and lmList[8][2] > lmList[5][2]
            and lmList[8][2] > lmList[9][2]
            and lmList[8][2] > lmList[13][2]
        ):
            pose = "down"
            num = 3
        elif (
            lmList[8][2] < lmList[7][2]
            and lmList[8][2] < lmList[6][2]
            and lmList[8][2] < lmList[5][2]
            and lmList[8][2] < lmList[9][2]
            and lmList[8][2] < lmList[13][2]
            and lmList[10][2] < lmList[3][2]
        ):
            pose = "up"
            num = 4
        elif (
            lmList[8][1] < lmList[10][1]
            and lmList[8][1] < lmList[7][1]
            and lmList[8][1] < lmList[6][1]
            and lmList[8][1] < lmList[5][1]
        ):
            pose = "right"
            num = 5
        elif (
            lmList[8][1] > lmList[2][1]
            and lmList[8][1] > lmList[7][1]
            and lmList[8][1] > lmList[6][1]
            and lmList[8][1] > lmList[5][1]
        ):
            pose = "left"
            num = 6

    return pose, num


def main():
    """Handles the camera feed, gesture detection, and serial communication."""
    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        detected_pose, num = direction(img)

        if detected_pose:
            command = f"{num}\n"  # Format the number to be sent
            arduino.write(command.encode())  # Send the command to Arduino

            time.sleep(0.01)  # Short delay for stability

            try:
                response = arduino.readline().decode(errors="ignore").strip()  # Read Arduino's response
                print("Supposed to be:", num, "returned", response)
            except UnicodeDecodeError:
                print("Received unreadable serial data, ignoring.")

        cv2.imshow("Hand Tracking", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
            break

    cap.release()
    cv2.destroyAllWindows()
    arduino.close()  # Close the serial connection when exiting


if __name__ == "__main__":
    main()
