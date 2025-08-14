from CursorPool import Cursor
from User import User
class UserDao:

    _SELECCIONAR = 'SELECT * FROM user_lab ORDER BY id_user'
    _INSERTAR = 'INSERT INTO user_lab(username, password) VALUES (%s, %s)'
    _ACTUALIZAR = 'UPDATE user_lab SET username = %s, password = %s WHERE id_user = %s'
    _ELMINAR = 'DELETE FROM user_lab WHERE id_user = %s'

    @classmethod
    def select(cls):
        with Cursor() as cursor:
            cursor.execute(cls._SELECCIONAR)
            return cursor.fetchall()

    @classmethod
    def insert(cls, user):
        with Cursor() as cursor:
            valores = (user.name, user.password)
            cursor.execute(cls._INSERTAR, valores)
            registro = cursor.rowcount
            return f'Registros ingresados {registro}'

    @classmethod
    def update(cls, user):
        with Cursor() as cursor:
            valores = (user.name, user.password, user.id)
            cursor.execute(cls._ACTUALIZAR, valores)
            registro = cursor.rowcount
            return f'Registros actualizados: {registro}'

    @classmethod
    def delete(cls, user):
        with Cursor() as cursor:
            valor = (user.id, )
            cursor.execute(cls._ELMINAR, valor)
            registro = cursor.rowcount
            return f'Regristros eliminados: {registro}'

if __name__ == '__main__':
    persona = User().select()
    print(persona)