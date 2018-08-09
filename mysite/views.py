import datetime

from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from django.core.cache import cache

from blog.models import Blog
from read_counter.utils import get_today_hot_data
from read_counter.utils import get_yesterday_hot_data
from read_counter.utils import get_7_days_read_data



def get_7_days_hot_blogs():
    today = timezone.now().date()
    date = today - datetime.timedelta(days=7)
    blogs = Blog.objects \
                    .filter(read_details__date__lte=today, read_details__date__gte=date) \
                    .values('id', 'title') \
                    .annotate(read_num_sum=Sum('read_details__read_num')) \
                    .order_by('-read_num_sum')
    return blogs[:6]


def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = get_7_days_read_data(blog_content_type)

    # 获取7天热门博文的缓存数据
    seven_days_hot_blogs = cache.get('seven_days_hot_blogs')
    if seven_days_hot_blogs is None:
        seven_days_hot_blogs = get_7_days_hot_blogs()
        cache.set('seven_days_hot_blogs', seven_days_hot_blogs, 3600)   # 3600s = 1h

    context = {}
    context['dates'] = dates
    context['read_nums'] = read_nums
    context['today_hot_data'] = get_today_hot_data(blog_content_type)
    context['yesterday_hot_data'] = get_yesterday_hot_data(blog_content_type)
    context['seven_days_hot_blogs'] = get_7_days_hot_blogs()

    return render(request, 'home.html', context)



