from django.shortcuts import render


# 404 xatosi uchun maxsus sahifa
def custom_page_not_found_page_view(request, exception):
    return render(request, '404.html', status=404)
