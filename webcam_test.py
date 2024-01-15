import cv2
import os

# Verifica se a pasta para armazenar as imagens existe, se não, cria-a
output_folder = 'imagens_webcam'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Inicializa a captura da webcam
cap = cv2.VideoCapture(0)  # O número '0' representa a webcam padrão do seu computador

# Configuração da gravação das imagens
fps = 24  # Define a taxa de frames por segundo desejada
count = 0

cap.read()
while True:
    ret, frame = cap.read()  # Captura um frame da webcam

    if ret:
        cv2.imshow('Webcam', frame)  # Exibe o frame capturado

        # Salva o frame como uma imagem na pasta especificada
        image_name = f'image_{count}.png'  # Nome do arquivo de imagem
        image_path = os.path.join(output_folder, image_name)  # Caminho completo do arquivo
        cv2.imwrite(image_path, frame)  # Salva o frame como imagem

        count += 1

        # Define o tempo de espera para capturar o próximo frame
        key = cv2.waitKey(int(1000 / fps)) & 0xFF

        # Se pressionar a tecla 'q', encerra a captura
        if key == ord('q'):
            break
    else:
        break

# Libera a captura e fecha as janelas abertas
cap.release()
cv2.destroyAllWindows()
