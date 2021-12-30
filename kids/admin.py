from django.contrib import admin
from .models import Kid,Image
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
# Register your models here.




class ImageAdmin(admin.ModelAdmin):
    list_display = ('kid','image_preview','food_group','created_on','updated_on','is_approved','approved_by')
    readonly_fields = ('image_preview','created_on','updated_on','approved_by',)

    def image_preview(self, obj):
        return obj.image_preview

    image_preview.short_description = 'Image Preview'
    image_preview.allow_tags = True
    
    

    
    # def send_mail(self, obj):
    #     subject = 'Important Notification from Alemeno'
    #     message = 'Hi ,Your kid have uploaded the food in unknown category.'
    #     email_from = settings.EMAIL_HOST_USER
    #     recipient_list = ["alemenotest478@gmail.com"]
    #     send_mail(subject, message, email_from, recipient_list)

    def save_model(self, request, obj, form, change):
        if obj.is_approved:
            obj.approved_by = request.user
            super().save_model(request, obj, form, change)
        else:
           obj.approved_by = None
           super().save_model(request, obj, form, change)
    

admin.site.register(Kid)

admin.site.register(Image,ImageAdmin)



