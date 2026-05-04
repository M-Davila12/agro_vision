from ultralytics import YOLO

# Cargar el modelo
model = YOLO('yolov8n.pt')

# Cambia 'Pest-Detection-1/data.yaml' por solo 'data.yaml'
results = model.train(
    data='data.yaml', 
    epochs=50, 
    imgsz=640, 
    device='cpu'
)