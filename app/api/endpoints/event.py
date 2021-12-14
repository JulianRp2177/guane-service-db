from typing import List, Optional
from app.infra.postgres.models.event import Event
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from app.infra.postgres.crud.event import event_crud
from app.schemas.event import CreateEvent, UpdateEvent, EventInDB, PayloadEvent



router = APIRouter()

@router.post(
    "/",
    response_class=JSONResponse,
    response_model=EventInDB,
    status_code=200,
    responses={
        200: {"description": "user found"},
        401: {"description": "user unauthorized"},
        404: {"description": "user not found"},
    },
)
async def create_event(*, event: CreateEvent):

    event = await event_crud.create(object_to_create=event)
    if event:
        return event
    else:
        return None

@router.post(
    "/payload",
    response_class=JSONResponse,
    response_model=List[EventInDB],
    status_code=200,
    responses={
        200: {"description": "Event found"},
        401: {"description": "Event unauthorized"},
        404: {"description": "Event not found"},
    },
)
async def get_with_payload( *,
        payload: Optional[PayloadEvent],
        skip_interval: int = 0,
        limit_interval: int = 10):
    payload_transform = payload.dict(exclude_none=True)
    events = await event_crud.get_with_payload(payload= payload_transform, skip = skip_interval, limit = limit_interval )
    if not events:
        return JSONResponse(status_code=404)
    else:
        return events 

@router.get(
    "/",
    response_class=JSONResponse,
    response_model=List[EventInDB],
    status_code=200,
    responses={
        200: {"description": "event found"},
        401: {"description": "event unauthorized"},
        404: {"description": "event not found"},
    },
)
async def get_all():
    events = await event_crud.get_all()
    if not events:
        return JSONResponse(status_code=404)
    else:
        return events


@router.get(
    "/{id_event}",
    response_class=JSONResponse,
    response_model=EventInDB,
    status_code=200,
    responses={
        200: {"description": "event found"},
        401: {"description": "event unauthorized"},
        404: {"description": "event not found"},
    },
)
async def get_by_id(*, id_event: int):
    event = await event_crud.get_by_id(object_id=id_event)
    if not event:
        return JSONResponse(status_code=404)
    else:
        return event

""" @router.get(
    "/",
    response_class=JSONResponse,
    response_model=List[EventInDB],
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
    events = await event_crud.get_with_payload(payload = dict, int = 0, int = 10 )
    if not events:
        return JSONResponse(status_code=404)
    else:
        return events """

@router.put(
    "/{id_user}",
    response_class=JSONResponse,
    response_model=EventInDB,
    status_code=200,
    responses={
        200: {"description": "user found"},
        401: {"description": "user unauthorized"},
        404: {"description": "user not found"},
    },
)
async def update( *,id_event: int, in_event: UpdateEvent):
    object_id = {
        "id" : id_event}
    event = await event_crud.update(id = object_id, new_user = in_event )
    if not event:
        return JSONResponse(status_code=404)
    else:
        return event

@router.delete(
    "/{id_event}",
    response_class=JSONResponse,
    status_code=200,
    responses={
        200: {"description": "user found"},
        401: {"description": "user unauthorized"},
        404: {"description": "user not found"},
    },
)
async def delete_by_id( *,id_event : int):
    event = await event_crud.delete_by_id(object_id= id_event)
    if not event:
        return JSONResponse(status_code=404)
    else:
        return event




