
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.recipe_list, name='home'),
    path('login/', views.login,name='login'),
    path('signup/', views.signUp,name='signup'),
    path('recipeScrapping', views.recipeScrapping, name='recipeScrapping'),
    path('<int:id>/', views.recipeDetail, name='recipe_details'),
    path('addComment', views.addComment, name='addComment'),
    path('logout/', views.logOut, name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
