import ollama
import json

# Este es el JSON que acabas de recibir
resultado_vision = """
[
  {
    "classification_predictions": [
      { "predictions": [{ "class": "earthworms", "confidence": 0.9832 }] },
      { "predictions": [{ "class": "earthworms", "confidence": 0.9773 }] }
    ]
  }
]
"""

# 1. Extraer todas las plagas únicas encontradas
datos = json.loads(resultado_vision)
lista_predicciones = datos[0]["classification_predictions"]
plagas_encontradas = set([p["predictions"][0]["class"] for p in lista_predicciones])

# 2. Convertir la lista en un texto para el prompt
plagas_texto = ", ".join(plagas_encontradas)

print(f"--- Sistema AgroIA: Analizando plagas encontradas: {plagas_texto} ---")

# 3. Prompt para Ollama
prompt = f"""
Soy un campesino y mi sistema de IA ha detectado lo siguiente en mi cultivo: {plagas_texto}.
Por favor, actúa como un experto agrónomo y dime:
1. ¿Son estas lombrices beneficiosas o perjudiciales para mi cultivo específico? (Aclara si son lombrices de tierra comunes o algún tipo de larva dañina).
2. Si son beneficiosas, ¿cómo puedo mantener el suelo saludable para ellas?
3. Si son una plaga (como gusanos cortadores), ¿qué remedio orgánico me sugieres?
Responde de forma clara y breve.
"""

# 4. Llamada a Ollama
response = ollama.chat(model='llama3.2:3b', messages=[
    {'role': 'user', 'content': prompt}
])

print("\n--- INFORME DEL AGRÓNOMO VIRTUAL ---")
print(response['message']['content'])