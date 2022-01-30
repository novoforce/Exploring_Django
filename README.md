# Exploring_Django

Model View Template
```
USERS <----> DJANGO <----
                        |             ------> MODEL
                        |             |
                        V             V
                        URLS <----> VIEWS
                                      A
                                      |
                                      -------> TEMPLATE
```
                                      

## Basic environment settings
conda create -n django_traversy python=3.9.7
conda activate django_traversy
pip install Django==3.2.7


# for creating the project
python manage.py startproject studybud

# for creating the apps
python manage.py startapp base

# add the installed app to the django project
go to > studybud\studybud\settings.py > INSTALLED_APPS > add this >>'base.apps.BaseConfig' class

# For adding templates to the project
go to > studybud\studybud\settings.py and add the following to DIR[]
BASEDIR / "templates"


26/1/2022:> https://www.youtube.com/watch?v=PtQiiknWUcI&t=2395s


# include a template into different templates
{% include 'navbar.html'%}

# for extending the template

navbar.html ---> main.html (include)
                    ||
                    VV
                home.html / room.html (extending the main.html template functionality)


    inside main.html file
```python
    {% include 'navbar.html' %}
    {% block content %}
    {% endblock %}
```

    inside home.html file

```python
{% extends 'main.html'%}

{% block content %}
<h1>room</h1>

{% endblock %}
```

