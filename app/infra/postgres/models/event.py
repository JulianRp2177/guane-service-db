from tortoise import fields, models
from tortoise.fields.base import SET_NULL

class Event(models.Model):
    name = fields.CharField(max_length=255)
    meeting_time = fields.CharField(max_length=255)
    description = fields.CharField(max_length=255)
    reservation = fields.BooleanField()
    quantity = fields.IntField()
    trainer = fields.ForeignKeyField(
        "models.Trainer",
        related_name="trainer",
        on_delete=SET_NULL,
        null=True,
    )
    site = fields.ForeignKeyField(
        "models.Site",
        related_name="site",
        on_delete=SET_NULL,
        null=True,
    )

    