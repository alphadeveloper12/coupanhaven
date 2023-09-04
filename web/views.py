from django.shortcuts import render
from web.models import *
from django.shortcuts import render, get_object_or_404
# Create your views here.
def home(request):
    stores = Store.objects.all()
    category= Category.objects.all()

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
        "categories": category
    }
    return render(request, 'index.html', context)

def stores(request):
    # Get all stores from the database and order them by name
    stores = Store.objects.order_by('name')

    # Create a list to store the grouped stores
    store_groups = []

    # Initialize variables to keep track of the current letter and stores for that letter
    current_letter = None
    current_stores = []

    for store in stores:
        first_letter = store.name[0].upper()

        if first_letter != current_letter:
            # If the letter changes, add the current stores to the list
            if current_letter is not None:
                store_groups.append((current_letter, current_stores))
            current_letter = first_letter
            current_stores = []

        current_stores.append(store)

    # Add the last group of stores
    if current_stores:
        store_groups.append((current_letter, current_stores))

    context = {
        'store_groups': store_groups
    }

    return render(request, 'stores.html', context)

def category(request):
    category= Category.objects.all()
    context = {
        'categories': category
    }
    return render(request, 'category.html', context=context)

def coupans(request):
    return render(request, 'coupans.html')

def dealCoupans(request):
    return render(request, 'dealCoupans.html')

def blog(request):
    return render(request, 'blog.html')

def about_us(request):
    return render(request, 'about.html')

def privacy_policy(request):
    return render(request, 'privacy-policy.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def base(request):
    stores= Store.objects.all()

    context = {
        'stores': stores
    }
    return render(request, 'base.html', context=context)

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
