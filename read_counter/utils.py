import datetime
# import time

from django.contrib.contenttypes.models import ContentType
from django.db.models import F
# from django.db.models import Count
from django.utils import timezone

from .models import ReadNum, ReadDetail


def counter_once_read(request, obj):
    ct = ContentType.objects.get_for_model(obj)
    key = '%s_%s_had_been_read' % (ct.model, obj.pk)
    if not request.COOKIES.get(key):
        # 阅读数+1
        readnum, created = ReadNum.objects.get_or_create(content_type=ct, object_id=obj.pk)
        readnum.read_num = F('read_num') + 1
        readnum.save()

        # 记录详细
        # 2019-5-27 14:43:07 更新 产生数据量太多，暂时不做记录，日后重写
        # if 'HTTP_X_FORWARDED_FOR' in request.META:  # 获取ip
        #     client_ip = request.META['HTTP_X_FORWARDED_FOR']
        #     client_ip = client_ip.split(",")[0]  # 所以这里是真实的ip
        # else:
        #     client_ip = request.META['REMOTE_ADDR']  # 这里获得代理ip
        # meta = request.META
        # read_detail = ReadDetail(ip=client_ip, meta=meta, content_type=ct, object_id=obj.pk)
        # read_detail.save()

    return key


def get_a_week_read_data():
    today = timezone.now().date()
    dates = []
    read_count = []
    for i in range(6, -1, -1):
        date = today - datetime.timedelta(days=i)
        dates.append(date.strftime("%m/%d"))
        date = datetime.date(date.year, date.month, date.day)

        rn = ReadDetail.objects.filter(date__date=date).count()
        read_count.append(rn)

    return dates, read_count
