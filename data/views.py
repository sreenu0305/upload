import csv
from pathlib import Path

from django.shortcuts import render
from tablib import Dataset

from .models import File
from .forms import FileForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect


def load(request):
    return render(request, 'data/upload.html')


def upload(request):
    if request.method == 'POST':
        file = request.FILES['myfile']
        print(file)
        print(dir(file))
        import pdb
        # pdb.set_trace()

        if not file.name.endswith('.csv'):
            messages.info(request, 'wrong format')
            return render(request, 'data/upload.html')

        file = file.readlines()
        file = file[1:]
        for each in file:
            file1 = each.decode('UTF-8').split(',')
            print(file1)
            print(type(file1))
            File.objects.get_or_create(name=file1[0], email=file1[1], phone=file1[2])

            # Path(__file__).resolve()
        # with open(file,'r') as csv_file :
        #     total_data=csv.reader(csv_file)
        #     # total_data = csv.reader(csvfile, delimiter=' ', quotechar='|')
        #     for line in total_data:
        #
        #         line1=line[1]
        #         line2=line[2]
        #         line3=line[3]
        return render(request, 'data/result.html', {'file': file1})

    return render(request, 'data/upload.html')


def all_objects(request):
    all = File.objects.all()
    return render(request, 'data/all_list.html',{'all': all})
