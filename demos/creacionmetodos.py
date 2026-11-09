CuentaBancaria:
def __init__(self, titular: str, saldo_inicial: float):
        self.titular = titular
        self.saldo = saldo_inicial
 # Método para depositar dinero
def depositar(self, monto: float):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito exitoso de ${monto}. Nuevo saldo: ${self.saldo}")
        else:
            print("El monto a depositar debe ser mayor a cero.")
 # Método para retirar dinero
 
def retirar(self, monto: float) -> bool:
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro exitoso de ${monto}. Saldo restante: ${self.saldo}")
            return True
        else:
            print("Fondos insuficientes o monto inválido.")
            return False
# Pruebas con los métodos
        mi_cuenta = CuentaBancaria("Ana Torres", 200000.0)
# Llamada a métodos
        mi_cuenta.depositar(50000.0) # Saldo sube a 250000
        mi_cuenta.retirar(100000.0) # Saldo baja a 150000
        mi_cuenta.retirar(300000.0) # Intento con saldo insuficiente
