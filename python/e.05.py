servidor = {
    "nombre" : "web" , 
    "ip" : "10.10.10.10" ,
    "puerto" : 80 ,
    "activo" : True
}


# print(servidor)
# print(servidor["nombre"])

# if servidor ["activo"]== True:
#     print("Esta activo")
# else:
#     print("No esta activo")


   #if servidor ["activo"]
      #print("Esta activo")
   #else:
      #print("No esta activo")


 # Ap 03
 # cambiar la IP
 # nueva_ip = input("nueva IP")
 # servidor  ["ip"] = nueva_ip    




# añadiendo email si no existe cvrelo 
# servidor  ["email"] = "ana@local" 
# imprimir
# print(servidor)





# servidor = {"ip": "192.168.1.1", "puerto": 8080}  # Ejemplo de diccionario

# clave = input("Clave a buscar: ")

# if clave in servidor:
#     print(f"clave {clave} con valor {servidor[clave]}")
# else:
#     print(f"clave {clave} no existe")



for x in servidor:
   print(x, "=>", servidor["x"])


for clave, valor in servidor.items():
    print(clave, "=>", valor)




