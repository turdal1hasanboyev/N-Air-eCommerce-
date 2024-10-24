# global_context bu orqali barcha template fayllariga ma'lumot yuborish mumkin

### Har doim chap tamon frontend o'ng tomon esa backend bo'ladi

from apps.n_air.models import Tag, Category


def object(request):
    categories = Category.objects.filter(is_active=True).order_by('name')
    tags = Tag.objects.filter(is_active=True).order_by('name')
    
    return {
        'categories': categories,
        'tags': tags,
    }
