class MaquinaInferencia:
    def __init__(self):
        # Base de conocimientos que mapea una enfermedad (en este caso, Varicela)
        # Lista de síntomas y su respectiva probabilidad.
        self.base_conocimientos = {
            "Varicela": [
                ("Erupcion cutanea con manchas rojas y ampollas", 0.3),  # Síntoma: Erupción cutánea con manchas rojas y ampollas, Probabilidad: 30%
                ("Picazon intensa en las ampollas", 0.3),  # Síntoma: Picazón intensa en las ampollas, Probabilidad: 30%
                ("Fiebre moderada a alta", 0.1),  # Síntoma: Fiebre moderada a alta, Probabilidad: 10%
                ("Vomito", 0.15),  # Síntoma: Vómito, Probabilidad: 15%
                ("Fatiga", 0.1),  # Síntoma: Fatiga, Probabilidad: 10%
                ("Perdida de apetito", 0.1),  # Síntoma: Pérdida de apetito, Probabilidad: 10%
                ("Dolor de cabeza", 0.1),  # Síntoma: Dolor de cabeza, Probabilidad: 10%
                ("Dolor abdominal o muscular", 0.1),  # Síntoma: Dolor abdominal o muscular, Probabilidad: 10%
                ("Irritabilidad (niños pequenos)", 0.1),  # Síntoma: Irritabilidad (niños pequeños), Probabilidad: 10%
                ("Has estado en contacto con alguien con signos visibles de varicela?", 0.20),  # Pregunta: Has estado en contacto con alguien con signos visibles de varicela?, Probabilidad: 20%
            ]
        }

    def hacer_preguntas(self):
        respuestas = {}
        enfermedad = list(self.base_conocimientos.keys())[0]  # Obtiene el nombre de la enfermedad (en este caso, Varicela)

        # Itera sobre cada síntoma y su probabilidad asociada en la base de conocimientos
        for pregunta, probabilidad in self.base_conocimientos[enfermedad]:
            respuesta = input(f"{pregunta}: Si o No? ").lower()  # Pide al usuario que responda Si o No para cada síntoma
            respuestas[pregunta] = probabilidad if respuesta == "si" else 0  # Guarda la probabilidad si la respuesta es Sí, de lo contrario, guarda 0

        probabilidad_total = sum(respuestas.values())  # Calcula la probabilidad total sumando todas las probabilidades de los síntomas

        return enfermedad, probabilidad_total  # Retorna el nombre de la enfermedad y la probabilidad total


if __name__ == "__main__":
    maquina = MaquinaInferencia()

    print("Por favor, responde las siguientes preguntas con Si o No:")
    enfermedad_diagnosticada, probabilidad = maquina.hacer_preguntas()

    if probabilidad > 0:  # Si hay alguna probabilidad de enfermedad
        print(
            f"\nBasado en tus respuestas, hay un {probabilidad * 100}% de probabilidad de tener {enfermedad_diagnosticada}"
        )
    else:  # Si no hay ninguna probabilidad de enfermedad
        print(
            "\nNo se pudo determinar la enfermedad. Consulta a un profesional de la salud para un diagnóstico preciso."
        )
