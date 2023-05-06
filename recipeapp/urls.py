
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('recipeScrapping', views.recipeScrapping, name='recipeScrapping'),
    path('<int:id>/', views.recipeDetail, name='recipe_details'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
