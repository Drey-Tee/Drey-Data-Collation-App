from django.shortcuts import render
from file_logs.models import UploadFile, AllData
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




def home(request):
    file_list = UploadFile.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(file_list, 10)
    try:
        files = paginator.page(page)
    except PageNotAnInteger:
        files = paginator.page(1)
    except EmptyPage:
        files = paginator.page(paginator.num_pages)

    return render(request, 'main/home.html', { 'files': files })


def alldata(request):
    data_list = AllData.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(data_list, 100)
    try:
        alldata = paginator.page(page)
    except PageNotAnInteger:
        alldata = paginator.page(1)
    except EmptyPage:
        alldata = paginator.page(paginator.num_pages)

    return render(request, 'main/alldata.html', { 'alldata': alldata})