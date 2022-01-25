# Exploring_Django

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



26/1/2022:> https://www.youtube.com/watch?v=PtQiiknWUcI&t=2395s