from core.models import DynamicPasswordValidator

from django.core.exceptions import ValidationError

# Create your views here.

def validate_password_dynamic(new_pwd):
    validators = DynamicPasswordValidator.objects.filter(is_active=True)
    failed_validators = []

    for validator in validators:
        if not validator.validate_password(new_pwd):
            # raise ValidationError()
            failed_validators.append(validator.identifier)

    if len(failed_validators) > 0:
        failed_validators_fmt = ",".join(failed_validators)
        raise ValidationError("password failed validators: %s" % failed_validators_fmt)
