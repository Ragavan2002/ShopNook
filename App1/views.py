from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import Product, Order, OrderItem
from xhtml2pdf import pisa
from django.template.loader import get_template


def home(req):
    return render(req,"home.html")

def User_login(req):
    if req.method == "POST":
        username = req.POST.get('username')
        password = req.POST.get("password")
        if not username or not password:
            return HttpResponse("Error")
        user=authenticate(username=username,password=password)
        if user is not None:
            login(req,user)
            return redirect('product_list')
        else:
            return redirect('index')
    else:
        return render(req,"home.html")

def User_create(req):

    if req.method=="POST":
        username=req.POST.get("user_name")
        password=req.POST.get("password")
        confirm_password=req.POST.get("confirm_password")
        email=req.POST.get("email")
        if not username or not password or not confirm_password or not email:
            return HttpResponse("Error")
        if password == confirm_password:
            user=User.objects.create_user(username,email,password)
            user.save()
            return HttpResponse("User Created")
    else:
        return render(req,"create_user.html")

def product_list(request):
    username = request.user.username
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products,'username':username})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        order_item = OrderItem.objects.create(product=product, quantity=quantity)
        request.session['order_item'] = order_item.id
        return redirect('cart_view')
    context={'product': product}
    return render(request, 'product_detail.html', context)

def cart_view(request):
    order_item_id = request.session.get('order_item')
    if not order_item_id:
        return redirect('product_list')
    order_item = get_object_or_404(OrderItem, id=order_item_id)
    return render(request, 'cart.html', {'order_item': order_item})


def checkout_view(request):
    if request.method == 'POST':
        order_item_id = request.POST.get('order_item_id')
        if not order_item_id:
            return redirect('product_list')
        
        order_item = get_object_or_404(OrderItem, id=order_item_id)
        order = Order.objects.create()
        order.items.add(order_item)
        order.calculate_total()
        
        # Redirect to the bill generation page
        return redirect('download_bill', order_id=order.id)

    return redirect('product_list')




def generate_bill_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = order.items.all()

    total = sum(item.get_total_price() for item in order_items)
    template = get_template('bill.html')
    context = {
        'order': order,
        'order_items': order_items,
        'total': total,
        'host': request.get_host()
    }
    html = template.render(context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="bill_{order_id}.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('Error generating PDF')
    return response

def order_confirmation(request):
    return render(request, 'order_confirmation.html')


