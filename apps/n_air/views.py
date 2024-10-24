from django.shortcuts import render, redirect, get_object_or_404 ### get_object_or_404 ### redirect otib yuborish uchun

from django.core.paginator import Paginator ### paginator class

from .models import Banner, Product


def home_page_view(request):
    ### carousel 3x banner
    banners = Banner.objects.filter(is_active=True).order_by('-id')[:3] ### filterlash va oxiridan 3ta olib kelish
    ### fall and fell banner
    banners2 = Banner.objects.filter(is_active=True).order_by('-id')[:2] ### oxiridan kesish qayta filterlashda ishlamaydi

    '''
    if banner:
        banners2 = Banner.objects.filter(is_active=True, name__icontains=banner) ### bu usul ishlamaydi chunki tepada kesilgan
    
    ### *Ishlashi uchun context {ni ichida kesish kerak [:2]} qilib
    '''

    products = Product.objects.filter(is_active=True).order_by('id')[:6]

    context = {
        'banners': banners,
        'banners2': banners2,
        'products': products,
    }

    return render(request, 'index.html', context) ### to'g'ridan to'gri bersa ham bo'ladi shu usulda yoki tenglashtirib beriladi quyidagi kabi:

    ### return render(request=request, template_name='index.html', context=context) ### birinchi yozilgan bu argument 2-si esa def dan kelib chiqib beriladi

    ### context bitta bo'lsa to'g'ridan to'gri bersa ham bo'ladi {'a': a} yoki context={'a': a} qilib

def product_detail_page_view(request, slug):
    # slug bo'yicha mahsulotni topish
    product = Product.objects.filter(is_active=True, slug__iexact=slug).first() ### birinchisini oladi list holatidan

    product.views_count += 1

    product.save() ### har safar detail sahifaga o'tilganda views_countga + 1 qo'shiladi

    # Shu mahsulotning kategoriyasiga mos keladigan boshqa mahsulotlarni topish
    if not product:
        products = Product.objects.none()  # Agar mahsulot topilmasa, bo'sh queryset

    products = Product.objects.filter(is_active=True, category_id=product.category.id).exclude(id=product.id).order_by('-id')[:3] ### .exclude kesadi id=product.id hozirgi produkt ya'ni o'zi chiqmasligi uchun

    ### if else bilan ishlasam ham bolardi

    '''
    if product:
        products = Product.objects.filter(is_active=True, category_id=product.category.id).exclude(id=product.id).order_by('-id')[:3]

    else:
        products = Product.objects.none()
    '''

    '''
    get_object_or_404 orqali qilishim ham mumkin agar product yo'q bo'lsa avtomatik 404 error beradi

    def product_detail_page_view(request, slug):
        product = get_object_or_404(Product, slug__iexact=slug, is_active=True)

        products = Product.objects.filter(is_active=True, category_id=product.category.id).exclude(id=product.id).order_by('-id')[:3]
    '''

    '''
    __ = Filterlash(tenglashtirish) va *yoki foreign key bog'lanish bo'lsa ichma ich kirish uchun (Odatda filterlash(tenglashtirish) uchun bu ham)
    _ = Modelning fieldlariga ichma ich to'g'ridan to'g'ri murojat qilish (Kirish)
    . = (Tashqi) Obyektning fieldlariga to'g'ridan to'g'ri murojat qilish (To'g'ridan to'g'ri olish)
    '''

    context = {
        'product': product,
        'products': products,
    }

    return render(request=request, template_name='single.html', context=context)

def products_page_view(request, slug):
    products = Product.objects.filter(is_active=True, category__slug__exact=slug).order_by('-name') ### fieldlarni to'g'ridan to'g'ri tenglashtirsa ham bo'ladi lekin aniqlik muhim *** Ichma ich kirib borish __ orqali (odatda __ ichma ich kirib borib filterlash(tenglashtirish) uchun qilinadi bu)
    
    #context = {
    #    'products': products[:12], ### context ni ichida kesish (Odatda contextda obyekt 1ta bo'lsa return render() ichida berish kerak bu shunchaki joy tejaydi)
    #}

    return render(request, 'products.html', {'products': products[:12]}) ### hatto shu yerda ham kessa boladi

    ### return render(request=request, template_name='products.html', context={'products': products[:12]})

'''
order_by() bilan tanishamiz 
order_by() - sortlash (saralash) uchun foydalaniladi
order_by('id') id bo'yicha 1, 2, 3, ... (O'sib borish tartibida)
order_by('-id') id bo'yicha 3, 2, 1, ... (Kamayib borish tartibida)
order_by('?') random saralash har safar har hil deganidek

O'zi umuman shart berilganda ko'payib borish tartibida yani 1, 2, 3, ... a, b, d ... 
Agar shart oldiga - qo'yilsa kamayib borish tartibida bo'ladi 3, 2, 1, ... d, b, a ...
? qo'yilsa random shaklda boladi
'''
