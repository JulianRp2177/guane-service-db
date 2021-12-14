from fastapi import APIRouter

from app.api.endpoints import (
    root,
    trainer,
    user,
    event,
    event_x_user,
    site
)

api_router = APIRouter()

api_router.include_router(root.router)
api_router.include_router(trainer.router, prefix="/trainer", tags=["Trainer"])
api_router.include_router(user.router, prefix="/user", tags=["User"])
api_router.include_router(site.router, prefix="/site", tags=["Site"])
api_router.include_router(event.router, prefix="/event", tags=["Event"])
api_router.include_router(event_x_user.router, prefix="/event_x_user", tags=["Event X User"])