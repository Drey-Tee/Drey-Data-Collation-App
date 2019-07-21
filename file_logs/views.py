from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from file_logs.forms import UploadFileForm
from django.contrib.auth.decorators import login_required
from .models import UploadFile, AllData
import pandas as pd 
from django.contrib import messages
from django.conf import settings
# from sqlalchemy import create_engine
from file_logs.tasks import process_file, read_file

# database_name = settings.DATABASES['default']['NAME']
# database_url = 'sqlite:///{}'.format(database_name)
# engine = create_engine(database_url, echo=False)




@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        new_file = read_file(request.FILES['file'])
        new_file.columns = new_file.columns.str.lower()
        new_file.columns = new_file.columns.str.replace(' ', '')
        new_file_columns = new_file.columns.values
        print(new_file_columns)
        if len(new_file_columns) == 5:
            if set(new_file_columns) == set(['firstname','lastname', 'age', 'gender', 'address']):
                if form.is_valid():
                    instance = UploadFile(file=request.FILES['file'], user=request.user, file_name=str(request.FILES['file']))
                    instance.save()
                    new_file['file_id'] = instance.id
                    new_file['user_id'] = request.user.id
                    print(new_file)
                    list_dict = new_file.to_dict('records')
                    process_file.delay(list_dict)
                    # new_file.to_sql('file_logs_alldata', con=engine, if_exists="append", index=False)
                    return redirect('profile')
    else:
        form = UploadFileForm()
    return render(request, 'file_logs/upload.html', {'form': form})

