from typing import List
from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.site import Site
from app.schemas.site import CreateSite, UpdateSite


class CRUDSite(CRUDBase[Site, CreateSite, UpdateSite]):
    ...


site_crud = CRUDSite(Site)