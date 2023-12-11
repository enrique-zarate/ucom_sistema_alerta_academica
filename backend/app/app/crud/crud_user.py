from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    """CRUD operations for the User model."""

    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        """Get a user by email.

        Args:
            db (Session): The database session.
            email (str): The email address to search for.

        Returns:
            Optional[User]: The user if found, else None.
        """
        return db.query(User).filter(User.email == email).first()

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        """Create a new user.

        Args:
            db (Session): The database session.
            obj_in (UserCreate): The input data for creating a user.

        Returns:
            User: The created user.
        """
        db_obj = User(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            full_name=obj_in.full_name,
            is_superuser=obj_in.is_superuser,
            roles=obj_in.roles,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        """Update a user.

        Args:
            db (Session): The database session.
            db_obj (User): The user object to update.
            obj_in (Union[UserUpdate, Dict[str, Any]]): The input data for updating a user.

        Returns:
            User: The updated user.
        """
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        password_update = update_data.get("password")
        if password_update:
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[User]:
        """Authenticate a user.

        Args:
            db (Session): The database session.
            email (str): The user's email address.
            password (str): The user's password.

        Returns:
            Optional[User]: The authenticated user if successful, else None.
        """
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def is_active(self, user: User) -> bool:
        """Check if a user is active.

        Args:
            user (User): The user object.

        Returns:
            bool: True if the user is active, else False.
        """
        return user.is_active

    def is_superuser(self, user: User) -> bool:
        """Check if a user is a superuser.

        Args:
            user (User): The user object.

        Returns:
            bool: True if the user is a superuser, else False.
        """
        return user.is_superuser


user = CRUDUser(User)
