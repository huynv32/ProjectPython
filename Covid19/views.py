from django.contrib.sites import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.sites import requests
# Create your views here.
from rest_framework.views import APIView
import requests

from Covid19.models import Country, Global, Summary


# class Data(APIView):
#     def get(self, request):
#         globals = Global.objects.all()
#         for g in globals:
#             go = g.countryCode
#             print(go)
#             response_result = requests.get("https://api.covid19api.com/country/" + go)
#             print(response_result)
#             data_result = response_result.json()
#             for o in data_result:
#                 summary = Summary(country=o["Country"], countryCode=o["CountryCode"], confirmed=o["Confirmed"],
#                                   deaths=o["Deaths"], date=o["Date"])
#                 summary.save()
#
#         return HttpResponse("add thành công")

def cases(request):
    id = request.user.id
    print(id)
    # result_all = Result.objects.exclude(user_id=2)
    result_all = Global.objects.all().order_by('totalConfirmed')
    result_all1 = Global.objects.all().order_by('id')
    try:
        count = (result_all.count()) // 15
    except:
        count = (result_all.count())

    # filter(Q(user_id_id__in=1))
    list_country = []
    list_totalConfirmed = []
    list_page = result_all1[:count]
    for o in result_all[:15]:
        list_country.append(o.country)
        list_totalConfirmed.append(o.totalConfirmed)
    context = {
        "list_country": list_country,
        "list_totalConfirmed": list_totalConfirmed,
        "mes": "Kết quả",
        "count": list_page,
        "country": result_all,
    }
    return render(request, 'Covid19/Result.html', context)


def cases_page(request, page):
    re_page = int(page) + 1
    result_all1 = Global.objects.all().order_by('id')
    result_all = Global.objects.all().order_by('totalConfirmed')
    count = result_all.count()
    list_country = []
    list_totalConfirmed = []
    count = result_all1[:count // 15]
    for o in result_all[(re_page - 1) * 15:re_page * 15]:
        list_country.append(o.country)
        list_totalConfirmed.append(o.totalConfirmed)
    context = {
        "list_country": list_country,
        "list_totalConfirmed": list_totalConfirmed,
        "mes": "Kết quả",
        "count": count,
        "country": result_all
    }
    return render(request, 'Covid19/Result.html', context)


def cases_page1(request):
    page = request.GET.get("page")
    print(page)
    re_page = int(page) + 1
    result_all1 = Global.objects.all().order_by('id')
    result_all = Global.objects.all().order_by('totalConfirmed')
    count = result_all.count()
    list_country = []
    list_totalConfirmed = []
    count = result_all1[:count // 15]
    for o in result_all[(re_page - 1) * 15:re_page * 15]:
        list_country.append(o.country)
        list_totalConfirmed.append(o.totalConfirmed)
    context = {
        "list_country": list_country,
        "list_totalConfirmed": list_totalConfirmed,
        "mes": "Kết quả",
        "count": count,
        "country": result_all
    }
    return JsonResponse({"list_country": list_country, "list_totalConfirmed": list_totalConfirmed}, status=200)


def select_code(request, code):
  try:
      summary = Summary.objects.filter(countryCode=code)
      result_all = Global.objects.all()
      try:
          count = result_all.count()
          count = result_all[:count // 15]
      except:
          HttpResponse("dữ liệu không đủ")
      list_date = []
      list_totalConfirmed = []
      for o in summary:
          list_date.append(o.date)
          list_totalConfirmed.append(o.confirmed)
      context = {
          "list_date": list_date,
          "list_totalConfirmed": list_totalConfirmed,
          "mes": "Kết quả của " + summary[1].country,
          "count": count,
          "country": result_all
      }
      return render(request, 'Covid19/Country.html', context)
  except:
      HttpResponse("Có lỗi xẩy ra ")


def select_code1(request):
    country = request.GET.get("page")
    summary = Summary.objects.filter(country__contains=country)
    result_all = Global.objects.all()
    count = result_all.count()
    print(count // 15)
    count = result_all[:count // 15]
    list_date = []
    list_totalConfirmed = []
    for o in summary:
        list_date.append(o.date)
        list_totalConfirmed.append(o.confirmed)
    context = {
        "list_date": list_date,
        "list_totalConfirmed": list_totalConfirmed,
        "mes": "Kết quả của " + summary[1].country,
        "count": count,
        "country": result_all
    }
    return JsonResponse({"list_country": list_date, "list_totalConfirmed": list_totalConfirmed}, status=200)


def deaths(request):
    # result_all = Result.objects.exclude(user_id=2)
    page = 1;
    result_all = Global.objects.all().order_by('totalDeaths')
    result_all1 = Global.objects.all().order_by('id')
    count = (result_all.count()) // 15

    # filter(Q(user_id_id__in=1))
    list_country = []
    list_totalConfirmed = []
    count = result_all1[:count]
    for o in result_all[:15]:
        list_country.append(o.country)
        list_totalConfirmed.append(o.totalDeaths)
    context = {
        "list_country": list_country,
        "list_totalConfirmed": list_totalConfirmed,
        "mes": "Kết quả Số ca tử vong",
        "count": count,
        "country": result_all,
    }
    return render(request, 'Covid19/Deads.html', context)


def deaths_page(request, page):
    re_page = int(page) + 1
    result_all1 = Global.objects.all().order_by('id')
    result_all = Global.objects.all().order_by('totalDeaths')
    count = result_all.count()
    list_country = []
    list_totalConfirmed = []
    count = result_all1[:count // 15]
    for o in result_all[(re_page - 1) * 15:re_page * 15]:
        list_country.append(o.country)
        list_totalConfirmed.append(o.totalDeaths)
    context = {
        "list_country": list_country,
        "list_totalConfirmed": list_totalConfirmed,
        "mes": "Kết quả số ca tử vong",
        "count": count,
        "country": result_all
    }
    return render(request, 'Covid19/Deads.html', context)
