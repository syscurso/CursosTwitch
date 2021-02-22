import cv2

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video = cv2.VideoCapture('titulo.png')

while True:

    succesful_frame_read, frame = video.read()

    if not succesful_frame_read:

        break

    frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(frame_grayscale)

    print(faces)

    for (x, y, w, h ) in faces:

        cv2.rectangle(frame, (x, y), (x+w, y+h), (100, 200, 50), 2)
    
    cv2.imshow('LOL', frame)

    if cv2.waitKey(0) & 0xFF == ord('q'):

        break

video.release()
cv2.destroyAllWindows()


print('Cerrado!!')


