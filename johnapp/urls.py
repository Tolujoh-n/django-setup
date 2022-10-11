from django import path
from . import views


urlpatterns = [
    path('', views.index, name="johnapp"),
    path('add-johnapp', views.add_johnapp, name="add-johnapp")
]


