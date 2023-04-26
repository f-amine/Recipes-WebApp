from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('recipe-list/', views.recipeList, name='recipe-list'),
    path('recipe-id/<int:id>/', views.recipeId, name='recipe-id'),
    path('recipe-create/', views.recipeCreate, name='recipe-create'),
    path('recipe-update/<int:id>/', views.recipeUpdate, name='recipe-update'),
    path('recipe-delete/<int:id>/', views.recipeDelete, name='recipe-delete'),
    path('ingredient-list/', views.ingredientList, name='ingredient-list'),
    path('ingredient-id/<int:id>/', views.ingredientId, name='ingredient-id'),
    path('ingredient-create/', views.ingredientCreate, name='ingredient-create'),
    path('ingredient-update/<int:id>/', views.ingredientUpdate, name='ingredient-update'),
    path('ingredient-delete/<int:id>/', views.ingredientDelete, name='ingredient-delete'),
    path('comment-list/', views.commentList, name='comment-list'),
    path('comment-id/<int:id>/', views.commentId, name='comment-id'),
    path('recipe-comments/<int:id>/', views.recipeComments, name='recipe-comments'),
    path('comment-create/', views.commentCreate, name='comment-create'),
    path('comment-update/<int:id>/', views.commentUpdate, name='comment-update'),
    path('comment-delete/<int:id>/', views.commentDelete, name='comment-delete'),
    path('rating-list/', views.ratingList, name='rating-list'),
    path('rating-id/<int:id>/', views.ratingId, name='rating-id'),
    path('recipe-ratings/<int:id>/', views.recipeRatings, name='recipe-ratings'),
    path('rating-create/', views.ratingCreate, name='rating-create'),
    path('rating-update/<int:id>/', views.ratingUpdate, name='rating-update'),
    path('rating-delete/<int:id>/', views.ratingDelete, name='rating-delete'),
    ]