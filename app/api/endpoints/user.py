from typing import List, Optional
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from app.infra.postgres.crud.user import user_crud
from app.infra.postgres.crud.event_x_user import event_x_user_crud
from app.infra.postgres.crud.event import event_crud
from app.schemas.user import CreateUser, UpdateUser, UserInDB, PayloadUser
from app.schemas.event_x_user import PayloadEventXUser
from app.schemas.event import UpdateEvent



router = APIRouter()

@router.post(
    "/",
    response_class=JSONResponse,
    response_model=UserInDB,
    status_code=200,
    responses={
        200: {"description": "user found"},
        401: {"description": "user unauthorized"},
        404: {"description": "user not found"},
    },
)
async def create_user(*, user: CreateUser):

    user = await user_crud.create(object_to_create=user)
    if user:
        return user
    else:
        return None

@router.post(
    "/counter",
    response_class=JSONResponse,
    response_model=int,
    status_code=200,
    responses={
        200: {"description": "user found"},
        401: {"description": "user unauthorized"},
        404: {"description": "user not found"},
    },
)
async def counter(*, payload: PayloadUser = None):
    payload_transform = payload.dict(exclude_none=True)
    counter = await user_crud.counter(payload = payload_transform)
    return counter

@router.get(
    "/{id_user}",
    response_class=JSONResponse,
    response_model=UserInDB,
    status_code=200,
    responses={
        200: {"description": "user found"},
        401: {"description": "user unauthorized"},
        404: {"description": "user not found"},
    },
)
async def get_by_id(*, id_user: int):
    user = await user_crud.get_by_id(object_id=id_user)
    if not user:
        return JSONResponse(status_code=404)
    else:
        return user

@router.get(
    "/",
    response_class=JSONResponse,
    response_model=List[UserInDB],
    status_code=200,
    responses={
        200: {"description": "event found"},
        401: {"description": "event unauthorized"},
        404: {"description": "event not found"},
    },
)
async def get_all():
    users = await user_crud.get_all()
    if not users:
        return JSONResponse(status_code=404)
    else:
        return users

@router.post(
    "/payload",
    response_class=JSONResponse,
    response_model=List[UserInDB],
    status_code=200,
    responses={
        200: {"description": "user found"},
        401: {"description": "user unauthorized"},
        404: {"description": "user not found"},
    },
)
async def get_with_payload( *,
        payload: Optional[PayloadUser],
        skip_interval: int = 0,
        limit_interval: int = 10):
    payload_transform = payload.dict(exclude_none=True)
    users = await user_crud.get_with_payload(payload= payload_transform, skip = skip_interval, limit = limit_interval )
    if not users:
        return JSONResponse(status_code=404)
    else:
        return users 

@router.put(
    "/{id_user}",
    response_class=JSONResponse,
    response_model=UserInDB,
    status_code=200,
    responses={
        200: {"description": "user found"},
        401: {"description": "user unauthorized"},
        404: {"description": "user not found"},
    },
)
async def update( *,id_user: int, in_user: UpdateUser):
    user = await user_crud.update(object_id = id_user, object_to_update = in_user )
    if not user:
        return JSONResponse(status_code=404)
    else:
        return user

@router.delete(
    "/{id_user}",
    response_class=JSONResponse,
    response_model=str,
    status_code=200,
    responses={
        200: {"description": "user found"},
        401: {"description": "user unauthorized"},
        404: {"description": "user not found"},
    },
)
async def delete_by_id( *,id_user : int):
    user = await user_crud.delete_by_id(object_id= id_user)
    if not user:
        return JSONResponse(status_code=404)
    else:
        return "register deleted"


@router.post(
    "/reservation",
    response_class=JSONResponse,
    response_model=dict,
    status_code=200,
    responses={
        200: {"description": "user found"},
        401: {"description": "user unauthorized"},
        404: {"description": "user not found"},
    },
)
async def create_reservation(*, payload: PayloadEventXUser):
    
    event = await event_crud.get_by_id(object_id=payload.event_id)

    if event["quantity"] > 0:
        reservation = await event_x_user_crud.create(object_to_create=payload)

        if reservation:
            event_update = UpdateEvent(**event)
            quantity = event_update.quantity
            quantity = quantity - 1
            event_update.quantity = quantity
            event = await event_crud.update(object_id=event["id"], object_to_update=event_update)

            return reservation
        else:
            message = {"message": "Reservation not found"}
            return message
    else:
        message = {"message": "There are no more quotas"}
        return message


# @router.delete(
#     "/{user_id}",
#     response_class=JSONResponse,
#     status_code=204,
#     responses={
#         204: {"description": "user deleted"},
#         401: {"description": "user unauthorized"},
#         404: {"description": "user not found"},
#     },
# )
# async def remove(*, user_id: int):
#     payload = {
#         "id":user_id
#     }
#     user_remove = await user_crud.remove_user(query=payload)
#     if not user_remove:
#         return JSONResponse(status_code=404)
#     return user_remove


# @router.put(
#     "/{user_id}",
#     response_class=JSONResponse,
#     response_model=UserResponse,
#     status_code=200,
#     responses={
#         200: {"description": "user updated"},
#         401: {"description": "user unauthorized"},
#         404: {"description": "user not found"},
#     },
# )
# async def update(*, user_id: int, user_in: UpdateUser):

#     payload = user_in

#     payload_id = {
#         "id" : user_id
#     }

#     user = await user_crud.update_user(id=payload_id, new_user=payload)
#     if not user:
#         return JSONResponse(status_code=404)
#     else:
#         user = UserResponse(**user)
#         return user

# @router.post(
#     "/auth/",
#     response_class=JSONResponse,
#     response_model=UserInDB,
#     status_code=200,
#     responses={
#         200: {"description": "user found"},
#         401: {"description": "user unauthorized"},
#         404: {"description": "user not found"},
#     },
# )
# async def get_user_by_payload(*,user_payload: PayloadUser):
#     user_payload = user_payload.dict()
#     user = await user_crud.get_user_payload(payload=user_payload)
#     if not user:
#         return JSONResponse(status_code=404)
#     else:
#         user = UserInDB(**user[0])
#         return user

# @router.get(
#     "/get_users/",
#     response_class=JSONResponse,
#     response_model=list,
#     status_code=200,
#     responses={
#         200: {"description": "user found"},
#         401: {"description": "user unauthorized"},
#         404: {"description": "user not found"},
#     },
# )
# async def get_all_users():
#     users = await user_crud.get_users()
#     if not users:
#         return JSONResponse(status_code=404)
#     else:
#         response_user = []
#         for user in users:
#             user = UserList(**user)
#             response_user.append(user)
#         return response_user

# @router.post(
#     "/get_by_username/",
#     response_class=JSONResponse,
#     response_model=UserInDB,
#     status_code=200,
#     responses={
#         200: {"description": "user found"},
#         401: {"description": "user unauthorized"},
#         404: {"description": "user not found"},
#     },
# )
# async def get_user_by_payload(*,user_payload: UsernamePayload):
#     user_payload = user_payload.dict()
#     user = await user_crud.get_user_payload(payload=user_payload)
#     if not user:
#         return JSONResponse(status_code=404)
#     else:
#         user = UserInDB(**user[0])
#         return user