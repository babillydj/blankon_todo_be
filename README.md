
# Description
this is a simple api Django project,   
there is no user or profile model, assuming it's already implemented in a separate service    
always add slash at the end of endpoint   



# Installation
Make sure you have the latest Docker and Docker Compose installed and active
- copy .env.dev to .env
- run `docker-compose build`
- run `docker-compose up`

It should be running at *localhost:8000/* now,     
you can open *localhost:8000/admin/* or *localhost:8000/api/v1/init* for trial   



# Notes
superuser account for admin (localhost:8000/admin/):    
username = blankonuser   
password = blankonpass   

run test:   
- run `docker exec -it blankon-web-1 sh` (container name)
- run `python manage.py test`

for any migrate or create superuser
- run `docker exec -it blankon-web-1 sh` (container name)
- run `python manage.py makemigrations`
- run `python manage.py migrate`
- run `python manage.py createsuperuser`  
