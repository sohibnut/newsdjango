from .models import Category, Social, User, Tag

def baseView(request):
    categories = Category.objects.all()
    socials = Social.objects.all()
    authors = User.objects.all()
    tags = Tag.objects.all()
    context = {
        'category_list': categories,
        'social_list': socials,
        'authors' : authors,
        'tags' : tags,
    }

    return context