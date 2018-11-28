import datetime

from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from django.core.cache import cache

import markdown

from blog.models import Blog
from read_counter.utils import get_a_week_read_data



def home(request):
    recent_blogs = Blog.objects.all().order_by('-last_updated_time')[:6]
    read_date, read_count = get_a_week_read_data()

    context = {}
    context['recent_blogs'] = recent_blogs
    context['read_date'] = read_date
    context['read_count'] = read_count
    return render(request, 'home.html', context)




def about(request):
    context = {}
    about = Blog.objects.get(title='关于本站')
    about.content = markdown.markdown(about.content,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    context['about'] = about
    return render(request, 'about.html', context)