from authentication.services import validate_password_dynamic

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def set_password(self, raw_password):
        import ipdb; ipdb.set_trace(context=8)
        validate_password_dynamic(raw_password)
        return super().set_password(raw_password)
