from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "Covid19"

urlpatterns = [
    # path('', views.Data.as_view(), name="data"),
    path('global/', views.cases, name="data"),
    path('global/page/<page>', views.cases_page, name="page"),
    path('global/page/', views.cases_page1, name="page1"),
    path('global/country/<code>', views.select_code, name="select_code"),
    path('global/country/', views.select_code1, name="select_code1"),
    path('global/deaths/', views.deaths, name="deaths"),
    path('global/deaths/<page>', views.deaths_page, name="deaths_page"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
