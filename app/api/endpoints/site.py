from typing import List, Union, Optional
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from app.infra.postgres.crud.site import site_crud
from app.schemas.site import CreateSite, UpdateSite, SiteInDB, PayloadSite



router = APIRouter()

@router.post(
    "/",
    response_class=JSONResponse,
    response_model=SiteInDB,
    status_code=200,
    responses={
        200: {"description": "site found"},
        401: {"description": "site unauthorized"},
        404: {"description": "site not found"},
    },
)
async def create_event(*, site: CreateSite):

    site = await site_crud.create(object_to_create=site)
    if site:
        return site
    else:
        return None

@router.post(
    "/payload",
    response_class=JSONResponse,
    response_model=List[SiteInDB],
    status_code=200,
    responses={
        200: {"description": "Site found"},
        401: {"description": "Site unauthorized"},
        404: {"description": "Site not found"},
    },
)
async def get_with_payload( *,
        payload: Optional[PayloadSite],
        skip_interval: int = 0,
        limit_interval: int = 10):
    payload_transform = payload.dict(exclude_none=True)
    sites = await site_crud.get_with_payload(payload= payload_transform, skip = skip_interval, limit = limit_interval )
    if not sites:
        return JSONResponse(status_code=404)
    else:
        return sites 

@router.get(
    "/{id_site}",
    response_class=JSONResponse,
    response_model=SiteInDB,
    status_code=200,
    responses={
        200: {"description": "site found"},
        401: {"description": "site unauthorized"},
        404: {"description": "site not found"},
    },
)
async def get_by_id(*, id_site: int):
    site = await site_crud.get_by_id(object_id=id_site)
    if not site:
        return JSONResponse(status_code=404)
    else:
        return site

@router.get(
    "/",
    response_class=JSONResponse,
    response_model=List[SiteInDB],
    status_code=200,
    responses={
        200: {"description": "event found"},
        401: {"description": "event unauthorized"},
        404: {"description": "event not found"},
    },
)
async def get_all():
    sites = await site_crud.get_all()
    if not sites:
        return JSONResponse(status_code=404)
    else:
        return sites

""" @router.get(
    "/",
    response_class=JSONResponse,
    response_model=List[SiteInDB],
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
    sites = await site_crud.get_with_payload(payload = dict, int = 0, int = 10 )
    if not sites:
        return JSONResponse(status_code=404)
    else:
        return sites """

@router.put(
    "/{id_site}",
    response_class=JSONResponse,
    response_model=SiteInDB,
    status_code=200,
    responses={
        200: {"description": "user found"},
        401: {"description": "user unauthorized"},
        404: {"description": "user not found"},
    },
)
async def update( *,site_id: int, site: UpdateSite):
    users = await site_crud.get_with_payload(object_id = site_id, object_to_update = UpdateSite )
    if not users:
        return JSONResponse(status_code=404)
    else:
        return users

@router.delete(
    "/{id_site}",
    response_class=JSONResponse,
    status_code=200,
    responses={
        200: {"description": "user found"},
        401: {"description": "user unauthorized"},
        404: {"description": "user not found"},
    },
)
async def delete_by_id( *,id_site : int):
    site = await site_crud.delete_by_id(object_id= id_site)
    if not site:
        return JSONResponse(status_code=404)
    else:
        return site

