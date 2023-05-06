from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic

from PhoneReview.models import Brand, Model, Review
from main.models import PhoneForm, ReviewForm


# Create your views here.
def redirect_to_index(request):
    return redirect('/index')


class IndexView(generic.ListView):
    model = Brand
    template_name = 'index.html'
    context_object_name = 'all_brands'

    def get_queryset(self):
        return Brand.objects.all()


class ModelListView(generic.ListView):
    model = Model
    template_name = 'model.html'
    context_object_name = 'all_models'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        brand_instance = Brand.objects.get(slug=slug)
        context['brands'] = Brand.objects.all()
        context['brand'] = brand_instance.title
        return context

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return Model.objects.filter(brand__slug=slug)


class ReviewListView(generic.ListView):
    model = Review
    template_name = 'review-list.html'
    context_object_name = 'all_reviews'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        model_instance = Model.objects.get(slug=slug)
        context['news_link'] = model_instance.news_link
        context['model'] = model_instance.title
        return context

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return Review.objects.filter(model__slug__contains=slug)


class ReviewView(generic.DetailView):
    model = Review
    template_name = 'review-detail.html'
    context_object_name = 'review'

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return Review.objects.get(slug=slug)


class AddPhoneView(generic.TemplateView):
    template_name = 'new-phone.html'

    def post(self, request, *args, **kwargs):
        form = PhoneForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:index'))
        else:
            args = {
                'form': form,
                'models': Model.objects.all()
            }
            return render(request, self.template_name, args)

    def get(self, request, *args, **kwargs):
        form = PhoneForm()
        models = Model.objects.all()
        args = {
            'form': form,
            'models': models
        }
        return render(request, self.template_name, args)


class AddReviewView(generic.TemplateView):
    template_name = 'new-review.html'

    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:index'))
        else:
            args = {
                'form': form,
                'models': Review.objects.all()
            }
            return render(request, self.template_name, args)

    def get(self, request, *args, **kwargs):
        form = ReviewForm()
        models = Review.objects.all()
        args = {
            'form': form,
            'models': models
        }
        return render(request, self.template_name, args)
