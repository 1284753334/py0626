# 自定义过滤器

from django.template.library import Library
from django.template.defaultfilters import stringfilter

register = Library()

# 加入 is_safe = True 支持HTML,识别标签
@register.filter(is_safe = True)
@stringfilter
def get_ext(value):
    index = value.rfind(".")
    return value[index+1:]

@register.filter(is_safe = True)
@stringfilter
def get_name(value):
    index = value.rfind("/")
    return value[index+1:]
