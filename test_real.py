import ollama
from ultralytics import YOLO

# 1. Cargar TU modelo entrenado en Colab
model = YOLO('best.pt')

# 2. Hacer una predicción con una imagen nueva (pon una foto de plaga en la carpeta)
# Cambia 'foto_prueba.jpg' por el nombre de tu imagen
# Cambia 'foto_prueba.jpg' por 'test1.jpg'
results = model.predict(source='test1.jpg', save=True, conf=0.5)

# 3. Extraer el nombre de la plaga detectada
for result in results:
    for box in result.boxes:
        class_id = int(box.cls[0])
        plaga_nombre = model.names[class_id]
        
        print(f"--- DETECTADO: {plaga_nombre} ---")

        # 4. Enviar el nombre a Ollama para el consejo agrícola
        prompt = f"Se ha detectado la plaga '{plaga_nombre}' en un cultivo. Dame un consejo breve de control orgánico y químico."
        
        response = ollama.chat(model='llama3.2:3b', messages=[
            {'role': 'user', 'content': prompt}
        ])
        
        print("\nCONSEJO DEL EXPERTO:")
        print(response['message']['content'])