# 1. EL INVENTARIO ORIGINAL
SERVIDORES = [
    {"nombre": "srv-web-01", "ip": "192.168.1.10", "rol": "web", "estado": "encendido"},
    {"nombre": "srv-db-01", "ip": "192.168.1.20", "rol": "db", "estado": "apagado"},
    {"nombre": "srv-web-02", "ip": "192.168.1.11", "rol": "web", "estado": "encendido"},
    {"nombre": "srv-backup", "ip": "192.168.1.30", "rol": "backup", "estado": "apagado"}
]


# 2. FUNCIÓN MOSTRAR INVENTARIO (Reutilizada)
def mostrar_inventario(lista_servidores):
    """Muestra los servidores por pantalla."""
    if not lista_servidores:
        print("[] (No hay coincidencias)")
        return
        
    for srv in lista_servidores:
        print(f"Nombre: {srv['nombre']} | IP: {srv['ip']} | Rol: {srv['rol']} | Estado: {srv['estado']}")


# 3. FUNCIONES DE FILTRADO (Apartado 3)
def filtrar_por_estado(servidores, estado):
    """Devuelve la lista de servidores del estado indicado."""
    lista = []
    for servidor in servidores:
        if servidor["estado"] == estado:
            lista.append(servidor)
    return lista


def filtrar_por_rol(servidores, rol):
    """Devuelve la lista de servidores del rol indicado."""
    lista = []
    for servidor in servidores:
        if servidor["rol"] == rol:
            lista.append(servidor)
    return lista


# ==========================================
# PRUEBAS DE FUNCIONAMIENTO
# ==========================================

print("--- Servidores Encendidos ---")
servidores_encendidos = filtrar_por_estado(SERVIDORES, "encendido")
mostrar_inventario(servidores_encendidos)

print("\n--- Servidores Apagados ---")
servidores_apagados = filtrar_por_estado(SERVIDORES, "apagado")
mostrar_inventario(servidores_apagados)

print("\n--- Servidores con Rol 'web' ---")
servidores_web = filtrar_por_rol(SERVIDORES, "web")
mostrar_inventario(servidores_web)

print("\n--- Prueba sin coincidencias (Rol 'correo') ---")
servidores_correo = filtrar_por_rol(SERVIDORES, "correo")
mostrar_inventario(servidores_correo)




