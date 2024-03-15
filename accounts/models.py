from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    short_bio = models.CharField(
        validators=[
            MinLengthValidator(
                255, "Your short bio should be at least 255 characters long"
            )
        ]
    )
