import cv2
import mediapipe as mp

def videoReader (path):
    mp_hand = mp.solutions.hands
    hands = mp_hand.Hands()

    #pass in path to video here instead of 0
    cap = cv2.VideoCapture(path)

    videoRep = []

    while True:
        success, img = cap.read()

        if not success:
            break

        result = hands.process(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
        if result.multi_hand_landmarks:
            videoRep.extend(result.multi_hand_landmarks)
    cap.release()
    cv2.destroyAllWindows()
    print(videoRep)
    return videoRep