from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Review
from .forms import ClientReviewForm
from django.contrib.auth.decorators import login_required

def all_reviews(request):
    paramsAsc = request.GET.get('asc_votes', '')
    paramsDsc = request.GET.get('dsc_votes', '')
    paramsOldest = request.GET.get('first_added', '')
    if paramsAsc:
            reviews = Review.objects.all().order_by('-upvotes')
    elif paramsDsc:   
            reviews = Review.objects.all().order_by('-upvotes').reverse()
    elif paramsOldest:   
            reviews = Review.objects.all()
    else:
        reviews = Review.objects.all().order_by('-id')

    return render(request, "reviews.html", {'reviews': reviews})

asc_date=1

def review_detail(request, pk):
    if request.method == "GET":
        review = get_object_or_404(Review, pk=pk)
        review.save()
        return render(request, "review_detail.html", {'review': review})
    if request.method == "POST":
        review = get_object_or_404(Review, pk=pk)
        review.upvotes += 1
        review.save()
        return redirect('/reviews/', {'review': review})

@login_required
def create_or_edit_review(request, pk=None):
    review = get_object_or_404(Review, pk=pk) if pk else None
    if request.method == "POST":
        form = ClientReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save()
            return redirect('/reviews/', {'review': review})
    else:
        form = ClientReviewForm(instance=review)
    return render(request, 'client_review_form.html', {'form': form})

def upvotes(request, pk):
    if request.method == "POST":
        upvotes = get_object_or_404(Review, pk=pk)
        upvotes.upvotes += 1
        print(upvotes.upvotes)
        upvotes.save()
        return redirect('reviews.html')