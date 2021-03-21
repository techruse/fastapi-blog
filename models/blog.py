from tortoise.models import Model
from tortoise import fields


class Blog(Model):
    title = fields.CharField(max_length=255)

