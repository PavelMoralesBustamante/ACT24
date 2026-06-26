
#Colección para almacenar temporalmente los personajes 
personajes = []

def buscar(nombre):
    for i in range(len(personajes)):
        if personajes[i]["nombre"]==nombre:
            return i #retornamos la posición donde está
    return -1 #Si el personaje no se encuentra retorna -1

def agregar(nombre,clase,nivel):
    #validar los datos
    if len(nombre.strip())==0 or len(nombre.strip())>20:
        print("Nombre no válido")
        return
    elif buscar(nombre)>=0:
        print("Nombre ya existe")
        return
    elif clase not in ("Guerrero", "Mago","Pícaro"):
        print("Clase no válida, debe ser Guerrero, Mago o Pícaro")
        return
    elif nivel<=0 or nivel>50:
        print("El nivel debe estar entre 1 y 50")
        return
    #Registrar personaje en la lista
    rango = "recluta"
    if nivel>=30: rango = "Élite"
    pj = {"nombre":nombre,"clase":clase,"nivel":nivel,"rango":rango}
    personajes.append(pj)
    print("Personaje registrado")

def mostrar(nombre):
    posicion = buscar(nombre)
    if posicion >= 0:
        print(f"Persona encontrado : {personajes[posicion]}")
    else:
        print("Nombre no existe")

def listar():
    if len(personajes)>0:
        print(f"{"N°":<3}.- {"nombre":<20} {"Clase":<10} {"nivel":<4} {"rango":<10}")
        for i in range(len(personajes)):
            print(f"{i+1:<3}.- {personajes[i]["nombre"]:<20} {personajes[i]["clase"]:<10} {personajes[i]["nivel"]:<4} {personajes[i]["rango"]:<10}")
    else:
        print("No hay personajes registrados")

def eliminar(nombre):
    pos = buscar(nombre)
    if pos >= 0:
        personajes.pop(pos)
        print("Personaje Eliminado")
    else:
        print("Nombre no existe")

def subirNivel(nombre):
    pos = buscar(nombre)
    if pos >= 0:
        nivel = personajes[pos]["nivel"]
        if nivel<50:
            personajes[pos]["nivel"] = nivel+1
            print("Level UP ⚔️")
            #Si los personajes alcanzan nivel 30 son élite
            if personajes[pos]["nivel"]>=30: 
                personajes[pos]["rango"] = "Élite"
        else:
            print("El personaje ya tiene nivel máximo")
    else:
        print("El nombre del personaje no existe")

def estadisticas():
    if len(personajes)>0:
        sumaniveles = 0
        guerreros = 0
        magos = 0
        picaros = 0
        for pj in personajes:
            sumaniveles += pj["nivel"] #sumar niveles
            match pj["clase"]:
                case "Guerrero": guerreros+=1
                case "Mago": magos+=1
                case "Pícaro": picaros+=1
        promedio = round(sumaniveles/len(personajes) ,1)
        print(f"""
        Nivel promedio del gremio : {promedio}      
        🧝‍♂️Cantidad Guerreros : {guerreros}      
        🧙‍♂️Cantidad Magos     : {magos}      
        🥷Cantidad Picaros   : {picaros}      
    """)
    else:
        print("No hay personajes registrados")