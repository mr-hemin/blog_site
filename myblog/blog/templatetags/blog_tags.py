from django import template
from ..models import Category

register = template.Library()


@register.inclusion_tag('blog/category_list.html')
def show_categories():
    categories = Category.objects.all()
    return {"categories": categories}
