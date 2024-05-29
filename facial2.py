import cv2
import time
import reconhecimento
from twilio.rest import Client


account_sid = 'AC9a06a2012637aa16113b2dd32283670b'
auth_token = '267832887f6ccd8a43397e70898ebeac'
client = Client(account_sid, auth_token)
from_number = '+17083152521'
to_number = '+55 31985702668'


def send_sms():
    message = client.messages.create(
        body="Rosto detectado por mais de 30 segundos.",
        from_=from_number,
        to=to_number
    )
    print(f"SMS enviado: {message.sid}")

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')  
video_capture = cv2.VideoCapture(0)

face_detected = False
start_time = None
if reconhecimento.identify_face() == 0:
 while True:
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    if len(faces) > 0:
        if not face_detected:
            face_detected = True
            start_time = time.time()
        else:
            elapsed_time = time.time() - start_time
            if elapsed_time > 15:
                send_sms()
                face_detected = False  
    else:
        face_detected = False
        start_time = None
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Camera', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
else:
    face_detected = False
    start_time = None
    print("Rosto detectado")
    cv2.destroyAllWindows()

