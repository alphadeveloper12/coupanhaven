from django.shortcuts import render
from web.models import *
# Create your views here.
def home(request):
    stores = Store.objects.all()

    # Create a dictionary to store the first associated coupon for each store
    store_coupons = {}

    for store in stores:
        # Get the first coupon associated with the store, if any
        coupon = Coupon.objects.filter(store=store).first()

        # Add the store and its associated coupon (if any) to the dictionary
        store_coupons[store] = coupon

    context = {
        "stores": stores,
        "store_coupons": store_coupons,
    }
    return render(request, 'index.html', context)

def stores(request):
    return render(request, 'stores.html')

def category(request):
    return render(request, 'category.html')

def coupans(request):
    return render(request, 'coupans.html')

def dealCoupans(request):
    return render(request, 'dealCoupans.html')

def blog(request):
    return render(request, 'blog.html')


from django.shortcuts import render, get_object_or_404
from .models import Store, Category


def store_details(request, pk):
    store = get_object_or_404(Store, id=pk)
    coupans = Coupon.objects.filter(store=store)
    # deals = Deal.objects.filter(store=store)

    # categories_and_deals = list(coupans) + list(deals)

    context = {
        "stores": store,
        "categories_and_deals": coupans,
    }
    return render(request, 'store_details.html', context=context)
