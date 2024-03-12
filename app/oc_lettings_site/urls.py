from django.contrib import admin
from django.urls import path

import oc_lettings_site.views
import lettings.views
import profiles.views

def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('', oc_lettings_site.views.index, name='index'),
    path('lettings/', lettings.views.lettings_index, name='lettings_index'),
    path('lettings/<int:letting_id>/', lettings.views.letting, name='letting'),
    path('profiles/', profiles.views.profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', profiles.views.profile, name='profile'),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
]
