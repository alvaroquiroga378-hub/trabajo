# Clase Padre / Base
class CuentaBancaria:
    def __init__(self, titular: str, saldo: float):
        self.titular = titular
        self._saldo = saldo # Usamos protegido (_) para permitir acceso en las clases hijas
    def obtener_saldo(self):
        return self._saldo
# Clase Hija 1
class CuentaAhorros(CuentaBancaria):
 def __init__(self, titular: str, saldo: float, tasa_interes: float):
    # Llama al constructor de la clase padre
        super().__init__(titular, saldo)
        self.tasa_interes = tasa_interes
        def aplicar_interes(self):
            interes = self._saldo * self.tasa_interes
            self._saldo += interes
            print(f"Interés aplicado: ${interes}. Nuevo saldo: ${self._saldo}")
# Clase Hija 2
class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular: str, saldo: float, limite_sobregiro: float):
        super().__init__(titular, saldo)
        self.limite_sobregiro = limite_sobregiro
    def retirar(self, monto: float)

        if monto <= (self._saldo + self.limite_sobregiro):
            self._saldo -= monto
            print(f"Retiro exitoso de ${monto}. Saldo restante: ${self._saldo}")
        else:
            print("Retiro excede el límite de sobregiro permitido.")

# Pruebas de Herencia
ahorros = CuentaAhorros("Laura", 1000000.0, 0.02) # 2% interés
ahorros.aplicar_interes()
corriente = CuentaCorriente("Pedro", 200000.0, 500000.0)
corriente.retirar(400000.0) # Retira usando sobregiro

