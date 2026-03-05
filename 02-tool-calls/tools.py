import os

class Tools:
    
    def __init__(self):
        pass

    def obtener_clima(self, ciudad: str = "") -> str:
        print(f"Herramienta obtener_clima llamada con ciudad={ciudad}")
        # Aquí iría la lógica para obtener el clima de la ciudad
        return f"El clima en {ciudad} es soleado con 25 grados Celsius."
    
    
    
if __name__ == "__main__":
    tools = Tools()
    clima = tools.obtener_clima("Valencia")
    print(clima)