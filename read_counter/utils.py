import datetime

from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum

from .models import ReadNum, ReadDetail


# 阅读计数器，每增加一次阅读，计数器加一
# 返回cookie的key
def read_counter_add(request, obj):

    ct = ContentType.objects.get_for_model(obj)
    key = '%s_%s_had_been_read' % (ct.model, obj.pk)

    if not request.COOKIES.get(key):

        # 总阅读数 +1
        readnum, _ = ReadNum.objects.get_or_create(content_type=ct, object_id=obj.pk)
        readnum.read_num += 1
        readnum.save()

        # 当天阅读数 +1
        date = timezone.now().date()
        readDetail, _ = ReadDetail.objects.get_or_create(content_type=ct, object_id=obj.pk, date=date)
        readDetail.read_num += 1
        readDetail.save()

    return key


def get_7_days_read_data(content_type):
    today = timezone.now().date()
    dates = []
    read_nums = []
    for i in range(6, -1, -1):
        date = today - datetime.timedelta(days=i)
        read_detail = ReadDetail.objects.filter(content_type=content_type, date=date)
        result = read_detail.aggregate(read_num_sum=Sum('read_num'))
        dates.append(date.strftime('%m/%d'))
        read_nums.append(result['read_num_sum'] or 0)
    return dates, read_nums


def get_today_hot_data(content_type):
    today = timezone.now().date()
    read_details = ReadDetail.objects \
                            .filter(content_type=content_type, date=today).order_by('-read_num')
    return read_details[:6]


def get_yesterday_hot_data(content_type):
    today = timezone.now().date()
    yesterday = today - datetime.timedelta(days=1)
    read_details = ReadDetail.objects \
                            .filter(content_type=content_type, date=yesterday).order_by('-read_num')
    return read_details[:6]

