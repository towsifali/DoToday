from models.user_model import User
from schemas.user_schema import UserAuth
from core.security import get_password


class UserService:
    @staticmethod
    async def create_user(user: UserAuth) -> UserOut:
        user_in = User(
            email=user.email,
            username=user.username,
            password=get_password(user.password),
        )
        await user_in.save()
        return user_in
