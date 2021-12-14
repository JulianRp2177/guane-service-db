from typing import List
from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.event_x_user import EventXUser
from app.schemas.event_x_user import CreateEventXUser, UpdateEventXUser


class CRUDEventXUser(CRUDBase[EventXUser, CreateEventXUser, UpdateEventXUser]):
    ...


event_x_user_crud = CRUDEventXUser(EventXUser)