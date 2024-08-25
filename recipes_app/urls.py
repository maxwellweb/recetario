from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RecipeViewSet, IngredientViewSet, CommentViewSet, FavoriteViewSet, RatingViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'recipes', RecipeViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'favorites', FavoriteViewSet)
router.register(r'ratings', RatingViewSet)

urlpatterns = router.urls
