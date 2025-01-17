from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.dp_depends import get_db
from typing import Annotated

from app.models.user import User
from sqlalchemy import insert
from app.schemas import CreateUser

from slugify import slugify



router = APIRouter(prefix='/user', tags=['user'])


@router.get('/')
async def get_all_users():
    pass


@router.get('/user_id')
async def get_user_by_id():
    pass


@router.post('/create')
async def create_user(db: Annotated[Session, Depends(get_db)], create_category: CreateUser):
    db.execute(insert(User).values(name=create_user.name,
                                       parent_id=create_user.parent_id,
                                       slug=slugify(create_user.name)))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }


@router.put('/update')
async def update_user():
    pass


@router.delete('/delete')
async def delete_user():
    pass
