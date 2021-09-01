from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_user.jpg', upload_to='profile_pics')
    branch = models.CharField(max_length=40, default='Engineering')
    stream = models.CharField(max_length=40, default='Engineering')
    year_of_joining = models.PositiveIntegerField(default=current_year(),
                                        validators=[MinValueValidator(1994), max_value_current_year])

    def __str__(self):
        return f'{self.user.username} Profile'

    """def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if(img.height>300 or img.width>300):
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)"""

    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'pk': self.pk})
