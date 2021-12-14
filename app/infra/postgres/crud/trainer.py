from typing import List
from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.trainer import Trainer
from app.schemas.trainer import CreateTrainer, UpdateTrainer


class CRUDTrainer(CRUDBase[Trainer, CreateTrainer, UpdateTrainer]):
    ...

trainer_crud = CRUDTrainer(Trainer)

