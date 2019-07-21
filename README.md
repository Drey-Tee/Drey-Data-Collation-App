# Drey's Data Collation App
 A simple data collation app to aid in the upload of excelfiles.

To run the codes:

*Pip install virtualenv 
*Create a virtualenv and activate it. 
Eg virtualenv env1
Source env1/bin/activate 
*Change current directory into dreys_project 
*Run pip install -r requirements.txt
*Install rabbitmq
*Run rabbitmq-server start in new command line 
*Activate virtualenv and change current directory to dreys_project in new command line
*Run celery -A dreys_project worker -l info
*Activate virtualenv and change directory to dreys_project in new command line
*Run python manage.py runserver
