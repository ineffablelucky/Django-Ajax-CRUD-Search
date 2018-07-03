from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import people_list, delete, create, update, search, month_list

urlpatterns = [
    path('', view=people_list, name='people_list'),
    path('update/', view=update, name='update'),
    path('delete/<int:pk>', view=delete, name='delete'),
    path('create/', view=create, name='create'),
    path('search/', view=search, name='search'),
    path('month/', view=month_list, name='month'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
