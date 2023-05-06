from django.contrib import admin

from PhoneReview.models import Brand, Model, Review

# Register your models here.
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Review)
