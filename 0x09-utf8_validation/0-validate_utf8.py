def ordenar(doc_id, nombre, apellidos, telefono):
    for i in range(0, N-1):
        for j in range(i+1, N):
            if nombre[i] > nombre[j]:
                # organizo doc_id
                t = doc_id[i]
                doc_id[i] = doc_id[j]
                doc_id[j] = t
                # organizo nombre
                t = nombre[i]
                nombre[i] = nombre[j]
                nombre[j] = t
                # organizo apellidos
                t = apellidos[i]
                apellidos[i] = apellidos[j]
                apellidos[j] = t
                # organizo telefono
                t = telefono[i]
                telefono[i] = telefono[j]
                telefono[j] = t
                return doc_id, nombre, apellidos, telefono


N = int(input('Ingrese cantidad de datos a registrar: '))
doc_id = []
nombre = []
apellidos = []
telefono = []
for i in range(N):
    doc_id.append(int(input('ingrese documento de identidad: ')))
    nombre.append(input('ingrese nombre: '))
    apellidos.append(input('apellido: '))
    telefono.append(int(input('Telefono: ')))
    print()
    print(doc_id)
    print(nombre)
    print(apellidos)
    print(telefono)
    documento, nombres, apellido, telefonos = ordenar(
        doc_id, nombre, apellidos, telefono)
    print()
    print()
for x in range(N):
    print(documento[x])
    print(nombres[x])
    print(apellido[x])
    print(telefonos[x])
    print()
