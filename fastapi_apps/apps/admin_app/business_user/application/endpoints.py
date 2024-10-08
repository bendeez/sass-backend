from fastapi import APIRouter, Depends, Request
from apps.admin_app.business_user.domain.service import BusinessUserService
from apps.admin_app.business_user.domain.schemas import BusinessUserAccountOut
from apps.admin_app.accounts.domain.models import Accounts
from apps.admin_app.auth.application.dependencies import get_account
from tools.application.rate_limiter import limiter, limit
from apps.admin_app.business_user.application.dependencies import (
    get_business_user_service,
)

business_user_router = APIRouter()


@business_user_router.get("/business-user/me", response_model=BusinessUserAccountOut)
@limiter.limit(limit)
async def get_business_user_info(
    request: Request,
    business_user_service: BusinessUserService = Depends(get_business_user_service),
    account: Accounts = Depends(get_account),
):
    business_user_info = await business_user_service.get_business_user_account_info(
        account=account
    )
    return business_user_info
