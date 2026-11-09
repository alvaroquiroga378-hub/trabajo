class CuentaBancaria:
    def __init__(self, titular: str, saldo: float):
        self.titular = titular
        self.saldo = saldo
    # Método genérico que será sobrescrito por las clases hijas
    def generar_extracto(self):
        return f"Extracto General - Titular: {self.titular} | Saldo: ${self.saldo}"
class CuentaAhorros(CuentaBancaria):
    def generar_extracto(self):
 # Sobrescritura de método
        return f"[CUENTA DE AHORROS] Titular: {self.titular} | Saldo Disponible:${self.saldo}"

class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular: str, saldo: float, sobregiro: float):
        super().__init__(titular, saldo)
        self.sobregiro = sobregiro

    def generar_extracto(self):
 # Sobrescritura de método
        return f"[CUENTA CORRIENTE] Titular: {self.titular} | Saldo: ${self.saldo} |Cupo Sobregiro: ${self.sobregiro}"
#Demostración del Polimorfismo
# Creamos una lista heterogénea de cuentas
cuentas = [
 CuentaAhorros("Andrés", 300000.0),
 CuentaCorriente("Beatriz", 150000.0, 200000.0),
 CuentaAhorros("Camilo", 800000.0)
]
# Recorremos la lista ejecutando la misma función en objetos distintos
print("--- EXTRACTOS BANCARIOS ---")
for c in cuentas:
 # Se ejecuta el método correspondiente a la clase de cada objeto en tiempo de
    ejecución:
print(c.generar_extracto())
