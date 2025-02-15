import cv2
import HandTrackingModule as htm
import direction as dir

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Set width
cap.set(4, 480)  # Set height

detector = htm.handDetector(detectionCon=0.75)

while True:
    success, img = cap.read()
    if not success:
        break

    # Detect hand and get pose direction
    pose = dir.direction(img)

    # Display detected direction on the window
    cv2.putText(img, f"Direction: {pose}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the frame
    cv2.imshow("Hand Tracking Test", img)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
