import os
import time
from builtins import print
from datetime import datetime
from random import random

from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from setuptools.glob import magic_check

# Create your views here.
from django.views import View

from ManageQuit.models import Category, Question, Answer, Result
from ManageQuit.serializers import QuestionSerializer, AnswerSerializer, CategorySerializer
import mimetypes


class ManageQuit(LoginRequiredMixin, View):
    def get(self, request):
        category = Category.objects.filter(status=True)
        context = {"category": category}
        return render(request, 'ManageQuit/AddQuestion.html', context)

    def post(self, request):

        question = QuestionSerializer(request.POST, request.FILES or None)
        # answer = AnswerSerializer(request.POST, request.FILES or None)
        answer_get = request.POST.getlist('answer')
        choice = request.POST.get('choice')
        print(choice)
        if request.method == "POST":
            question.is_valid();
            fs = FileSystemStorage()
            file_audio = fs.save("audio/" + question.cleaned_data['audio'].name, question.cleaned_data['audio'])
            audio_file_url = fs.url(file_audio)
            file_video = fs.save("video/" + question.cleaned_data['video'].name, question.cleaned_data['video'])
            video_file_url = fs.url(file_video)
            question.cleaned_data['audio'] = audio_file_url
            question.cleaned_data['video'] = video_file_url
            # user_id = request.user.id
            # if not user_id:
            #     user_id = User.objects.get(username="huy")
            # question.cleaned_data['user_id'] = user_id
            # question.cleaned_data['dateCreated'] = datetime.now()
            question.cleaned_data['category_id'] = 2
            try:
                question.save()
            except Exception as e:
                print(e)

            listQuestion = Question.objects.all()
            obj = Question.objects.latest('id')
            for idx, val in enumerate(answer_get):
                if idx + 1 == int(choice):
                    answer = Answer(question_id_id=obj.id, content=val, value=True, status=True)
                else:
                    answer = Answer(question_id_id=obj.id, content=val, value=False, status=True)
                try:
                    answer.save()
                except:
                    HttpResponse("Cant not insert Answer")
            # Converting to mp3 here
            context = {
                "list": listQuestion
            }
            return render(request, 'ManageQuit/ListQuestion.html', context)


# upstream = os.path.dirname(os.path.dirname(os.path.dirname(
#               os.path.abspath(__file__))))
#           path = os.path.join(upstream, 'audio', question.cleaned_data['audio'].name)
#           mp3_filename = '.'.join([question.cleaned_data['audio'].name.split('.')[0], 'mp3'])
#           new_path = os.path.join(
#               upstream, 'audio', mp3_filename)


class LoginClass(View):
    def get(self, request):
        return render(request, 'ManageQuit/login.html')

    def post(self, request):

        username = request.POST.get("username")
        password = request.POST.get("password")
        if not username and not password:
            HttpResponse("username and password can not empty")
            # return render(request,"bạn ")
        my_user = authenticate(username=username, password=password)
        if my_user is None:
            return HttpResponse("đăng nhập sai ")
        login(request, my_user)
        mes = "Đăng nhập thành công"
        return redirect('/question/')


def addCategory(request):
    if request.method == "POST":
        try:
            q = Category(name=request.POST.get("name"), status=True)
            q.save()
        except Exception as e:
            print(e)
        category = Category.objects.filter(status=True)
        context = {"category": category}
        return render(request, 'ManageQuit/ListCategory.html', context)


class category_manage(View, LoginRequiredMixin):
    def get(self, request):
        category = Category.objects.filter(status=True)
        if not category:
            HttpResponse("List Category is Empty")
        context = {"category": category}
        return render(request, 'ManageQuit/ListCategory.html', context)

    def put(self, request, id):
        return render(request, 'ManageQuit/ListCategory.html')


def delete_category(request, category_id):
    cate = Category.objects.get(pk=category_id)
    try:
        cate.delete()
    except:
        pass
    category = Category.objects.filter(status=True)
    context = {"category": category}
    return render(request, 'ManageQuit/ListCategory.html', context)


class update_category(View):
    def get(self, request, category_id):
        try:
            cate = Category.objects.get(pk=category_id)
        except:
            HttpResponse("Category not exist")
        context = {"category": cate}
        return render(request, 'ManageQuit/UpdateCategory.html', context)

    def post(self, request):
        try:
            id = request.POST.get("id")
            cate = Category.objects.get(pk=id)
            cate.name = request.POST.get("name")
        except:
            HttpResponse("Name category is empty")
        cate.save()
        category = Category.objects.filter(status=True)
        context = {"category": category}
        return render(request, 'ManageQuit/ListCategory.html', context)


class DetailAndUpdateQuit(View):

    def get(self, request, question_id, *args, **kwargs):
        print(question_id)
        question = Question.objects.get(id=question_id)
        list_answer = Answer.objects.filter(question_id=question_id)
        context = {"question": question, "answer": list_answer}
        return render(request, 'ManageQuit/DetailQuestion.html', context)


def detail(request, question_id):
    print(question_id)
    try:
        question = Question.objects.get(id=question_id)
        list_answer = Answer.objects.filter(question_id_id=question_id)
    except:
        HttpResponse("Question không tồn tại")
    context = {"question": question, "answer": list_answer}
    return render(request, 'ManageQuit/DetailQuestion.html', context)


total = 0
list = {}


