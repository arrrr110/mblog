from django import template
from rick.models import Category,Article

register = template.Library()

@register.inclusion_tag('rick/cats.html')
def get_category_list(cat=None):
    # print('*'*100)
    return {'cats': Category.objects.all(), 'act_cat': cat}
