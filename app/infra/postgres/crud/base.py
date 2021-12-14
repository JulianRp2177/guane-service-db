from datetime import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel

from app.crud.base import ICrudBase

ModelType = TypeVar("ModelType", bound=Any)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(ICrudBase[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    async def get_with_payload(
        self,
        *,
        payload: dict = None,
        skip: int = 0,
        limit: int = 10
    ) -> List:
        if payload:
            model = (
                await self.model.filter(**payload)
                .offset(skip)
                .limit(limit)
                .all()
                .values()
            )
        else:
            model = (
                await self.model.all()
                .offset(skip)
                .limit(limit)
                .values()
            )
        return model

    async def get_all(
        self,
    ) -> List:
        model = (
            await self.model.all()
            .values()
        )
        return model

    async def get_by_id(self, *, object_id: int):
        model = await self.model.filter(id=object_id).first().values()
        if model:
            return model
        else:
            return None

    async def create(self, *, object_to_create: CreateSchemaType):
        object_to_create = object_to_create.dict()
        try:
            model = self.model(**object_to_create)
            await model.save()
        except Exception as e:
            print(e)
        return model

    async def update(
        self, *, object_id: int, object_to_update: UpdateSchemaType):
        object_to_update = object_to_update.dict(exclude_none=True)
        model = await self.model.filter(id=object_id).update(**object_to_update)
        if model:
            update_model = await self.model.filter(id=object_id).first().values()
            model_m = self.model(**update_model)
            update_fields = list(update_model.keys())
            await model_m.save(update_fields=update_fields)
            return update_model
        return None
    
    async def delete_by_id(self, *, object_id: int) -> int:
        
        model = await self.model.filter(id=object_id).first().delete()
        if model:
            return model
        else:
            return None
        
    async def counter(self, payload: dict):
        if payload:
            count = await self.model.filter(**payload).all().count()
        else:
            count = await self.model.all().count()
        return count