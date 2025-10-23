from django.shortcuts import render, get_object_or_404
from .import models
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

# Create your views here.
def cars(request):
    cars = models.Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 3) # Show 3 cars per page
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    
    model_search =models.Car.objects.values_list('model',flat=True).distinct()
    city_search = models.Car.objects.values_list('city',flat=True).distinct()
    year_search = models.Car.objects.values_list('year',flat=True).distinct()
    body_style_search = models.Car.objects.values_list('body_style',flat=True).distinct()
    data = {
        'cars': paged_cars,
        'model_search':model_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style_search':body_style_search,
    }
    return render(request, 'cars/cars.html',data)


def car_detail(request, id):
    single_car = get_object_or_404(models.Car, pk=id)

    data = {
        'single_car': single_car
    }
    return render(request, 'cars/car_detail.html',data)


def search(request):
    cars = models.Car.objects.order_by('-created_date')
    model_search =models.Car.objects.values_list('model',flat=True).distinct()
    city_search = models.Car.objects.values_list('city',flat=True).distinct()
    year_search = models.Car.objects.values_list('year',flat=True).distinct()
    body_style_search = models.Car.objects.values_list('body_style',flat=True).distinct()
    transmission_search=models.Car.objects.values_list('body_style',flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword )
    
    if 'model' in request.GET:
        keyword = request.GET['model']
        if keyword:
            cars = cars.filter(model__iexact=keyword )

    if 'city' in request.GET:
        keyword = request.GET['city']
        if keyword:
            cars = cars.filter(city__iexact=keyword )
    
    if 'year' in request.GET:
        keyword = request.GET['year']
        if keyword:
            cars = cars.filter(year__iexact=keyword )

    if 'body_style' in request.GET:
        keyword = request.GET['body_style']
        if keyword:
            cars = cars.filter(body_style__iexact=keyword )
    
    if 'transmission' in request.GET:
        keyword = request.GET['transmission']
        if keyword:
            cars = cars.filter(body_style__iexact=keyword )

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars=cars.filter(price__gte = min_price,price__lte=max_price)


            
    data ={
        'cars': cars,
        'model_search':model_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style_search':body_style_search,
        'transmission_search':transmission_search
    }
    return render(request,'cars/search.html',data)
