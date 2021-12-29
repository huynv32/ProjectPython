from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from ManageNews.models import Category, News
from ManageNews.serializers import NewsSerializer


class AddNews(View):
    def get(self, request):
        category = Category.objects.filter(status=True)
        context = {"category": category}
        return render(request, 'ManageNews/AddNews.html', context)

    def post(self, request):
        news = NewsSerializer(request.POST, request.FILES or None)
        if request.method == "POST":

            news.is_valid();
            # if mimetypes.guess_type(question.cleaned_data['video']).startswith('video'):
            #     print('It is a video')
            # if not question.is_valid() and not answer.is_valid():
            #     return HttpResponse("nhập sai dữ liệu")
            # Using File storage to save file for future converting
            fs = FileSystemStorage()

            file_audio = fs.save("audio/" + news.cleaned_data['audio'].name, news.cleaned_data['audio'])
            audio_file_url = fs.url(file_audio)
            file_video = fs.save("video/" + news.cleaned_data['video'].name, news.cleaned_data['video'])
            video_file_url = fs.url(file_video)
            news.cleaned_data['audio'] = audio_file_url
            news.cleaned_data['video'] = video_file_url
            # if request.user.is_authenticated():
            #     user_id = request.user.id
            # else:
            user_id = User.objects.get(username="huy")
            news.cleaned_data['category_id'] = request.POST.get("category_id")
            try:
                news.save()
            except Exception as e:
                print(e)

            listNews = News.objects.all()
            context = {
                "list": listNews
            }

            return render(request, 'ManageNews/ListNews.html', context)


def addCategoryNews(request):
    if request.method == "POST":
        try:
            q = Category(name=request.POST.get("name"), status=True)
            q.save()
        except Exception as e:
            print(e)
        category = Category.objects.filter(status=True)
        context = {"category": category}
        return render(request, 'ManageNews/ListCategory.html', context)


def list_news(request):
    listNews = News.objects.all()
    context = {
        "list": listNews
    }

    return render(request, 'ManageNews/ListNews.html', context)


class update_news(View):
    def get(self, request, news_id):
        category = Category.objects.filter(status=True)
        news = News.objects.get(pk=news_id)
        context = {
            "category": category,
            "news": news
        }
        return render(request, 'ManageNews/UpdateNews.html', context)

    def post(self, request):
        if request.method == "POST":

            id = request.POST.get("id")
            data = News.objects.get(id=id)
            form = NewsSerializer(request.POST, request.FILES, instance=data)
            if form.is_valid():
                form.save()
                return redirect("/news/list/")
            else:
                HttpResponse("lỗi r")
                # return render(request, 'ManageNews/ListNews.html', context)


def detail_news(request, news_id):
    news = News.objects.get(pk=news_id)
    category = Category.objects.get(pk=news.category_id_id)
    context = {
        "news": news,
        "category": category
    }
    return render(request, 'ManageNews/Detail_News.html', context)


def search(request):
    input = request.POST.get("input")
    select = int(request.POST.get("select"))
    print(select)
    listNews = News.objects.all()
    if select == 1:
        listNews = News.objects.filter(title__contains=input)
    if select == 2:
        listNews = News.objects.filter(content__contains=input)

    context = {
        "list": listNews
    }

    return render(request, 'ManageNews/ListNews.html', context)
