from tortoise import fields, models


class Site(models.Model):
    name = fields.CharField(unique=True, max_length=255)
    direction = fields.TextField()
    description = fields.TextField()
    schedule = fields.CharField(unique=True, max_length=255)