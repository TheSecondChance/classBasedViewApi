from django.contrib import admin
from django.urls import path
from .views import PersonView, PersonDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('person/', PersonView.as_view()),
    path('person/<int:id>/', PersonDetail.as_view()),
]
