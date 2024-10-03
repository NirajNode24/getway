from rest_framework.routers import DefaultRouter
from .views import UserViewset

router = DefaultRouter()
router.register(r'user', UserViewset, basename='kill')

urlpatterns = router.urls