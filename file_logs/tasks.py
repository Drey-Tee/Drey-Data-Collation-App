
from file_logs.models import UploadFile, AllData
import pandas as pd 
from celery import shared_task
from django.shortcuts import render, redirect


def read_file(file_path):
    if str(file_path).endswith('.csv'):
        data = pd.read_csv(file_path, low_memory=False)
    elif str(file_path).endswith(('.xlsx', '.xls')):
        data = pd.read_excel(file_path)
    else:
        data = pd.DataFrame([])
    return data

@shared_task
def process_file(list_dict):
	for data_dict in list_dict:
		d = AllData(**data_dict)
		d.save()
	return 'done'