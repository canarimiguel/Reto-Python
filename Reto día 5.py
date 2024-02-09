class Usuario:
    def __init__(self, nombre, apellidos, telefono, correo):
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.correo = correo

class RegistroUsuarios:
    def __init__(self):
        self.usuarios = {}
        self.contador_id = 1

    def registrar_usuario(self, usuario):
        usuario.id = self.contador_id
        self.usuarios[self.contador_id] = usuario
        self.contador_id += 1

    def mostrar_ids(self):
        print("\nIDs de usuarios registrados:")
        for user_id in self.usuarios:
            print(f"ID {user_id}")

    def mostrar_usuario_por_id(self, user_id):
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            print(f"\nInformación del usuario con ID {user_id}:")
            print(f"Nombre: {usuario.nombre}")
            print(f"Apellidos: {usuario.apellidos}")
            print(f"Número de teléfono: {usuario.telefono}")
            print(f"Correo electrónico: {usuario.correo}")
        else:
            print(f"No existe un usuario con ID {user_id}.")

    def editar_usuario_por_id(self, user_id):
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            print(f"\nEditando información del usuario con ID {user_id}:")
            usuario.nombre = input("Nuevo nombre(s): ")
            usuario.apellidos = input("Nuevos apellidos: ")
            usuario.telefono = input("Nuevo número de teléfono: ")
            usuario.correo = input("Nuevo correo electrónico: ")
            print(f"Información actualizada para el usuario con ID {user_id}.")
        else:
            print(f"No existe un usuario con ID {user_id}.")

def main():
    registro = RegistroUsuarios()

    while True:
        print("\nMenú de opciones:")
        print("A. Registrar nuevos usuarios")
        print("B. Listar IDs de usuarios")
        print("C. Ver información de un usuario por ID")
        print("D. Editar información de un usuario por ID")
        print("E. Salir")

        opcion = input("Elige una opción (A/B/C/D/E): ")

        if opcion == "A":
            print("\nRegistrando nuevo usuario:")
            nombre = input("Ingresa tu nombre(s): ")
            apellidos = input("Ingresa tus apellidos: ")
            telefono = input("Ingresa tu número de teléfono: ")
            correo = input("Ingresa tu correo electrónico: ")

            usuario = Usuario(nombre, apellidos, telefono, correo)
            registro.registrar_usuario(usuario)
            print(f"Usuario registrado con ID {usuario.id}.")

        elif opcion == "B":
            registro.mostrar_ids()

        elif opcion == "C":
            user_id = int(input("Ingresa el ID del usuario: "))
            registro.mostrar_usuario_por_id(user_id)

        elif opcion == "D":
            user_id = int(input("Ingresa el ID del usuario a editar: "))
            registro.editar_usuario_por_id(user_id)

        elif opcion == "E":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    main()