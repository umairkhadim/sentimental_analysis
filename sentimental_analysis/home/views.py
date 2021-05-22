from django.shortcuts import render
from .models import *
from  .nlp.testFile import * 
from django.http import HttpResponse

# Create your views here.


# @login_required(login_url='login')
def customer_dashboard(request):
    products_obj = Product.objects.all()
    context = {

        "products": products_obj,

    }
    return render(request, 'home/dashboard.html', context)

def product_detail(request):

    product = request.GET.get('product')

    if request.is_ajax(): 
        rating = request.GET.get('rating')
        produc_obj = Product.objects.get(pk= product)
        new_rating_obj = Rating(rate_val=rating, product=produc_obj)
        new_rating_obj.save()
        return HttpResponse()

      
    produc_obj = Product.objects.get(pk= product)
         

    if request.method == 'POST': 
        new_comment = request.POST.get('comment') 
        comment_ = Comment(comment=new_comment, product=produc_obj) 
        comment_.save() 
          
    try:
        comments = Comment.objects.filter(product=produc_obj)  
        comments_list = list()
        for comment in comments:
            comments_list.append(comment)

        res=outputPredict(comments_list)   
    except:
        comments = None
        res={'positive':0,
            'negative':0}


    context={
        'product' : produc_obj,
        'comments' : comments,
        'positive_comments' : res['positive'],
        'negative_comments' : res['negative']
    }
    return render(request, 'home/product_detail.html', context)

