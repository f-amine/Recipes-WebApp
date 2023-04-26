from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from users.models import User
import jwt
from rest_framework.decorators import api_view
from .models import Recipe, Ingredient, Comment, Rating
from .serializers import RecipeSerializer, IngredientSerializer, CommentSerializer, RatingSerializer

# Create your views here.

#Crud for recipe
@api_view(['GET'])
def recipeList(request):
    recipe = Recipe.objects.all()
    serializer = RecipeSerializer(recipe, many=True)
    data = {
        'data': serializer.data,
        'message': 'recipe listed successfully',
        'status': 200
    }
    return JsonResponse(data)

@api_view(['GET'])
def recipeId(request,pk):
    recipe = Recipe.objects.get(id=pk)
    serializer = RecipeSerializer(recipe, many=True)
    data = {
        'data': serializer.data,
        'message': 'recipe listed successfully',
        'status': 200
    }
    return JsonResponse(data)

@api_view(['POST'])
def recipeCreate(request):
    token = request.data['jwt']
    if not token:
        return JsonResponse(({'message' : 'Only admins can add recipes','status':401}))
    try:
        payload = jwt.decode(token,'PLEASE WORK',algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return JsonResponse(({'message' : 'Only admins can add recipes','status':401}))
    if not payload['role']== 'admin':
        return JsonResponse(({'message' : 'Only admins can add recipes','status':401}))
    user = User.objects.get(id=payload['id'])
    request.data['user'] = user.id
    serializer = RecipeSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        recipe = serializer.save(user=user)
    else:
        return JsonResponse(({'message' : 'Invalid Data','status':400}))
    return JsonResponse(({'message' : 'Recipe added successfully','status':200, 'complexe_id': recipe.id}))

@api_view(['POST'])
def recipeUpdate(request, pk):
    token = request.data['jwt']
    if not token:
        return JsonResponse(({'message' : 'Only admins can add recipes','status':401}))
    try:
        payload = jwt.decode(token,'PLEASE WORK',algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return JsonResponse(({'message' : 'Only admins can add recipes','status':401}))
    if not payload['role']== 'admin':
        return JsonResponse(({'message' : 'Only admins can add recipes','status':401}))
    user = User.objects.get(id=payload['id'])
    request.data['user'] = user.id
    recipe = Recipe.objects.get(id=pk)
    serializer = RecipeSerializer(instance=recipe, data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
    else:
        return JsonResponse(({'message' : 'Invalid Data','status':400}))
    return JsonResponse(({'message' : 'Recipe updated successfully','status':200}))

@api_view(['DELETE'])
def recipeDelete(request, pk):
    token = request.data['jwt']
    if not token:
        return JsonResponse(({'message' : 'Only admins can add recipes','status':401}))
    try:
        payload = jwt.decode(token,'PLEASE WORK',algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return JsonResponse(({'message' : 'Only admins can add recipes','status':401}))
    if not payload['role']== 'admin':
        return JsonResponse(({'message' : 'Only admins can add recipes','status':401}))
    recipe = Recipe.objects.get(id=pk)
    recipe.delete()
    return JsonResponse(({'message' : 'Recipe deleted successfully','status':200}))

#Crud for ingredient
@api_view(['GET'])
def ingredientList(request):
    ingredient = Ingredient.objects.all()
    serializer = IngredientSerializer(ingredient, many=True)
    data = {
        'data': serializer.data,
        'message': 'ingredient listed successfully',
        'status': 200
    }
    return JsonResponse(data)

@api_view(['GET'])
def ingredientId(request, pk):
    ingredient = Ingredient.objects.get(id=pk)
    serializer = IngredientSerializer(ingredient, many=True)
    data = {
        'data': serializer.data,
        'message': 'ingredient listed successfully',
        'status': 200
    }
    return JsonResponse(data)

@api_view(['POST'])
def ingredientCreate(request):
    token = request.data['jwt']
    if not token:
        return JsonResponse(({'message' : 'Only admins can add ingredients','status':401}))
    try:
        payload = jwt.decode(token,'PLEASE WORK',algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return JsonResponse(({'message' : 'Only admins can add ingredients','status':401}))
    if not payload['role']== 'admin':
        return JsonResponse(({'message' : 'Only admins can add ingredients','status':401}))
    user = User.objects.get(id=payload['id'])
    request.data['user'] = user.id
    serializer = IngredientSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        ingredient = serializer.save(user=user)
    else:
        return JsonResponse(({'message' : 'Invalid Data','status':400}))
    return JsonResponse(({'message' : 'Ingredient added successfully','status':200, 'complexe_id': ingredient.id}))

@api_view(['POST'])
def ingredientUpdate(request, pk):
    token = request.data['jwt']
    if not token:
        return JsonResponse(({'message' : 'Only admins can add ingredients','status':401}))
    try:
        payload = jwt.decode(token,'PLEASE WORK',algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return JsonResponse(({'message' : 'Only admins can add ingredients','status':401}))
    if not payload['role']== 'admin':
        return JsonResponse(({'message' : 'Only admins can add ingredients','status':401}))
    user = User.objects.get(id=payload['id'])
    request.data['user'] = user.id
    ingredient = Ingredient.objects.get(id=pk)
    serializer = IngredientSerializer(instance=ingredient, data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
    else:
        return JsonResponse(({'message' : 'Invalid Data','status':400}))
    return JsonResponse(({'message' : 'Ingredient updated successfully','status':200}))

@api_view(['DELETE'])
def ingredientDelete(request, pk):
    token = request.data['jwt']
    if not token:
        return JsonResponse(({'message' : 'Only admins can add ingredients','status':401}))
    try:
        payload = jwt.decode(token,'PLEASE WORK',algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return JsonResponse(({'message' : 'Only admins can add ingredients','status':401}))
    if not payload['role']== 'admin':
        return JsonResponse(({'message' : 'Only admins can add ingredients','status':401}))
    ingredient = Ingredient.objects.get(id=pk)
    ingredient.delete()
    return JsonResponse(({'message' : 'Ingredient deleted successfully','status':200}))

#Crud for comment

@api_view(['GET'])
def commentList(request):
    comment = Comment.objects.all()
    serializer = CommentSerializer(comment, many=True)
    data = {
        'data': serializer.data,
        'message': 'comment listed successfully',
        'status': 200
    }
    return JsonResponse(data)

@api_view(['GET'])
def commentId(request, pk):
    comment = Comment.objects.get(id=pk)
    serializer = CommentSerializer(comment, many=True)
    data = {
        'data': serializer.data,
        'message': 'comment listed successfully',
        'status': 200
    }
    return JsonResponse(data)

@api_view(['POST'])
def commentCreate(request):
    token = request.data['jwt']
    if not token:
        return JsonResponse(({'message' : 'Only admins can add comments','status':401}))
    try:
        payload = jwt.decode(token,'PLEASE WORK',algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return JsonResponse(({'message' : 'Only admins can add comments','status':401}))
    if not payload['role']== 'client':
        return JsonResponse(({'message' : 'Only admins can add comments','status':401}))
    user = User.objects.get(id=payload['id'])
    request.data['user'] = user.id
    serializer = CommentSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        comment = serializer.save(user=user)
    else:
        return JsonResponse(({'message' : 'Invalid Data','status':400}))
    return JsonResponse(({'message' : 'Comment added successfully','status':200, 'complexe_id': comment.id}))
@api_view(['POST'])
def commentUpdate(request, pk):
    token = request.data['jwt']
    if not token:
        return JsonResponse(({'message' : 'Only admins can add comments','status':401}))
    try:
        payload = jwt.decode(token,'PLEASE WORK',algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return JsonResponse(({'message' : 'Only admins can add comments','status':401}))
    if not payload['role']== 'client':
        return JsonResponse(({'message' : 'Only admins can add comments','status':401}))
    user = User.objects.get(id=payload['id'])
    request.data['user'] = user.id
    comment = Comment.objects.get(id=pk)
    serializer = CommentSerializer(instance=comment, data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
    else:
        return JsonResponse(({'message' : 'Invalid Data','status':400}))
    return JsonResponse(({'message' : 'Comment updated successfully','status':200}))

@api_view(['DELETE'])
def commentDelete(request, pk):
    token = request.data['jwt']
    if not token:
        return JsonResponse(({'message' : 'Only admins can add comments','status':401}))
    try:
        payload = jwt.decode(token,'PLEASE WORK',algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return JsonResponse(({'message' : 'Only admins can add comments','status':401}))
    if not payload['role']== 'client':
        return JsonResponse(({'message' : 'Only admins can add comments','status':401}))
    comment = Comment.objects.get(id=pk)
    comment.delete()
    return JsonResponse(({'message' : 'Comment deleted successfully','status':200}))

#views.py

@api_view(['GET'])
def recipeComments(request, pk):
    comments = Comment.objects.filter(recipe=pk)
    serializer = CommentSerializer(comments, many=True)
    data = {
        'data': serializer.data,
        'message': 'comments listed successfully',
        'status': 200
    }
    return JsonResponse(data)

#Crud for rating

@api_view(['GET'])
def ratingList(request):
    rating = Rating.objects.all()
    serializer = RatingSerializer(rating, many=True)
    data = {
        'data': serializer.data,
        'message': 'rating listed successfully',
        'status': 200
    }
    return JsonResponse(data)

@api_view(['GET'])
def ratingId(request, pk):
    rating = Rating.objects.get(id=pk)
    serializer = RatingSerializer(rating, many=True)
    data = {
        'data': serializer.data,
        'message': 'rating listed successfully',
        'status': 200
    }
    return JsonResponse(data)


@api_view(['GET'])
def recipeRatings(request, pk):
    ratings = Rating.objects.filter(recipe=pk)
    serializer = RatingSerializer(ratings, many=True)
    data = {
        'data': serializer.data,
        'message': 'ratings listed successfully',
        'status': 200
    }
    return JsonResponse(data)
@api_view(['POST'])
def ratingCreate(request):
    token = request.data['jwt']
    if not token:
        return JsonResponse(({'message' : 'Only admins can add ratings','status':401}))
    try:
        payload = jwt.decode(token,'PLEASE WORK',algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return JsonResponse(({'message' : 'Only admins can add ratings','status':401}))
    if not payload['role']== 'client':
        return JsonResponse(({'message' : 'Only admins can add ratings','status':401}))
    user = User.objects.get(id=payload['id'])
    request.data['user'] = user.id
    serializer = RatingSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        rating = serializer.save(user=user)
    else:
        return JsonResponse(({'message' : 'Invalid Data','status':400}))
    return JsonResponse(({'message' : 'Rating added successfully','status':200, 'complexe_id': rating.id}))

@api_view(['POST'])
def ratingUpdate(request, pk):
    token = request.data['jwt']
    if not token:
        return JsonResponse(({'message' : 'Only admins can add ratings','status':401}))
    try:
        payload = jwt.decode(token,'PLEASE WORK',algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return JsonResponse(({'message' : 'Only admins can add ratings','status':401}))
    if not payload['role']== 'client':
        return JsonResponse(({'message' : 'Only admins can add ratings','status':401}))
    user = User.objects.get(id=payload['id'])
    request.data['user'] = user.id
    rating = Rating.objects.get(id=pk)
    serializer = RatingSerializer(instance=rating, data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
    else:
        return JsonResponse(({'message' : 'Invalid Data','status':400}))
    return JsonResponse(({'message' : 'Rating updated successfully','status':200}))

@api_view(['DELETE'])
def ratingDelete(request, pk):
    token = request.data['jwt']
    if not token:
        return JsonResponse(({'message' : 'Only admins can add ratings','status':401}))
    try:
        payload = jwt.decode(token,'PLEASE WORK',algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return JsonResponse(({'message' : 'Only admins can add ratings','status':401}))
    if not payload['role']== 'client':
        return JsonResponse(({'message' : 'Only admins can add ratings','status':401}))
    rating = Rating.objects.get(id=pk)
    rating.delete()
    return JsonResponse(({'message' : 'Rating deleted successfully','status':200}))

