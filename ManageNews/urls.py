from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "ManageNews"

urlpatterns = [
    path('add/', views.AddNews.as_view(), name="addNews"),
    path('add/category/', views.addCategoryNews, name="addCategoryNews"),
    path('list/', views.list_news, name="list_news"),
    path('update/<news_id>', views.update_news.as_view(), name="update_news"),
    path('update/', views.update_news.as_view(), name="update_news_put"),
    path('detail/<news_id>', views.detail_news, name="detail_news"),
    path('search/', views.search, name="search"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
