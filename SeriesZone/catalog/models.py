from django.db import models
from django.urls import reverse
from django.core.validators import FileExtensionValidator
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name




class Serial(models.Model):
    name=models.CharField(max_length = 255)
    # second_name = models.CharField(max_length = 225)
    img= models.ImageField(upload_to="image")
    cost=models.PositiveIntegerField()
    category = models.ManyToManyField(Category)
    raiting= models.FloatField()
    description=models.TextField(max_length=260)
    country= models.CharField(max_length = 25)
    age= models.PositiveIntegerField()
    dateOfIssue = models.CharField(max_length=11)
    trailer = models.FileField(upload_to="trailer", validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'webm'])])

    def get_absolute_url(self):
        return reverse('serial_view', kwargs={'serial_pk': self.pk})

    def get_absolute_url_for_buy(self):
        return reverse('buy_form', kwargs={'serial_pk': self.pk})
    
    def __str__(self):
        return self.name

class Season(models.Model):
    number_of_season = models.IntegerField()
    serial = models.ForeignKey(Serial, on_delete=models.CASCADE)


class Series(models.Model):
    number_of_series = models.IntegerField()
    preview = models.ImageField(upload_to='preview')
    name = models.CharField(max_length = 100)
    video = models.FileField(upload_to='video')
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    def __str__(self):
        return self.name #str(self.season.number_of_season + self.number_of_series + self.name +  self.season.serial.name) 
