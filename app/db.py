import logging  # new

from fastapi import FastAPI
from tortoise import Tortoise, run_async  # updated
from tortoise.contrib.fastapi import register_tortoise

from app.config import settings

ENVIRONMENT = settings.ENVIRONMENT

log = logging.getLogger(__name__)  # new



def init_db(app: FastAPI) -> None:
        register_tortoise(
            app,
            db_url=settings.DATABASE,
            modules={"models": ["app.infra.postgres.models"]},
            generate_schemas=True,
            add_exception_handlers=True,
        )


async def generate_schema() -> None:
    log.info("Initializing Tortoise...")
    await Tortoise.init(
        db_url=settings.DATABASE, modules={"models": ["app.infra.postgres.models"]},
    )
    log.info("Generating database schema via Tortoise...")
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()


if __name__ == "__main__":
    run_async(generate_schema())
