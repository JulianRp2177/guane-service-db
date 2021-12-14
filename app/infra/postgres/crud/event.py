from typing import List
from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.event import Event
from app.schemas.event import CreateEvent, UpdateEvent


class CRUDEvent(CRUDBase[Event, CreateEvent, UpdateEvent]):
    ...


event_crud = CRUDEvent(Event)