print("funciones creadas por el usuario")
def Mi_lista():
    amigos=["Homero","Paty","Lety"]
    for nava in amigos:
        print(nava)
# llamadas a funciones
print("----Ejemplo de funcion----")
Mi_lista()   

def Mis_listas():
    amigos=["Homero", "Paty", "Lety"]
    print(amigos)
    for nava in amigos:
        print(nava)
print("----Ejemplo de listas----")
Mis_listas()

def Mi_tupla():
    amigos=("Homero", "Paty", "Lety")
    print(amigos)
    for nava in amigos:
        print(nava)
print("----Ejemplo de tuplas----")
Mi_tupla() 

def Mi_conjunto():
    amigos={"Homero", "Paty", "Lety"}
    print(amigos)
    for nava in amigos:
        print(nava)
print("-----Ejemplo de conjuntos----") 
Mi_conjunto()   

def Mi_diccionario():
    amigos= {
        "amigo1" : "homero",
        "amigo2" : "Paty",
        "amigo3" : "Lety"
    }
    print(amigos)
    for nava in amigos:
        print(nava)
print("----Ejemplo de diccionarios----")
Mi_diccionario()