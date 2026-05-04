# 🌾 AgroVision: Detección de Plagas con IA

Sistema de visión artificial para la identificación de plagas en cultivos y generación de recomendaciones mediante IA generativa local.

## 🚀 Requisitos Previos
* **Sistema Operativo:** Linux (Recomendado Fedora/Ubuntu) o Windows con WSL2.
* **Python:** 3.10 o superior.
* **Ollama:** Instalado y con el modelo `llama3.2` descargado.

## 🛠️ Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/agro_vision.git](https://github.com/tu-usuario/agro_vision.git)
   cd agro_vision


   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install ultralytics ollama opencv-python

  
Visión: YOLOv8 (archivo best.pt incluido en la raíz).

Lenguaje: Llama 3.2 vía Ollama (para recomendaciones técnicas).

💻 Uso
Asegúrate de que Ollama esté corriendo: ollama serve.

Ejecuta el script de prueba:

Bash
python test_real.py
