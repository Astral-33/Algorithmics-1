# BaseDatos.py
from typing import List, Dict, Any, Optional, Set

class BaseDeDatos:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.tablas: Dict[str, 'Tabla'] = {}

    def crear_tabla(self, nombre_tabla: str, columnas: List[str]) -> bool:
        if nombre_tabla not in self.tablas:
            self.tablas[nombre_tabla] = Tabla(nombre_tabla, columnas)
            return True
        return False

    def obtener_tabla(self, nombre_tabla: str) -> Optional['Tabla']:
        return self.tablas.get(nombre_tabla)


class Tabla:
    def __init__(self, nombre: str, columnas: List[str]):
        self.nombre = nombre
        self.columnas: Set[str] = set(columnas)
        self.filas: List[Dict[str, Any]] = []

    def insertar(self, datos: Dict[str, Any]) -> bool:
        if self.columnas != set(datos.keys()):
            return False
        self.filas.append(datos)
        return True

    def seleccionar(self) -> List[Dict[str, Any]]:
        return self.filas

    def eliminar(self, indice: int) -> bool:
        if 0 <= indice < len(self.filas):
            self.filas.pop(indice)
            return True
        return False

    def actualizar(self, indice: int, nuevos_datos: Dict[str, Any]) -> bool:
        if 0 <= indice < len(self.filas) and set(nuevos_datos.keys()) == self.columnas:
            self.filas[indice] = nuevos_datos
            return True
        return False
