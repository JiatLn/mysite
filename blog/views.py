from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.utils.text import slugify
# 第三方
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
import markdown
from markdown.extensions.toc import TocExtension
# 本地
from .models import Blog, BlogType
from read_counter.utils import counter_once_read, get_a_week_read_data


# Create your views here.
def get_blog_list_common_data(request, blogs):
    
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(blogs, per_page=settings.PER_PAGE_BLOGS_NUM, request=request)
    blog_of_page = p.page(page)

    # 获取日期归档对应的博文数量
    blog_dates = Blog.objects.dates('created_time', 'month', order='DESC')
    blog_dates_dict = {}
    for blog_date in blog_dates:
        blog_count = Blog.objects.filter(created_time__year=blog_date.year,
                                        created_time__month=blog_date.month).count()
        blog_dates_dict[blog_date] = blog_count
    # 日期按时间倒序排列
    blog_dates_dict = sorted(blog_dates_dict.items(), key=lambda blog_dates_dict: blog_dates_dict[0])


    context = {}
    context['blog_of_page'] = blog_of_page
    context['blogs'] = blog_of_page.object_list
    context['blog_types'] = BlogType.objects.all()
    context['blog_dates'] = blog_dates_dict

    return context


def blog_list(request):

    blogs = Blog.objects.all()
    for blog in blogs:
        blog.content = markdown.markdown(blog.content,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                     
                                  ])
    context = get_blog_list_common_data(request, blogs)

    return render(request, 'blog/blog_list.html', context)


def blogs_with_type(request, blog_type_pk):

    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    blogs = Blog.objects.filter(blog_type=blog_type)

    context = get_blog_list_common_data(request, blogs)
    context['blog_type'] = blog_type

    return render(request, 'blog/blogs_with_type.html', context)


def blogs_with_date(request, year, month):

    blogs = Blog.objects.filter(created_time__year=year, created_time__month=month)

    context = get_blog_list_common_data(request, blogs)
    context['blog_date'] = '%d年%d月' % (year, month)

    return render(request, 'blog/blogs_with_date.html', context)


# 博文详情页
def blog_detail(request, blog_pk):

    blog = get_object_or_404(Blog, pk=blog_pk)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        TocExtension(slugify=slugify),
    ])
    blog.content = md.convert(blog.content)

    read_cookie_key = counter_once_read(request, blog)

    context = {}
    context['perivous_blog'] = Blog.objects.filter(created_time__lt=blog.created_time).first()
    context['next_blog'] = Blog.objects.filter(created_time__gt=blog.created_time).last()
    context['blog'] = blog
    context['toc'] = md.toc
        
    response = render(request, 'blog/blog_detail.html', context)
    response.set_cookie(read_cookie_key, 'true') # 已阅

    


    return response