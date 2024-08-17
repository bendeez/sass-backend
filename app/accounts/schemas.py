from app.user.schemas import UserAccountCreate, UserAccountIn, UserAccountOut
from app.business.schemas import (
    BusinessAccountCreate,
    BusinessAccountIn,
    BusinessAccountOut,
)
from pydantic import BaseModel, Field
from typing import Annotated, Union
from app.user.schemas import UserAccountCreate
from app.business.schemas import BusinessAccountCreate
from app.user.models import Users
from app.business.models import Business
from app.accounts.models import Business_Users
from typing import Literal
from app.accounts.enums import AccountType


class BusinessUserAccountOut(BaseModel):
    email: str
    business_id: int
    role_name: str


class BusinessUserAccountCreate(BusinessUserAccountOut):
    password: str


class BusinessUserAccountIn(BaseModel):
    type: Literal[AccountType.BUSINESS_USERS] = AccountType.BUSINESS_USERS
    email: str
    password: str


AccountCreate = Annotated[
    Union[BusinessAccountCreate, UserAccountCreate], Field(..., discriminator="type")
]

Account = Union[Business, Business_Users, Users]
