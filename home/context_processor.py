from .models import Category, Social, User

def baseView(request):
    categories = Category.objects.all()
    socials = Social.objects.all()
    authors = User.objects.all()
    context = {
        'category_list': categories,
        'social_list': socials,
        'authors' : authors,
    }

    return context