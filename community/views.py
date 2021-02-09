from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Review
from .forms import ReviewForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    review_list = Review.objects.order_by('-create_date')  # '-' : 역순
    context = {'review_list': review_list}

    return render(request, 'community/community.html', context)

def detail(request, review_id) :
    review = get_object_or_404(Review, pk=review_id)
    context = {'review': review}
    return render(request, 'community/review_detail.html', context)

@login_required(login_url='login')
def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.create_date = timezone.now()
            review.author = request.user
            review.save()
            return redirect('community:index')
    else:
        form = ReviewForm()
    context = {'form': form}
    return render(request, 'community/community.html', context)

@login_required(login_url='login')
def comment_create(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.create_date = timezone.now()
            comment.review = review
            comment.author = request.user
            comment.save()
            return redirect('community:detail', review_id=review.id)
    else:
        form = CommentForm()
    context = {'review': review, 'form': form}
    return render(request, 'community/review_detail.html', context)