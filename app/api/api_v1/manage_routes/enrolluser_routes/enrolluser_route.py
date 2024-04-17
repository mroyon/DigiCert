from fastapi import APIRouter, HTTPException, status, Depends
from app.services.user_services.user_service import UserService
from app.services.enrolluser_services.enrolluser_service import EnrollUserService
import pymongo
from app.schemas.user_schema import UserOut, UserAuth, UserUpdate
from app.schemas.enrolluser_schema import EnrollUserSchema

from app.models.user_models.user_model import UserModel
from app.models.enrolluser_models.enrolluser_model import EnrollUserModel
from app.api.deps.user_deps import get_current_user
from uuid import UUID

# User Route Entry Point
enrolluser_router = APIRouter()


@enrolluser_router.post("/enroll_user/")
async def enroll_user(user_data: EnrollUserSchema, user: UserModel = Depends(get_current_user)):
    # Prepare payload for external POST request
    try:
        print(f"data: {user_data}")
        user = await EnrollUserService.enroll_user(user_data, user)
        return {
            "code": 1,
            "message": "Success",
            "data": user
        }
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Warning! No response"
        )

