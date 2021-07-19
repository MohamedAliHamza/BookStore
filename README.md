# BOOK-STORE PROJECT

🛒 This is an e-commerce bookstore API based on Django REST Framework. This API features two types of users - Customer and Admin. For authenticating users, Django REST Framework simple jwt is used. The installation guide is given below.



## Setup & Launch
```
git clone https://github.com/MohamedAliHamza/BookStore.git
cd bookstore\backend
pip install virtualenvwrapper-win
mkvirtualenv venv
workon venv
pip install -r requirement.txt
python manage.py migrate
python manage.py runserver
```
## API Swagger Docs 
```
 http://127.0.0.1:8000/api/docs/
```
