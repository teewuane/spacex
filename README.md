I wanted to demonstrate my ability to take some simple instructions and make something that works. I did this from the backseat of a truck while I was driving through Nevada with spotty cell service.

It’s not exactly a “micro” service. For that I’d probably use Flask to keep it simple. But to get this up and off the ground as fast as possible I chose Django and the Django REST Framework. I tend to follow the “make it work, make it work right, make it fast” pattern. I’d say this is somewhere between “make it work” and “make it work right”. I’d probably add some caching to the requests to the SpaceX API to speed things up and feel better about not hammering their endpoint.

For caching I would make the initial request to the SpaceX endpoint and store the results in Redis. Then in my code I’d look to Redis for a fresh entry and if it didn’t exist or it existed but was stale I’d re-hit their api and store the up to date results. That would greatly speed things up and I’d feel like it was much closer to working “right”.

I really did the minimal amount of work required to consume the SpaceX API and turn it into my own resource.

Typically with Django Rest Framework you would represent your own models and data in your endpoints. Here I knew I wanted to easily be able to swap those out, so first I made my own object that I would first return, I got that working. Then, I swapped that out with data from the SpaceX endpoint.

If in the future you wanted to change this to use data from my own database it would be a matter of changing the type of serializer that you are using from "Serializer" to "HyperlinkedModelSerializer" (Or something similar depending on requirements). And create a model in Django and table in the database. The data is simple and I’d feel comfortable keeping the same database and swapping out Django / rest framework with Flask and SQLAlchemy.

My stack included:
	Digital Ocean Droplet running Ubuntu 18
	Nginx
	Lets Encrypt and the Certbot for SSL
	Gunicorn
	Python 3
	SQLite3 (I’d typically use PostgreSQL but just wanted to create a quick proof of concept here, plus in this scenario the database is not used anyways.)
	Django 2.2
	Django Rest Framework
	Python Requests (I usually like to write my own connections to endpoints vs using libraries that are available out there just to keep the code and requirements minimal.)


You can view the client/website at https://spacex.teewuane.com
View the API bits at https://spacex.teewuane.com/api/v1/launchpads
