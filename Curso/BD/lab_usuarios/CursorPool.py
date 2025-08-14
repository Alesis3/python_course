from ConnetionUser import Connetion

class Cursor:

    def __init__(self):
        self._cursor = None
        self._connetion = None

    def __enter__(self):
        self._connetion = Connetion.connetion_bd()
        self._cursor = self._connetion.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Se comineza el with')
        if exc_val:
            self._cursor.rollback()
            print(f'Ocurrio una excepcion se hace rollback {exc_val}')

        else:
            self._connetion.commit()
            print('Se hace commit')

        self._cursor.close()
        Connetion.liberate_connetion(self._connetion)

