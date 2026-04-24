from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class UserRepository():
    def __init__(self) -> None:
        ...
    
    @staticmethod
    def get_user_by_username(username: str) -> User | None:
        try:
            return User.objects.get(username=username)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def validate_password(user: User, password: str) -> bool:
        return user.check_password(password)
