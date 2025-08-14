
class User:

    def __init__(self, id=None, name=None, password=None):
        self._id = id
        self._name = name
        self._password = password

    def __str__(self):
        return f'{self._id}. {self._name} \n Contraseña: {self._password}'

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

