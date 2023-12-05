"""
URL configuration for objects project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from objects.views import *

schema_view = get_swagger_view(title='Simulus Object API')

urlpatterns = [
    url(r'^$', schema_view),
    path('admin/', admin.site.urls),
    # path('', include('routers')), Change this router to reflect the one below
    path('objective/', ObjectiveView.as_view()),
    path('labyrinth/', LabyrinthView.as_view()),
    path('roomObjective/', RoomObjectiveView.as_view())
]


"""
Example of router to be used 

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'accounts', AccountViewSet)
urlpatterns = router.urls
"""
