# Función sin parámetros (siempre hace lo mismo)
# def imprime_separador_simple():
#     print("-"*25)

# # Invocación ejecuta la función
# imprime_separador_simple()
# imprime_separador_simple()





# def imprime_separador_simple(tam):
#     print("-" * tam)


    # imprime_separador_simple(70)
#     print("hola mundo")
#     imprime_separador_simple(50)        



def imprime_separador_simple(tam):
    # Todo lo que esté indentado aquí pertenece a la función
    print("-" * tam)

# Las llamadas de abajo ya no están indentadas, por lo que se ejecutan después de definir la función
imprime_separador_simple(70)
print("hola mundo")
imprime_separador_simple(50)
