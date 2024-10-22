from django.db import models

import uuid


class BaseModel(models.Model):
    # uuid
    # uuid = models.UUIDField(
    #     primary_key=True,
    #     editable=False,
    #     default=uuid.uuid5,
    #     db_index=True,
    #     unique=True,
    # )
    
    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
