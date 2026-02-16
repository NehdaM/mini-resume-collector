from django.urls import path
from .views import *

urlpatterns = [
    path("resumes/", resumeView),
    path("resumes/<int:pk>/", resumeView)
]