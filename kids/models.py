from django.db import models
from django.conf import settings
from django.utils.html import mark_safe
from django.core.validators import RegexValidator
from django.core.mail import send_mail
from django.db.models.signals import post_save, pre_save
# Create your models here.


class PhoneValidator:
    phone_regex = RegexValidator(
        regex=r'^\d{10}$',
        message='Phone number must be entered in the format 9999999999. \
            Up to 10 digits')

class Kid(models.Model,PhoneValidator):
    kid_name = models.CharField(max_length=200)
    kid_age = models.IntegerField(default=0)
    parent_phone = models.CharField(
        'Parent Phone No.',
        validators=[PhoneValidator.phone_regex],
        max_length=10
    )
    parent_email = models.EmailField('Parent Email Address', max_length=255)
    def __str__(self):
         return self.kid_name

class Image(models.Model):
    food_group_choice = (
        ('Fruit','Fruit'),
        ('Vegetable','Vegetable'), 
        ('Grain','Grain'), 
        ('Protein','Protein'), 
        ('Dairy','Dairy'), 
        ('Unknown','Unknown')
    )
    kid = models.ForeignKey(Kid, on_delete=models.CASCADE)
    food_group =  models.CharField(
        max_length=30,
        choices= food_group_choice,
        default= food_group_choice[0][0]
    )
    image_url = models.URLField(max_length = 1000)

    @property
    def image_preview(self):
        if self.image_url:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.image_url))
        return ""

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True, null=True)
    
def send_email(sender,instance,**kwargs):
    if instance.food_group=='Unknown':
        subject = 'Important Notification from Alemeno'
        message = 'Hi {}, \nYour kid have uploaded the image in unknown category.\nTeam Alemeno'.format(instance.kid.parent_email)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [instance.kid.parent_email]
        send_mail(subject, message, email_from, recipient_list)

post_save.connect(send_email,sender=Image)