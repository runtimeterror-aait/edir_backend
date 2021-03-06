from os import stat
from app.dependencies.authorization import admin
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.repository.auth import AuthHandler
from app.schemas import Member as MemberSchema, MemberCreate, MemberUpdate
from app.db.database import get_db
from app.db.repository.member import (
    get_all_members,
    create_member,
    delete_member,
    get_member_by_edir_username,
    get_member_by_id,
    get_member_by_user_id,
    update_member,
)
from app.db.repository.user import get_user
from app.db.repository.edir import get_edir_by_id, get_edir_by_username

auth_handler = AuthHandler()

router = APIRouter(
    prefix="/api/v1/members",
    tags=["Manage Members"],
    responses={404: {"description": "Not found"}},
)

# get members


@router.get("/{edir_id}")
def get_edir_members(
    edir_id: int,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    email=Depends(auth_handler.auth_wrapper),
    check_admin=Depends(admin),
):
    return get_all_members(db=db, edir_id=edir_id, skip=skip, limit=limit)

@router.get("/user/{user_id}")
def get_member_by_user_id_with_edir(
    user_id: int,
    db: Session = Depends(get_db),
    email=Depends(auth_handler.auth_wrapper),
):
    return get_member_by_user_id(db=db, user_id=user_id)


# add a member


@router.post("/")
def add_member(
    member: MemberCreate,
    email=Depends(auth_handler.auth_wrapper),
    db: Session = Depends(get_db),
):
    # if the user doesn't exist
    if not get_user(db=db, user_id=member.user_id):
        raise HTTPException(status_code=404, detail="Oops, User doesn't exist")

    # if the edir doesn't exist
    if not get_edir_by_username(db=db, username=member.edir_username):
        raise HTTPException(status_code=404, detail="Oops, Edir doesn't exist")

    if get_member_by_edir_username(db=db, username=member.edir_username):
        raise HTTPException(status_code=403, detail="Member already exist")
   
    return create_member(db=db, member=member)


# approval


@router.put("/{member_id}")
def approve_member(
    member_id: int,
    email=Depends(auth_handler.auth_wrapper),
    db: Session = Depends(get_db),
    check_admin=Depends(admin),
):
    return update_member(db=db, member_id=member_id)


# delete member


@router.delete("/{member_id}")
def remove_member(
    member_id: int,
    email=Depends(auth_handler.auth_wrapper),
    db: Session = Depends(get_db),
):
    
    return delete_member(db=db, member_id=member_id)
