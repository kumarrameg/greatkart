from .models import Category


def category_menu_links(request):
    cat_links = Category.objects.all()
    return dict(cat_links=cat_links)