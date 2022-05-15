from hashlib import blake2b
from django.db import models
from django.forms import SlugField
from django.contrib.auth import get_user_model
from django.utils.text import slugify

# Create your models here.

## getting the user Model
User = get_user_model()

## gender chioces
GENDER = (
    ("Male", "Male"),
    ("Female", "Female"),
)



## survey instance
class Survey(models.Model):
    ## survey created SA
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    ##name of survey
    name = models.CharField(max_length=100, unique=True)
    ## creation and update timestamps
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    #survey slug for suvey link
    slug = models.SlugField(null=True, blank=True)
    ## returning survey in 
    ## human readable format
    def __str__(self) -> str:
        return self.name
    ## creating slug for the survey instance
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}")
        super().save(*args, **kwargs)


## survey fields
class SurveyResponse(models.Model):
    ## survey instance
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="fields")
    ##fields
    about_you = models.TextField(max_length=200)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    gender = models.CharField(choices=GENDER, max_length=10)

    ##
    date_submited = models.DateTimeField(auto_now_add=True)
    ## returning survey in 
    ## human readable format
    def __str__(self) -> str:
        return str(self.survey)