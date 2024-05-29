import cv2
import time
from twilio.rest import Client

# Configurações do Twilio
account_sid = 'SEU_ACCOUNT_SID_AQUI'
auth_token = 'SEU_AUTH_TOKEN_AQUI'
client = Client(account_sid, auth_token)
from_number = 'SEU_NUMERO_TWILIO_AQUI'
to_number = 'NUMERO_DESTINO_AQUI'

# Função para enviar SMS
def send_sms():
    message = client.messages.create(
        body="Rosto detectado por mais de 30 segundos.",
        from_=from_number,
        to=to_number
    )
    print(f"SMS enviado: {message.sid}")

# Carregar o classificador Haar Cascade pré-treinado para detecção de rosto
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inicializar a captura de vídeo da webcam (índice 0 é a webcam padrão)
video_capture = cv2.VideoCapture(0)

face_detected = False
start_time = None

while True:
    # Capturar um único frame do vídeo
    ret, frame = video_capture.read()

    # Converter o frame para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar rostos na imagem em escala de cinza
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Verificar se rostos foram detectados
    if len(faces) > 0:
        if not face_detected:
            face_detected = True
            start_time = time.time()
        else:
            elapsed_time = time.time() - start_time
            if elapsed_time > 30:
                send_sms()
                face_detected = False  # Reset para evitar múltiplos envios
    else:
        face_detected = False
        start_time = None

    # Desenhar um retângulo ao redor de cada rosto detectado
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Exibir o frame com os rostos detectados
    cv2.imshow('Video', frame)

    # Pressionar 'q' para sair do loop e fechar a janela
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar a captura de vídeo e fechar todas as janelas abertas
video_capture.release()
cv2.destroyAllWindows()
