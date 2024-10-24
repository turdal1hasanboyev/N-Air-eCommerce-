from django.shortcuts import render


def register_page_view(request):
    
    return render(request=request, template_name='register.html')
