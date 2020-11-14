import re

from django.db import models

from core.validators import validate_regex


class DynamicPasswordValidator(models.Model):
    identifier = models.CharField(
        max_length=255
    )
    description = models.TextField()
    expression = models.CharField(
        max_length=255,
        validators=(validate_regex,)
    )
    is_active = models.BooleanField(default=False)

    def validate_password(self, pwd):
        return re.match(self.expression, pwd) is not None
