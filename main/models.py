from django.forms import ModelForm

from PhoneReview.models import Model, Review


# Create your models here.
class PhoneForm(ModelForm):
    class Meta:
        model = Model
        fields = '__all__'
        exclude = ['slug']


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        exclude = ['slug']
