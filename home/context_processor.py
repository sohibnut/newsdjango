from .models import Category

def baseView(request):
    categories = Category.objects.all()
    context = {
        'category_list': categories
    }

    return context