from UserDao import UserDao
from User import User

while True:
    print('Ingresa la opcion a realizar\n'
          '1.Listar Usuarios\n'
          '2.Agregar Usuario\n'
          '3.Actualizar Usuario\n'
          '4.Eliminar Usuario\n'
          '5.Salir')
    user = int(input())

    if user == 1:
        usuarios = UserDao.select()
        for n in usuarios:
            print(f'{n[0]}. {n[1]} \n'
                  f'Contraseña: {n[2]}')

    elif user == 2:
        name1 = input('Ingrese el nombre: ')
        password1 = input('Ingrese la contraseña: ')
        usuario = User(name=name1, password=password1)
        print(UserDao.insert(usuario))

    elif user == 3:
        id_update = int(input('Ingresa el id que deseas actualizar: '))
        name1 = input('Cambio de nombre: ')
        password1 = input('Cambio de contraseña: ')
        usuario = User(name= name1, password=password1, id=id_update)
        print(UserDao.update(usuario))

    elif user == 4:
        id_delete = int(input('Ingresa el id a eliminar: '))
        usuario = User(id=id_delete)
        print(UserDao.delete(usuario))

    elif user == 5:
        break
