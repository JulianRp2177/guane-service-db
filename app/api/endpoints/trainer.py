from typing import List, Optional
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from app.infra.postgres.crud.trainer import trainer_crud
from app.schemas.trainer import CreateTrainer, UpdateTrainer, TrainerInDB, PayloadTrainer
#from app.services.user import UserService


router = APIRouter()

@router.post(
    "/",
    response_class=JSONResponse,
    response_model=TrainerInDB,
    status_code=200,
    responses={
        200: {"description": "user found"},
        401: {"description": "user unauthorized"},
        404: {"description": "user not found"},
    },
)
async def create_trainer(*, trainer: CreateTrainer):

    trainer = await trainer_crud.create(object_to_create=trainer)
    if trainer:
        return trainer
    else:
        return None

@router.get(
    "/{id_trainer}",
    response_class=JSONResponse,
    response_model=TrainerInDB,
    status_code=200,
    responses={
        200: {"description": "user found"},
        401: {"description": "user unauthorized"},
        404: {"description": "user not found"},
    },
)
async def get_byid(*, id_trainer: int):
    trainer = await trainer_crud.get_by_id(object_id=id_trainer)
    if not trainer:
        return JSONResponse(status_code=404)
    else:
        return trainer

@router.get(
    "/",
    response_class=JSONResponse,
    response_model=List[TrainerInDB],
    status_code=200,
    responses={
        200: {"description": "event found"},
        401: {"description": "event unauthorized"},
        404: {"description": "event not found"},
    },
)
async def get_all():
    trainers = await trainer_crud.get_all()
    if not trainers:
        return JSONResponse(status_code=404)
    else:
        return trainers

@router.post(
    "/payload",
    response_class=JSONResponse,
    response_model=List[TrainerInDB],
    status_code=200,
    responses={
        200: {"description": "Trainer found"},
        401: {"description": "Trainer unauthorized"},
        404: {"description": "Trainer not found"},
    },
)
async def get_with_payload( *,
        payload: Optional[PayloadTrainer],
        skip_interval: int = 0,
        limit_interval: int = 10):
    payload_transform = payload.dict(exclude_none=True)
    trainers = await trainer_crud.get_with_payload(payload= payload_transform, skip = skip_interval, limit = limit_interval )
    if not trainers:
        return JSONResponse(status_code=404)
    else:
        return trainers 

@router.put(
    "/{id_trainer}",
    response_class=JSONResponse,
    response_model=TrainerInDB,
    status_code=200,
    responses={
        200: {"description": "user found"},
        401: {"description": "user unauthorized"},
        404: {"description": "user not found"},
    },
)
async def update( *,trainer_id: int, trainer: UpdateTrainer):
    trainer = await trainer_crud.get_with_payload(object_id = trainer_id, object_to_update = UpdateTrainer )
    if not trainer:
        return JSONResponse(status_code=404)
    else:
        return trainer

@router.delete(
    "/{id_trainer}",
    response_class=JSONResponse,
    status_code=200,
    responses={
        200: {"description": "user found"},
        401: {"description": "user unauthorized"},
        404: {"description": "user not found"},
    },
)
async def delete_by_id( *,id_trainer : int):
    trainer = await trainer_crud.delete_by_id(object_id= id_trainer)
    if not trainer:
        return JSONResponse(status_code=404)
    else:
        return trainer


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