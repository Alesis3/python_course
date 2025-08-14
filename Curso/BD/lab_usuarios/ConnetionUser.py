from psycopg2 import pool
import sys
import os
from dotenv import load_dotenv
load_dotenv()

class Connetion:
    _DATABASE = os.getenv("DATABASE")
    _USER = os.getenv("USER")
    _HOST = os.getenv("HOST")
    _PORT = os.getenv("PORT")
    _PASSWORD = os.getenv("PASSWORD")
    _pool = None
    _MIN = 1
    _MAX = 5


    @classmethod
    def getpool(cls):

        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN, cls._MAX,
                    host = cls._HOST,
                    user = cls._USER,
                    password = cls._PASSWORD,
                    port = cls._PORT,
                    database = cls._DATABASE)

                print('Se obtuvo correctamente el pool')
            except Exception as e:
                print(f'Ocurrio una excepcion {e}')
                sys.exit()

        return cls._pool

    @classmethod
    def connetion_bd(cls):
        conexion = cls.getpool().getconn()
        print(f'Se obtuvo el pool de la conexion: {conexion}')
        return conexion

    @classmethod
    def liberate_connetion(cls, connetion):
        cls.getpool().putconn(connetion)
        print('Se libera correctamente la conexión')

    @classmethod
    def close_connetion(cls):
        cls.getpool().closeall()
