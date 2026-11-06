# ==========================================
# APARTADOS ANTERIORES: Mostrar Inventario
# ==========================================
def mostrar_inventario(servidores):
    """Muestra de forma formateada los servidores de la lista.
    Si la lista está vacía, indica que no hay servidores."""
    if not servidores:
        print("No hay servidores que coincidan con el filtro.")
        return

    print(f"{'NOMBRE':<15} {'IP':<15} {'ROL':<15} {'ESTADO':<15}")
    print("-" * 60)
    for srv in servidores:
        print(f"{srv.get('nombre', 'N/A'):<15} {srv.get('ip', 'N/A'):<15} {srv.get('rol', 'N/A'):<15} {srv.get('estado', 'N/A'):<15}")


# ==========================================
# APARTADO 3: Funciones de Filtrado
# ==========================================
def filtrar_por_estado(servidores, estado):
    """Devuelve una lista con los servidores del estado indicado."""
    # Crea una lista nueva mediante comprensión de listas sin alterar la original
    return [srv for srv in servidores if srv.get('estado') == estado]


def filtrar_por_rol(servidores, rol):
    """Devuelve una lista con los servidores del rol indicado."""
    # Crea una lista nueva mediante comprensión de listas sin alterar la original
    return [srv for srv in servidores if srv.get('rol') == rol]


# ==========================================
# PRUEBAS DE FUNCIONAMIENTO
# ==========================================
if __name__ == "__main__":
    # Inventario original de prueba
    inventario_original = [
        {"nombre": "srv-web-01", "ip": "192.168.1.10", "rol": "web", "estado": "activo"},
        {"nombre": "srv-db-01", "ip": "192.168.1.20", "rol": "db", "estado": "mantenimiento"},
        {"nombre": "srv-web-02", "ip": "192.168.1.11", "rol": "web", "estado": "activo"},
        {"nombre": "srv-backup", "ip": "192.168.1.30", "rol": "backup", "estado": "inactivo"}
    ]

    # 1. Prueba de filtrado por Estado
    print("\n=== SERVIDORES EN ESTADO 'activo' ===")
    activos = filtrar_por_estado(inventario_original, "activo")
    mostrar_inventario(activos)

    # 2. Prueba de filtrado por Rol
    print("\n=== SERVIDORES CON ROL 'web' ===")
    webs = filtrar_por_rol(inventario_original, "web")
    mostrar_inventario(webs)

    # 3. Prueba sin coincidencias (debe devolver [] y mostrar el aviso)
    print("\n=== SERVIDORES EN ESTADO 'error' (SIN COINCIDENCIAS) ===")
    errores = filtrar_por_estado(inventario_original, "error")
    mostrar_inventario(errores)








    