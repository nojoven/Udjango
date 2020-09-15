# Udjango
Udemy: Learn Django from scratch, build an E-commerce store, web based PDF generators, web crawlers, APIs using Python &amp; Django The instructor is Ashutosh Pawar https://www.udemy.com/course/django-course/
I removed the secret keys for security reasons.
You can generate a new one in a separate file (not settings.py) and access it using the django-keys module. You need to edit settings.py. There is a mistake in the documentation provided on pypi.org
You have to write #retrieve_key_from_file instead of retrieve_secret_key_from_file
https://pypi.org/project/django-keys/
