import os
os.system("cls")



"""El diccionario tiene una estructura de clave : valor.
   se ve así --> diccionario = {clave : valor}
   es la estructura ideal para darle un valor de amistad a cada persona
   en este caso"""

amiga_de = {
    "juana": ["maria"],# en este caso ponemos cada nombre dentro de una lista para que se transforme en un objeto
    "maria": ["rocio"],#si no estubiera dentro la fila y necesitaramos iterar con un for, lo haria cacarter por caracter
    "rocio": ["ana"],
    "ana": ["louisa"],
    "louisa": ["carla"],
    "carla": ["sofia"],
    "sofia": ["celeste"],
    "celeste": ["laura"],
    "laura": ["johanna"],
    "johanna":[] # esta es una manera de cortar el bucle (no recomendada)
}

# En la recursividad es recomendable darle una condición 
# que le de un break para evitar bucles inifinitos
# en este caso hemos creado una manera de cerrar el bucle en el mismo diccionario(no recomendado)

def amiga(x):
    
    y = [] 
    
    print(f"\n-->busca amiga de {x}")
    for z in amiga_de[x]:
        print(f"--> iteramos sobre los elementos de diccionario amiga_de --> en {x} y nos da {z}")
        y.append(z)
        
        #aca se a llama la recursividad
        y.extend(amiga(z))  #aca decimos que amiga ahora es z 
        #print(f"-->aca se ve el procesos de guardado de {y}"
    return y

las_amigas = amiga("juana")
print(f"\nlas amigas de Juana son :{las_amigas}")
print("\n-----------------------------------------------------------------------")
