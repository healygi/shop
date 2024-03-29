from django.http import Http404
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse  # noqa: E501
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, F
from django.db.models.functions import Lower

from profiles.models import WishListItem
from .models import Product, Category, Review
from .forms import ReviewForm, ProductForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    query = None
    categories = None
    sort = None
    direction = None

    if request.user.is_authenticated:
        wishlist = WishListItem.objects.filter(user=request.user)
    else:
        wishlist = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")  # noqa: E501
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)  # noqa: E501
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'wishlist': wishlist,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    wishlist_exists = False
    wishlist = None

    if request.user.is_authenticated:
        try:
            wishlistitem = get_object_or_404(WishListItem, user=request.user)
        except Http404:
            wishlistitem = {}
            wishlist = None
        else:
            wishlist = wishlistitem.product.all()
            if product in wishlist:
                wishlist_exists = True

    reviews = Review.objects.filter(product=product)

    if request.method == 'POST':

        review_form = ReviewForm(data=request.POST or None)

        if request.user.is_authenticated and review_form.is_valid():

            review_form.instance.user = request.user
            review = review_form.save(commit=False)
            review.product = product
            review.save()
            messages.success(
                request, (
                    f'Thank you for reviewing "{product.name[:25]}.."! '
                    'You can now view and remove it below.'
                )
            )

            if product.rating:
                product.rating = (product.rating + review.product_rating) / 2
            else:
                product.rating = review.product_rating
            product.save()

            return redirect(reverse('product_detail', args=[product.id]))
    else:
        review_form = ReviewForm()
    context = {
        'product': product,
        'wishlist': wishlist,
        'review_form': review_form,
        'reviews': reviews,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')  # noqa: E501
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')  # noqa: E501
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


def delete_review(request, review_id):
    """
    Removes a product on the site
    """

    review = get_object_or_404(Review, pk=review_id)
    product = review.product

    try:
        review.delete()
        messages.success(
            request, (
                f'Your review "{review.title}" of {review.product} '
                'is now deleted'
            )
        )

    except Exception as e:  # pylint: disable=broad-except, invalid-name
        messages.error(request, f'Error removing review: {e}')
        return HttpResponse(status=500)

    return redirect(reverse('product_detail', args=[product.id]))
