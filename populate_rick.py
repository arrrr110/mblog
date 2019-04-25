import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mblog.settings')

import django
django.setup()

from rick.models import Category, Article


# 输入测试数据

def populate():
    python_cat = add_cat('Python','slug1')

    add_article(cat=python_cat,
        title="Official Python Tutorial",
        body="http://docs.python.org/2/tutorial/")

    add_article(cat=python_cat,
        title="How to Think like a Computer Scientist",
        body="http://www.greenteapress.com/thinkpython/")

    add_article(cat=python_cat,
        title="Learn Python in 10 Minutes",
        body="http://www.korokithakis.net/tutorials/python/")

    django_cat = add_cat("医事晚报",'slug2')

    add_article(cat=django_cat,
        title="Official Django Tutorial",
        body="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")

    add_article(cat=django_cat,
        title="Django Rocks",
        body="http://www.djangorocks.com/")

    add_article(cat=django_cat,
        title="How to Tango with Django",
        body="http://www.tangowithdjango.com/")

    frame_cat = add_cat("Other Frameworks",'slug3')

    add_article(cat=frame_cat,
        title="Bottle",
        body="http://bottlepy.org/docs/dev/")

    add_article(cat=frame_cat,
        title="Flask",
        body="http://flask.pocoo.org")

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Article.objects.filter(category=c):
            print ("- {0} - {1}".format(str(c), str(p)))

def add_article(cat, title, body, views=0):
    p = Article.objects.get_or_create(category=cat, title=title)[0]
    p.body=body
    p.views=views
    p.save()
    return p

def add_cat(name,slug):
    c = Category.objects.get_or_create(name=name)[0]
    c.slug = slug
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print ("Starting rick population script...")
    populate()