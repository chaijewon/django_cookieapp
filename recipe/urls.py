from django.urls import path
from recipe import views
#URLConf  @app.router('')
urlpatterns=[
    path('',views.recipe_list),
    path('recipe_before/',views.recipe_before),
    path('recipe_detail/',views.recipe_detail)
]