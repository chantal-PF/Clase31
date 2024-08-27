viaje = []
nombre = []

def registra_usario():
    global nombre
    nombre = input("Resgistra tu nombre: ")
    print(f"Su nombre {nombre} se a registrado correctamente.")
    
def resevar_viaje():
    global viaje
    usuario = input("Ingrese su nombre:")
    if len(usuario) == nombre:
        viaje = input("Que viaje desea resevar: ")     
    
        
