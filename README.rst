Browner
=======
:Author:
	Víctor Muñoz <victorm@marshland.es>

About
=====
This web application is a simple multiuser tasklist, developed to demonstrate how to quickly develop applications using Django and MongoDB.

Dependencies
============
* `Django <http://djangoproject.com>`_, at least version 1.3 (due to the use of django.contrib.staticfiles).
* `MongoDB <http://mongodb.org>`_ and `PyMongo <http://api.mongodb.org/python/>`_.
* `PostgreSQL <http://postgresql.org>`_ and `Psycopg2 <http://initd.org/psycopg/>`_.

Usage
=====
The code is a full-featured Django project, so you can run it simply by creating the database tables starting the development server::

	$ ./manage.py syncdb
	$ ./manage.py runserver

Of course, you should have configured the PostgreSQL and MongoDB connection parametres beforehand, as well as created the appropriate user and database for PostgreSQL.

Since MongoDB is a schemaless database it does not require any special attention.

License
=======
This is beerware, which means: use, copy, modify, redistribute or print and burn my code, as long as you give me credit. If we meet someday, you can buy me a beer.

