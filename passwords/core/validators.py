import re

from django.core.exceptions import ValidationError


def validate_regex(value):
    try:
        re.compile(value)
    except re.error as ex:
        raise ValidationError(
            "Invalid Regex: %s" % ex
        )
