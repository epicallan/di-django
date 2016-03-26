from . import views
from rest_framework.routers import DefaultRouter

app_name = 'spotlight'
router = DefaultRouter()
router.register(r'spotlight', views.SpotlightViewSet)
router.register(r'indicator', views.IndicatorViewSet)
urlpatterns = router.urls
