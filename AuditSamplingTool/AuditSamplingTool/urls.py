from django.contrib import admin
from django.urls import path
from simple_sampling.views import load_page, run_sample
from home.views import home

urlpatterns = [
    path('admin-for-site-oaw52hjfpoq234tebgv89sdv351624122', admin.site.urls),
    path('simple_sampling/', load_page),
    path('simple_sampling/run_sample/', run_sample),
    path('', home, name='home')
]
