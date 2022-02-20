import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category,Page

def populate():
    python_pages = [
        {'title': 'Official Python Tutorial',
         'url': 'http://docs.python.org/3/tutorial/',
         'views':'123'},
        {'title': 'How to Think like a Computer Scientist',
         'url': 'http://www.greenteapress.com/thinkpython/',
         'views':'456'},
        {'title': 'Learn Python in 10 Minutes',
         'url': 'http://www.korokithakis.net/tutorials/python/',
         'views':'789'}]

    django_pages = [
        {'title': 'Official Django Tutorial',
         'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'views':'441'},
        {'title': 'Django Rocks',
         'url': 'http://www.djangorocks.com/',
         'views':'1024'},
        {'title': 'How to Tango with Django',
         'url': 'http://www.tangowithdjango.com/',
         'views':'31'}]

    other_pages = [
        {'title': 'Bottle',
         'url': 'http://bottlepy.org/docs/dev/',
         'views':'232'},
        {'title': 'Flask',
         'url': 'http://flask.pocoo.org',
         'views':'235'}]

    cats = {'Python': {'pages': python_pages},
            'Django': {'pages': django_pages},
            'Other Frameworks': {'pages': other_pages}}

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'],p['views'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat,title,url,views):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    if c.name == 'Python':
        c.views = 128
        c.likes = 64
    elif c.name == 'Django':
        c.views = 64
        c.likes = 32
    elif c.name == 'Other Frameworks':
        c.views = 32
        c.likes = 16
    c.save()
    return c

if __name__=='__main__':
    print('Starting Rango population script...')
    populate()
