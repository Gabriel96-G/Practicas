"""Enunciado:
Crea una función llamada convertir_temperatura que reciba una
temperatura y una escala ([C] para Celsius o [F] para Fahrenheit).
La función debe convertir la temperatura a la otra escala.
Por ejemplo, si recibe 32, 'F', debe devolver 0°C.
Si recibe 100, 'C', debe devolver 212°F.
El estudiante debe analizar cómo aplicar las fórmulas de conversión y
validar que la escala sea correcta.
T (° C) x 9/5 + 32
"""

def convertir_temperatura(valor: float, escala: str) -> float:
    if escala.upper() == 'C':
        # Convertir de Celsius a Fahrenheit
        return valor * 9/5 + 32
    elif escala.upper() == 'F':
        # Convertir de Fahrenheit a Celsius
        return (valor - 32) * 5/9
    else:
        raise ValueError("Escala no válida. Use 'C' para Celsius o 'F' para Fahrenheit.")
    
def main():
    try:
        temp = float(input("Ingrese la temperatura a convertir: "))
        escala = input("Ingrese la escala de la temperatura original ([C] para Celsius, [F] para Fahrenheit): ")
        resultado = convertir_temperatura(temp, escala)
        if escala.upper() == 'C':
            print(f"{temp}°C son {resultado:.2f}°F")
        else:
            print(f"{temp}°F son {resultado:.2f}°C")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()  
    