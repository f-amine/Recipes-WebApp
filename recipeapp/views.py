from django.http import JsonResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup



def home(request):
    # sliced_data = data[:5]
    return render(request, 'index.html', {'data':data})



def recipeScrapping():
    url = 'https://www.simplyrecipes.com/quick-dinner-recipes-5091422'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the container that holds all the Explore Cuisine cards
    container = soup.find('div', {'class': 'loc fixedContent'})
    recipes = []
    # Iterate through each card and extract the information you need
    for card in container.find_all('a', {'class': 'comp mntl-card-list-items mntl-document-card mntl-card card card--no-image'}):
        recipe_name = card.find('span', {'class': 'card__title-text'}).text.strip()
        time_needed = card.find('span', {'class': 'comp meta-text--recipe meta-text'})
        if time_needed:
            time_needed_text = time_needed.find('span', {'class': 'meta-text__text'}).text.strip()
        else:
            time_needed_text = None

        image_div = card.find('div', {'class': 'card__media mntl-universal-image universal-image__container'})
        image_url = image_div.find('img').get('data-src')

        recipe_url = card.get('href')

        recipe_page = requests.get(recipe_url)
        recipe_soup = BeautifulSoup(recipe_page.content, 'html.parser')

        # Extract the ingredients and instructions from the recipe page
        ingredients = recipe_soup.find('ul', {'class': 'structured-ingredients__list text-passage'})

        if ingredients:
            ingredients_list = []
            # Combine the ingredients and instructions into a single string
            for ingredient in ingredients.find_all('li', {'class': 'structured-ingredients__list-item'}):
                ingredient_name_tag = ingredient.find('span', {'data-ingredient-name': True})
                ingredient_quantity_tag = ingredient.find('span', {'data-ingredient-quantity': True})
                ingredient_unit_tag = ingredient.find('span', {'data-ingredient-unit': True})
                #
                ingredient_name = ingredient_name_tag.text.strip() if ingredient_name_tag else ""
                ingredient_quantity = ingredient_quantity_tag.text.strip() if ingredient_quantity_tag else ""
                ingredient_unit = ingredient_unit_tag.text.strip() if ingredient_unit_tag else ""
                ingredients_list.append(f"{ingredient_quantity} {ingredient_unit} {ingredient_name}")
        else:
            ingredients_list = None

        instructions = recipe_soup.find('ol', {'class': 'comp mntl-sc-block-group--OL mntl-sc-block mntl-sc-block-startgroup'})
        if instructions:
            instructions_list = []
            for step in instructions.find_all('li', {'class': 'comp mntl-sc-block-group--LI mntl-sc-block mntl-sc-block-startgroup'}):
                instructions_list.append(step.text.strip())
        else:
            instructions_list = None

        # Combine all the data into a dictionary and add it to the list of recipes
        recipe = {
            'id': len(recipes) + 1,
            'title': recipe_name,
            'time_needed': time_needed_text,
            'url': recipe_url,
            'image_url': image_url,
            'ingredients': ingredients_list,
            'instructions': instructions_list
        }
        recipes.append(recipe)    
    return recipes

data = []
data = recipeScrapping()

def recipeDetail(request, id):
    print('hh')
    for obj in data:
        if obj['id'] == id:
            return render(request, 'post-details.html', {'obj':obj})
        
    