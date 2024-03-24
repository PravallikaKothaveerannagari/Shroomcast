# Hello #
and welcome to Shroomcast which is my idea to showcase some Django prowess (especially Class-based Views).

# What Shroomcast is #
It's an app based on my father-in-law's to be insights about picking mushrooms. It presents crucial weather information from
a chosen municipality.
The app uses Visual Crossing API to access weather data.

# Requirements #
The requirements for the project are listed in the requirements.txt file.

# How to run Shroomcast? #
To run Shroomcast you will need a virtual environment with Django 4.2.1 or later installed. You can refer to this guide for how to install and use virtual environment:
https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

Before your first run of Shroomcast, you will also need to create tables in your dbsqlite. To do this run:

python manage.py makemigrations

and if everything is well:

python manage.py migrate

If something wouldn't work for you here, please do reach out to jakub.dabrowski777@gmail.com

# How to use Shroomcast? #
You can find descriptions of each Shroomcast subsites in the About section.

# Query section limitations #
The query section is highly imperfect since it uses only the query points you spend while using the Shroomcast app.
Unfortunately, Visual Crossing API does not return the information about all the query points you have in your pricing model and how many
you have left.
The solution I suggest sums up the points you use and compares them to the limit that free users get (1000 query points a day).
When the Visual Crossing key is changed, the query counter is reset.

# RWD #
The Shroomcast's display accommodates to 10 most popular screen resolutions by:
https://www.hobo-web.co.uk/best-screen-size/

# Ackonowledgements #
Thanks to mirrey2222 from Pixabay for a beautiful and yet free procini mushroom picture used as a background for this app <3
https://pixabay.com/pl/users/mirey2222-20742269/