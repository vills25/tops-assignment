'''
Make Django application to demonstrate following things There will be 2 modules(Admin,Product manager) Admin can add product name
(ex.Product id and product name) ex. (1, Samsung), (2, Apple)...etc. Data should store in''' 

'''
Step 1:
    open your command prompt and install Django and then type the following command to create a new project.
        django-admin startproject myproject .

Step 2:  Create a Django app    
    create a new Django app "myapp" by running the following command in your command prompt:
        python manage.py startapp myapp
    add app name in myproject/settings.py/INSTALLED_APPS = ['myapp']    

Step 3:     
    Open the myapp/models.py file and define the models for product and admin. Add the following code:
    
    from django.db import models

    class Product(models.Model):
        id = models.IntegerField(primary_key=True)
        name = models.CharField(max_length=100)

        def __str__(self):
            return f"{self.id}: {self.name}"   

Step 4: Create database tables
    In your command prompt, run the following commands to create the necessary database tables:

    python manage.py makemigrations
    python manage.py migrate

Step 5: Register the models in the admin panel
    Open the myapp/admin.py file

    from django.contrib import admin
    from .models import Product

    admin.site.register(Product)

Step 6: Start the development server
    
    Run the following command in your command prompt to start the Django development server:

    python manage.py runserver
    Access the admin panel
    Open your web browser and visit http://localhost:8000/admin. You should see the Django admin login page.

Step 7:
    Create a superuser
    To access the admin panel, create a superuser by running the following command in your command prompt:

    python manage.py createsuperuser
    Follow the prompts to enter a username, email (optional), and password.

    Step 8:

    Add products through the admin panel
    Log in to the admin panel using the superuser credentials you created. Click on "Product" under "myapp" and add products by clicking the "Add" button.

'''