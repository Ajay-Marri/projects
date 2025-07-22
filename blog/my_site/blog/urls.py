from django.urls import path
from . import views
from .views import (
    AboutPageView,
    ContactPageView,
    PrivacyPolicyView,
    TermsOfUseView,
)

urlpatterns = [
    path("",views.dashboard.as_view(), name='dashboard'),
    path("posts",views.posts.as_view(), name="posts"),
    path("posts/<str:slug>", views.post_details.as_view(), name='post_details'), #/posts/my-first-post
    path("read-later",views.readlaterview.as_view(),name="read-later"),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('privacy-policy/', PrivacyPolicyView.as_view(), name='privacy-policy'),
    path('terms/', TermsOfUseView.as_view(), name='terms'),
]