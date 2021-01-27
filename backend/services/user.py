from models.user import User

class UserService:

    @classmethod
    def buscar_por_id(cls, id):
        # pylint: disable=no-member
        user = User.objects.get(id=id).to_json()
        return user

    @classmethod
    def buscar_por_username(cls, username):
        # pylint: disable=no-member
        user = User.objects.get(username=username).to_json()
        return user

    @classmethod
    def buscar_todos(cls):
        # pylint: disable=no-member
        users = User.objects.to_json()
        return users