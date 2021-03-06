from django.urls import include, path
from rest_framework.routers import SimpleRouter

from board.views import BoardViewSet

app_name = 'board'

router = SimpleRouter()
router.register('board', BoardViewSet, basename='board')

urlpatterns = [
    path('', include((router.urls))),
]