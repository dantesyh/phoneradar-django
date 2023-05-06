from django.urls import path

from main import views

urlpatterns = [
    path('', views.redirect_to_index, name='redirect-to-index'),
    path('index/', views.IndexView.as_view(), name='index'),
    path('model/<slug:slug>/', views.ModelListView.as_view(), name='model'),
    path('review/<slug:slug>/', views.ReviewListView.as_view(), name='review'),
    path('review-detail/<slug:slug>/', views.ReviewView.as_view(), name='review_detail'),
    path('new-phone/', views.AddPhoneView.as_view(), name='new_phone'),
    path('new-review/', views.AddReviewView.as_view(), name='new_review')
]
