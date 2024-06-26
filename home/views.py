from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from django.contrib import messages
from .models import Product, Contact, Blog, About, TestModel, Order
from django.db.models import Q
from .forms import OrderForm

from .models import Product, About
from django.core.paginator import Paginator


class HomePageView(View):
     def get(self, request ):
          random_four_testimonials= TestModel.objects.filter(is_active = True).order_by('?')[:4]
          products = Product.objects.filter(is_active=True)
          random_three_products=products.order_by('?')[:3]
          blok = Blog.objects.all().order_by('?')[:3]
          conttext = {
               'product': products,
               'random_four_testimonials':random_four_testimonials,
               'random_three_products':random_three_products,
               'blok': blok,
          }
          return render(request, 'index.html', conttext)



class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

    
    def post(self, request):
        data=request.POST
        contact=Contact()

        contact.name=data.get('name')
        contact.email=data.get('email')
        contact.subject=data.get('subject')
        contact.message=data.get('message')

        contact.save()

        messages.success(request, 'Malumotlaringiz yuborildi.')
        return render(request, 'contact.html')



class BlogView(View):
    def get(self, request):
        blok = Blog.objects.all()
        context = {
            'blok': blok,
        }
        
        return render(request, 'blog.html', context)



class BlogDetailView(View):
    def get(self, request, uuid):
        detail = get_object_or_404(Blog, id=uuid)
        detail.views+=1
        detail.save()
        
        context = {
            'detail': detail,
        }

        return render(request, 'blog-details.html', context)



class AboutView(View):
    def get(self, request):
        about = About.objects.all()
        context = {
            'about': about,
        }

        return render(request, 'about.html', context)



class SearchView(View):
    def get(self, request):
        query = request.GET.get('q')
        if not query:
            messages.error(request, "Bunday mahsulot topilmadi!")
            return redirect('index')

        searchs = Blog.objects.all().filter(Q(title__icontains = query) | Q(description__icontains = query))


        context = {
            'searchs': searchs,
        }
        messages.success(request, "Siz qidirgan mahsulotlar.")
        return render(request, 'search.html', context)

      
class AllProductView(View):
    def get(self, request):

        products_all = Product.objects.all().filter(is_active = True)

        page_size=request.GET.get('page_size', 8)
        paginator = Paginator(products_all, page_size)

        page = request.GET.get('page', 1)
        page_obj = paginator.page(page)
        context = {
            'products_all':page_obj,
            
        }

        return render(request, "products.html", context)




class ProductDetailView(View):
    def get(self, request, uuid):
        product=Product.objects.filter(is_active = True, id=uuid).first()

        context = {
            'product':product
        }
        
        return render(request, 'product-details.html', context)

    def post(self, request, uuid):
        quantity = request.POST.get('quantity')
        print(quantity)
        product = Product.objects.filter(id=uuid).first()
        order = Order.objects.create(
            product=product,
            quantity=quantity,
        )

        return redirect('checkout', uuid=order.id)

class AboutView(View):
    def get(self, request):
        all_about=About.objects.all().filter(is_active=True)
        # chosen_about=all_about.filter(id=id)

        context = {
            'all_about':all_about
        }
        

        return render(request, 'about.html', context)



class SharhlarView(View):
    def get(self, request):
        all_testimonials = TestModel.objects.filter(is_active=True)
        numberrr=int(all_testimonials.count()/2)
        print(numberrr)
        context = {
            'all_testimonials':all_testimonials,
            'numberrr':numberrr
        }

        return render(request, 'testimonials.html', context) 


class CheckoutView(View):
    def get(self, request, uuid):
        order = Order.objects.filter(id=uuid).first()
        form = OrderForm()

        context = {
            'order': order,
            'form': form
        }

        context = {
            'order': order,
            'form': form
        }
        return render(request, 'checkout.html', context)

    def post(self, request, uuid):
        order = Order.objects.filter(id=uuid).first()
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            order.status = True
            order.save()
            print("saqlandi")
            messages.success(request, 'Zakasingiz qabul qilindi.')
            return redirect('index')
        messages.warning(request, 'Nimadir xato ketdi.')
        return redirect('checkout', uuid=order.id)

