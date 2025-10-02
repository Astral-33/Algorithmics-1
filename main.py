# main.py
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QFormLayout,
    QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
)
from PyQt5.QtGui import QIcon
from BaseDatos import BaseDeDatos

class AppClientes(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Clientes - Marketplace")
        self.setGeometry(200, 200, 700, 400)

        self.setWindowIcon(QIcon("handsome squidward.webp"))
        
        # --- Backend ---
        self.db = BaseDeDatos("AmazonDB")
        self.db.crear_tabla("Clientes", [
            "nombre", "apellido", "cedula",
            "celular", "correo", "fecha_nacimiento"
        ])
        self.tabla_clientes = self.db.obtener_tabla("Clientes")

        # --- UI ---
        layout = QVBoxLayout()

        # Formulario
        form = QFormLayout()
        self.input_nombre = QLineEdit()
        self.input_apellido = QLineEdit()
        self.input_cedula = QLineEdit()
        self.input_celular = QLineEdit()
        self.input_correo = QLineEdit()
        self.input_fecha = QLineEdit("DD/MM/AAAA")

        form.addRow("Nombre:", self.input_nombre)
        form.addRow("Apellido:", self.input_apellido)
        form.addRow("Cédula:", self.input_cedula)
        form.addRow("Celular:", self.input_celular)
        form.addRow("Correo:", self.input_correo)
        form.addRow("Fecha Nac.:", self.input_fecha)

        self.btn_agregar = QPushButton("Agregar Cliente")
        self.btn_agregar.clicked.connect(self.agregar_cliente)
        form.addRow(self.btn_agregar)

        layout.addLayout(form)

        # Tabla visual
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "Nombre", "Apellido", "Cédula", "Celular", "Correo", "Fecha Nac."
        ])
        layout.addWidget(self.table)

        self.setLayout(layout)

    def agregar_cliente(self):
        datos = {
            "nombre": self.input_nombre.text(),
            "apellido": self.input_apellido.text(),
            "cedula": self.input_cedula.text(),
            "celular": self.input_celular.text(),
            "correo": self.input_correo.text(),
            "fecha_nacimiento": self.input_fecha.text()
        }

        if not all(datos.values()):
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios")
            return

        if self.tabla_clientes.insertar(datos):
            self.mostrar_clientes()
            self.limpiar_campos()
        else:
            QMessageBox.warning(self, "Error", "Estructura de datos inválida")

    def mostrar_clientes(self):
        filas = self.tabla_clientes.seleccionar()
        self.table.setRowCount(len(filas))
        for i, fila in enumerate(filas):
            for j, valor in enumerate(fila.values()):
                self.table.setItem(i, j, QTableWidgetItem(str(valor)))

    def limpiar_campos(self):
        self.input_nombre.clear()
        self.input_apellido.clear()
        self.input_cedula.clear()
        self.input_celular.clear()
        self.input_correo.clear()
        self.input_fecha.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = AppClientes()
    ventana.show()
    sys.exit(app.exec_())
