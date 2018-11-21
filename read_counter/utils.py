from django.contrib.contenttypes.models import ContentType

from .models import ReadNum, ReadDetail


def counter_once_read(request, obj):
    ct = ContentType.objects.get_for_model(obj)
    key = '%s_%s_had_been_read' % (ct.model, obj.pk)
    if not request.COOKIES.get(key):
        if ReadNum.objects.filter(content_type=ct, object_id=obj.pk).count():
            # 存在记录
            readnum = ReadNum.objects.get(content_type=ct, object_id=obj.pk)
        else:
            # 不存在
            readnum = ReadNum(content_type=ct, object_id=obj.pk)
        # +1
        readnum.read_num += 1
        readnum.save()

        
        # 记录访问ip
        if 'HTTP_X_FORWARDED_FOR' in request.META:  # 获取ip
            client_ip = request.META['HTTP_X_FORWARDED_FOR']
            client_ip = client_ip.split(",")[0]  # 所以这里是真实的ip
        else:
            client_ip = request.META['REMOTE_ADDR']  # 这里获得代理ip
        username = request.META['USERNAME']
        read_detail = ReadDetail(ip=client_ip, username=username)
        read_detail.save()

    return key