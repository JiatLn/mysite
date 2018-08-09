from django import template
from django.contrib.contenttypes.models import ContentType

from ..models import Comment
from ..forms import CommentForm


register = template.Library()


@register.simple_tag
def get_comments(obj):
    content_type = ContentType.objects.get_for_model(obj)
    comments = Comment.objects.filter(content_type=content_type, object_id=obj.pk, parent=None)
    return comments.order_by('-comment_time')


@register.simple_tag
def get_comment_count(obj):
    content_type = ContentType.objects.get_for_model(obj)
    comment_count = Comment.objects.filter(content_type=content_type, object_id=obj.pk).count()
    return comment_count


@register.simple_tag
def get_comment_form(obj):
    content_type = ContentType.objects.get_for_model(obj)
    comment_form = CommentForm(
        initial={'content_type': content_type.model, 'object_id': obj.pk, 'reply_comment_id': 0}
    )
    return comment_form