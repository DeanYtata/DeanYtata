invitados = []

invitados.append(input ("Ingrese el nombre del invitado: "))
otro = input("Desea agregar otro? y/n : ")
while otro== "y":
    invitados.append(input ("Ingrese el nombre del invitado: "))
    otro = input("Desea agregar otro? y/n : ")

print("Usted tiene", len(invitados), "invitados")
print (invitados)