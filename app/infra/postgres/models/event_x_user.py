from tortoise import fields, models
from tortoise.fields.base import SET_NULL

class EventXUser(models.Model):
    event = fields.ForeignKeyField(
        "models.Event",
        related_name="event_x_user",
        on_delete=SET_NULL,
        null=True,
    )
    user = fields.ForeignKeyField(
        "models.User",
        related_name="event_x_user",
        on_delete=SET_NULL,
        null=True,
    )

    class Meta:
        unique_together = ("event_id", "user_id")

        