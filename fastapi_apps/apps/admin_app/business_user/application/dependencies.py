from fastapi import Depends
from apps.admin_app.business_user.domain.repository import BusinessUserRepository
from apps.admin_app.business_user.domain.service import BusinessUserService
from tools.application.dependencies import get_db
from sqlalchemy.ext.asyncio import AsyncSession


def _get_business_user_repository(
    db: AsyncSession = Depends(get_db),
) -> BusinessUserRepository:
    return BusinessUserRepository(db=db)


def get_business_user_service(
    business_user_repository: BusinessUserRepository = Depends(
        _get_business_user_repository
    ),
) -> BusinessUserService:
    return BusinessUserService(repository=business_user_repository)