class MakeQuit(LoginRequiredMixin, View):

    def get(self, request):
        try:
            global total
            global list
            total = 0
            list = None
            list = Question.objects.all()
            # list = Question.objects.all().order_by('?')[:10]
            question = list[0]
            list_answer = Answer.objects.filter(question_id_id=question.id)
        except:
            HttpResponse("Question không tồn tại")
        page = 1
        context = {"question": question, "answer": list_answer, "mes": "1/10", "page": page, "total": total}
        return render(request, 'ManageQuit/DetailQuestion.html', context)

    def post(self, request):
        if request.method == "POST":
            global total
            question_id = request.POST.get("question_id")
            page = request.POST.get("page")
            new_page = int(page) + 1
            answer_get = request.POST.get('answer')
            answer = Answer.objects.filter(question_id_id=question_id)
            if request.user:
                user_id = request.user
            for idx, val in enumerate(answer):
                if idx + 1 == int(answer_get):
                    if val.value == True:
                        total = total + 1
                        print("**** ddusng ")
                        print(total)
            if new_page == 11:
                r = Result(user_id=user_id, scope=total)
                r.save()
                result_all = Result.objects.all()
                id = request.user.id
                print(id)
                # result_all = Result.objects.exclude(user_id=2)
                result_all = Result.objects.all()
                # filter(Q(user_id_id__in=1))
                list_scope = []
                list_user = []
                for o in result_all:
                    list_scope.append(o.scope)
                    list_user.append(o.user_id.username)
                context = {
                    "list_scope": list_scope,
                    "list_user": list_user,
                    "mes": "số điểm của bạn là :" + str(total)
                }
                return render(request, 'ManageQuit/Result.html', context)
            try:
                question = list[new_page]
                list_answer = Answer.objects.filter(question_id_id=question.id)
            except:
                HttpResponse("Question không tồn tại")
            mes = str(new_page) + "/10"
            print(new_page)
            context = {"question": question, "answer": list_answer, "mes": mes, "page": new_page, "total": total}
            return render(request, 'ManageQuit/DetailQuestion.html', context)


def list_question(request):
    try:
        listQuestion = Question.objects.all()
        category = Category.objects.filter(status=True)
    except:
        HttpResponse("List question Empty ")

    context = {
        "list": listQuestion,
        "category": category
    }

    return render(request, 'ManageQuit/ListQuestion.html', context)


class update_question(View):
    def get(self, request, question_id):
        question = Question.objects.get(pk=question_id)
        anwser = Answer.objects.filter(question_id_id=question_id)
        anwser1 = anwser[0].content
        anwser2 = anwser[1].content
        anwser3 = anwser[2].content
        anwser4 = anwser[3].content
        print(anwser1)
        checked = 0
        for idx, val in enumerate(anwser):
            if val.value == True:
                checked = idx + 1;
                print(checked)
        category = Category.objects.filter(status=True)
        context = {
            "anwser1": anwser1,
            "anwser2": anwser2,
            "anwser3": anwser3,
            "anwser4": anwser4,
            "question": question,
            "category": category,
            "checked": checked
        }
        return render(request, 'ManageQuit/UpdateQuestion.html', context)

    def post(self, request):
        if request.method == "POST":
            try:
                qid = request.POST.get("id")
                data = Question.objects.get(id=qid)
                answer_get = request.POST.getlist('answer')
                choice = request.POST.get('choice')
                form = QuestionSerializer(request.POST, request.FILES, instance=data)
            except:
                HttpResponse("Chọn câu trả lời và chọn đáp án đúng")
            if form.is_valid():
                form.save()
            else:
                HttpResponse("Không thể thêm câu hỏi")
                # return render(request, 'ManageNews/ListNews.html', context)
            listAnswer = Answer.objects.filter(question_id_id=qid)
            for idx, val in enumerate(listAnswer):
                if idx + 1 == int(choice):
                    answer = Answer(id=val.id, question_id_id=val.question_id, content=answer_get[idx], value=True,
                                    status=True)
                else:
                    answer = Answer(id=val.id, question_id_id=val.question_id, content=answer_get[idx], value=False,
                                    status=True)
                try:
                    answer.save()
                except:
                    HttpResponse("Cant not insert Answer")
            return redirect("question/")


def select_category(request, category_id):
    question = Question.objects.filter(category_id=category_id)
    category = Category.objects.filter(status=True)

    context = {
        "list": question,
        "category": category,
        "mes": "Chọn theo"
    }

    return render(request, 'ManageQuit/ListQuestion.html', context)


def search(request):
    input = request.POST.get("input")
    question = Question.objects.filter(title__contains=input)
    category = Category.objects.filter(status=True)

    context = {
        "list": question,
        "category": category,
        "mes": "Chọn theo"
    }

    return render(request, 'ManageQuit/ListQuestion.html', context)


def result(request):
    id = request.user.id
    print(id)
    # result_all = Result.objects.exclude(user_id=2)
    result_all = Result.objects.all()
    # filter(Q(user_id_id__in=1))
    list_scope = []
    list_user = []
    for o in result_all:
        list_scope.append(o.scope)
        list_user.append(o.user_id.username)
    context = {
        "list_scope": list_scope,
        "list_user": list_user,
        "mes": "Kết quả"
    }
    return render(request, 'ManageQuit/Result.html', context)
