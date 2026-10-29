
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.core.dependencies import get_current_user

from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from app.db.dependencies import get_db
from app.db.models import User
from app.schemas.user import UserCreate, UserLogin, UserResponse

router = APIRouter()


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
)
def register_user(
    user_data: UserCreate,
    db: Session = Depends(get_db),
):
    existing_user = db.scalar(
        select(User).where(User.email == str(user_data.email))
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An account with this email already exists.",
        )

    new_user = User(
        email=str(user_data.email),
        full_name=user_data.full_name,
        hashed_password=hash_password(user_data.password),
    )

    db.add(new_user)

    try:
        db.commit()
        db.refresh(new_user)
    except Exception:
        db.rollback()
        raise

    return new_user


@router.post(
    "/login",
    summary="Log in and receive a JWT access token",
)
def login_user(
    user_data: UserLogin,
    db: Session = Depends(get_db),
):
    user = db.scalar(
        select(User).where(User.email == str(user_data.email))
    )

    if not user or not verify_password(
        user_data.password,
        user.hashed_password,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="This account is inactive.",
        )

    token = create_access_token(subject=str(user.id))

    return {
        "access_token": token,
        "token_type": "bearer",
    }

@router.get(
    "/me",
    response_model=UserResponse,
    summary="Get the currently authenticated user",
)
def get_my_profile(
    current_user: User = Depends(get_current_user),
):
    return current_user