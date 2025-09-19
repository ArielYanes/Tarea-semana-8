import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
)
from PyQt5.QtGui import QFont, QPalette, QColor


class CalculadoraIMC(QWidget):
    def __init__(self):
        super().__init__()
        # Configuración principal de la ventana
        self.setWindowTitle("💪 Calculadora de IMC")
        self.setGeometry(400, 200, 400, 300)

        # Paleta de colores para el fondo de la ventana
        paleta = QPalette()
        paleta.setColor(QPalette.Window, QColor("#F3F9FF"))  # Azul claro
        self.setPalette(paleta)

        # ====== Título ======
        self.label_titulo = QLabel("Calculadora de Índice de Masa Corporal")
        self.label_titulo.setFont(QFont("Arial", 14, QFont.Bold))  # Fuente grande y en negrita

        # ====== Campo Nombre ======
        self.label_nombre = QLabel("Nombre:")
        self.input_nombre = QLineEdit()
        self.input_nombre.setPlaceholderText("Escribe tu nombre")  # Texto guía

        # ====== Campo Peso ======
        self.label_peso = QLabel("Peso (kg):")
        self.input_peso = QLineEdit()
        self.input_peso.setPlaceholderText("Ejemplo: 70")  # Placeholder

        # ====== Campo Altura ======
        self.label_altura = QLabel("Altura (m):")
        self.input_altura = QLineEdit()
        self.input_altura.setPlaceholderText("Ejemplo: 1.70")

        # ====== Botón Calcular ======
        self.boton_calcular = QPushButton("Calcular IMC")
        # Color verde y letras blancas en negrita
        self.boton_calcular.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold;")

        # ====== Botón Limpiar ======
        self.boton_limpiar = QPushButton("Limpiar")
        # Color rojo para destacar la acción de borrar
        self.boton_limpiar.setStyleSheet("background-color: #F44336; color: white; font-weight: bold;")

        # ====== Resultado ======
        self.resultado = QLabel("Resultado: ")
        self.resultado.setFont(QFont("Arial", 12, QFont.Bold))  # Texto más grande y negrita

        # ====== Conexión de eventos ======
        # Cuando se hace clic en calcular o limpiar
        self.boton_calcular.clicked.connect(self.calcular_imc)
        self.boton_limpiar.clicked.connect(self.limpiar)

        # ====== Layout principal ======
        layout = QVBoxLayout()

        # Agrego título
        layout.addWidget(self.label_titulo)
        layout.addSpacing(10)  # Espacio visual

        # Agrego campos de entrada
        layout.addWidget(self.label_nombre)
        layout.addWidget(self.input_nombre)

        layout.addWidget(self.label_peso)
        layout.addWidget(self.input_peso)

        layout.addWidget(self.label_altura)
        layout.addWidget(self.input_altura)

        # Layout horizontal para los botones
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.boton_calcular)
        h_layout.addWidget(self.boton_limpiar)

        layout.addLayout(h_layout)
        layout.addSpacing(15)
        layout.addWidget(self.resultado)

        # Aplico el layout a la ventana
        self.setLayout(layout)

    # ====== Función para calcular el IMC ======
    def calcular_imc(self):
        try:
            # Obtengo los valores del usuario
            peso = float(self.input_peso.text())
            altura = float(self.input_altura.text())
            nombre = self.input_nombre.text()

            # Fórmula del IMC: peso / altura^2
            imc = peso / (altura ** 2)

            # Determinar estado del IMC y color para mostrar
            if imc < 18.5:
                estado = "Bajo peso"
                color = "blue"
            elif 18.5 <= imc < 25:
                estado = "Normal"
                color = "green"
            elif 25 <= imc < 30:
                estado = "Sobrepeso"
                color = "orange"
            else:
                estado = "Obesidad"
                color = "red"

            # Actualizar etiqueta de resultado con color y texto
            self.resultado.setText(f"Resultado: {nombre}, tu IMC es {imc:.2f} ({estado})")
            self.resultado.setStyleSheet(f"color: {color}; font-weight: bold;")

            # Mostrar ventana emergente con la información
            QMessageBox.information(
                self, "Resultado IMC",
                f"{nombre}, tu IMC es {imc:.2f}\nEstado: {estado}"
            )

        except ValueError:
            # Si hay error al ingresar los datos (ejemplo: letras en lugar de números)
            QMessageBox.warning(self, "Error", "Por favor ingresa valores numéricos válidos.")

    # ====== Función para limpiar los campos ======
    def limpiar(self):
        self.input_nombre.clear()
        self.input_peso.clear()
        self.input_altura.clear()
        self.resultado.setText("Resultado: ")
        self.resultado.setStyleSheet("color: black;")  # Regresa el texto al color negro


# ====== Programa principal ======
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = CalculadoraIMC()
    ventana.show()
    sys.exit(app.exec_())
