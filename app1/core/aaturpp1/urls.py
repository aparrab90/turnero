from django.urls import path
from core.aaturpp1.views.category.views import *



app_name = 'turnero'
urlpatterns = [
    path('categoria/list/', category_lis, name='category_list'),


]
