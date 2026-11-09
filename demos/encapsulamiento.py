class CuentaBancaria:
        def __init__(self, titular: str, saldo_inicial: float):
            self.titular = titular
            self.__saldo = saldo_inicial if saldo_inicial >= 0 else 0.0 # Atributo 



            # Getter para el saldo
        def get_saldo(self) -> float:
            return self.__saldo
        def set_saldo(self, nuevo_saldo: float):
            if nuevo_saldo >= 0:
                self.__saldo = nuevo_saldo
            else:
                print("Error: El saldo no puede ser negativo.")

        def depositar(self, monto: float):
            if monto > 0:
                self.__saldo += monto

# Uso y prueba del encapsulamiento
cuenta = CuentaBancaria("Juan", 100.0)
# Intentar acceder directamente al atributo privado generará AttributeError:
# print(cuenta.__saldo) # Error!
# Forma correcta a través del Getter
print(f"Saldo actual: ${cuenta.get_saldo()}") # 100.0
# Intentar modificar con Setter
cuenta.set_saldo(-50.0) # Muestra mensaje de error
cuenta.set_saldo(200.0) # Modificación válida
print(f"Saldo actualizado: ${cuenta.get_saldo()}")

