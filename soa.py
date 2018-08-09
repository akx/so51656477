import os

DEBUG = True
ROOT_URLCONF = 'soa'
ALLOWED_HOSTS = '*'
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(os.path.dirname(__file__), 'pingu.sqlite3'),
	},
}
SECRET_KEY = "x"
INSTALLED_APPS = ["pingu.apps.PinguConfig"]

urlpatterns = []