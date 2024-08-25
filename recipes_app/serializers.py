from rest_framework import serializers
from .models import User, Recipe, Ingredient, RecipeIngredient, Comment, Favorite, Rating

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'created_at', 'updated_at']

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']

class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()

    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity']

class RecipeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    recipe_ingredients = RecipeIngredientSerializer(many=True)
    comments = serializers.StringRelatedField(many=True)

    class Meta:
        model = Recipe
        fields = ['id', 'user', 'title', 'description', 'instructions', 'recipe_ingredients', 'comments', 'created_at', 'updated_at']

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'created_at']

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['user', 'recipe']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'recipe', 'user', 'rating', 'created_at']
