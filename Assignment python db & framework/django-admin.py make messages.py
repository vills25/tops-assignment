# Explain what does django-admin.py make messages command is used for?

'''
In Django, the django-admin.py or django-admin command-line utility provides various tools for managing Django projects,
including database migrations, starting development servers, creating new applications, and more.

The django-admin.py make_messages command is used to manage translation files within a Django project. Specifically, it is used to extract
translatable strings from the source code and templates of a Django project and create or update message files (.po files) for translation.

Here's how it works:

Identifying translatable strings: Django uses the gettext internationalization (i18n) framework for handling translations. Translatable 
strings in Django projects are typically wrapped in translation functions like gettext() or ugettext_lazy().

Extracting translatable strings: When you run the make_messages command, Django scans the Python source code files and templates of your 
project to find these translatable strings.

Generating .po files: After extracting the translatable strings, the make_messages command generates or updates .po files for each language 
specified in your project's settings. The .po files contain the translatable strings along with their context and comments to help translators
understand the context of the strings.

Translation: Once the .po files are generated, translators can use tools like msgfmt to translate the strings into the desired languages. 
They translate the strings within the .po files and save them.

Compiling .po files: After translation, the translated .po files need to be compiled into machine-readable .mo files. This is done using 
the compilemessages command, also provided by Django's django-admin.py utility.

Integration into the Django application: Finally, Django loads the appropriate translations based on the user's language preference and 
displays the translated strings in the application.

In summary, the make_messages command is a crucial tool for managing translations in Django projects, allowing developers to extract 
translatable strings and facilitate the localization of their applications.
'''