from typing import List, Optional
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from app.infra.postgres.crud.event_x_user import event_x_user_crud
from app.schemas.event_x_user import CreateEventXUser, UpdateEventXUser, EventXUserInDB, PayloadEventXUser



router = APIRouter()

@router.post(
    "/",
    response_class=JSONResponse,
    response_model=EventXUserInDB,
    status_code=200,
    responses={
        200: {"description": "event_x_user found"},
        401: {"description": "event_x_user unauthorized"},
        404: {"description": "event_x_user not found"},
    },
)
async def create_event_x_user(*, event_x_user: CreateEventXUser):

    event_x_user = await event_x_user_crud.create(object_to_create=event_x_user)
    if event_x_user:
        return event_x_user
    else:
        return None

@router.post(
    "/payload",
    response_class=JSONResponse,
    response_model=List[EventXUserInDB],
    status_code=200,
    responses={
        200: {"description": "EventXUser found"},
        401: {"description": "EventXUser unauthorized"},
        404: {"description": "EventXUser not found"},
    },
)
async def get_with_payload( *,
        payload: Optional[PayloadEventXUser],
        skip_interval: int = 0,
        limit_interval: int = 10):
    payload_transform = payload.dict(exclude_none=True)
    events = await event_x_user_crud.get_with_payload(payload= payload_transform, skip = skip_interval, limit = limit_interval )
    if not events:
        return JSONResponse(status_code=404)
    else:
        return events 

@router.get(
    "/{id_event_x_user}",
    response_class=JSONResponse,
    response_model=EventXUserInDB,
    status_code=200,
    responses={
        200: {"description": "event_x_user found"},
        401: {"description": "event_x_user unauthorized"},
        404: {"description": "event_x_user not found"},
    },
)
async def get_by_id(*, id_event_x_user: int):
    event_x_user = await event_x_user_crud.get_by_id(object_id=id_event_x_user)
    if not event_x_user:
        return JSONResponse(status_code=404)
    else:
        return event_x_user

@router.get(
    "/",
    response_class=JSONResponse,
    response_model=List[EventXUserInDB],
    status_code=200,
    responses={
        200: {"description": "event found"},
        401: {"description": "event unauthorized"},
        404: {"description": "event not found"},
    },
)
async def get_all():
    events_x_users = await event_x_user_crud.get_all()
    if not events_x_users:
        return JSONResponse(status_code=404)
    else:
        return events_x_users

@router.put(
    "/{id_event_x_user}",
    response_class=JSONResponse,
    response_model=EventXUserInDB,
    status_code=200,
    responses={
        200: {"description": "user found"},
        401: {"description": "user unauthorized"},
        404: {"description": "user not found"},
    },
)
async def update( *,id_event_x_user: int, in_event_x_user: UpdateEventXUser):
    object_id = {
        "id" : id_event_x_user}
    event_x_user = await event_x_user_crud.update(id = object_id, new_user = in_event_x_user )
    if not event_x_user:
        return JSONResponse(status_code=404)
    else:
        return event_x_user

@router.delete(
    "/{id_event_x_user}",
    response_class=JSONResponse,
    status_code=200,
    responses={
        200: {"description": "user found"},
        401: {"description": "user unauthorized"},
        404: {"description": "user not found"},
    },
)
async def delete_by_id( *,id_event_x_user : int):
    event_x_user = await event_x_user_crud.delete_by_id(object_id= id_event_x_user)
    if not event_x_user:
        return JSONResponse(status_code=404)
    else:
        return event_x_user

""" @router.get(
    "/",
    response_class=JSONResponse,
    response_model=List[EventXUserInDB],
    status_code=200,
    responses={
        200: {"description": "user found"},
        401: {"description": "user unauthorized"},
        404: {"description": "user not found"},
    },
)
async def get_with_pyload( *,
        payload: dict = None,
        skip: int = 0,
        limit: int = 10):
    event_x_users = await event_x_user_crud.get_with_payload(payload = dict, int = 0, int = 10 )
    if not event_x_users:
        return JSONResponse(status_code=404)
    else:
        return event_x_users
 """


