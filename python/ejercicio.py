
# Crear lista y acceder a un valor que no existe 

latencias = [1.2, 3.4, 4.5, 16, 7]

indice = int(input("Posicion en la lista: "));

print("valor", latencias[indice])



try: 

    print("valor: ", latencias[indice])

except IndexError:

    print(f"Valor {indice}  fuera de randgo, maximo es {len(indice)-1}")

    


# Crear un diccinario y acceder a una clave que no existe 


servidor = {

    "nombre"


}