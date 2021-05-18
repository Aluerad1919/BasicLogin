from django.urls import path, include
from.import views, models
urlpatterns = [
    path('', views.index),
    path('success', views.success),
    path('register', views.register),
    path('log', views.log),
    path('destory/<int:val>', views.delete),
    path('logout', views.logout),

]