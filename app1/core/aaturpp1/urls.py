from django.urls import path

from core.aaturpp1.views import myfisrtview

urlpatterns = [
    path('uno/', myfisrtview),
    path('dos/', myfisrtview)

]
