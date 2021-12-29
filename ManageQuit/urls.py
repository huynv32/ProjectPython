from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "ManageQuit"

urlpatterns = [
    path('add/', views.ManageQuit.as_view(), name="add"),
    # path('detail/<question_id>', views.ManageQuit.as_view(), name="detail"),
    path('detail/<question_id>', views.detail, name="detail"),
    path('make_quit/', views.MakeQuit.as_view(), name="quit"),
    path('page/', views.MakeQuit.as_view(), name="make_quit"),
    path('question/', views.list_question, name="listQuestion"),
    path('login/', views.LoginClass.as_view(), name="login"),
    path('add/category/', views.addCategory, name="addCategory"),
    path('category/', views.category_manage.as_view(), name="get"),
    path('category/delete/<category_id>', views.delete_category, name="delete_category"),
    path('category/update/<category_id>', views.update_category.as_view(), name="update_category"),
    path('category/update', views.update_category.as_view(), name="update_category"),
    path('question/update/<question_id>', views.update_question.as_view(), name="update_question"),
    path('question/update/', views.update_question.as_view(), name="update_question"),
    path('abc', views.update_question.as_view(), name="abc"),
    path('select/<category_id>', views.select_category, name="select"),
    path('search/', views.search, name="search"),
    path('result/', views.result, name="result"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
