from tortoise import fields, models


class Trainer(models.Model):
    username = fields.CharField(unique=True, max_length=255)
    password = fields.TextField()
    document = fields.CharField(unique=True, max_length=255)
    speciality = fields.CharField(max_length=255)
    email = fields.CharField(unique=True, max_length=255)
    phone = fields.CharField(max_length=255)