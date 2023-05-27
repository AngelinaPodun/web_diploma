from django.shortcuts import render, redirect
from django.views.generic.base import View
from .form import *


class Index(View):

    def get(self, request):
        services = Service.objects.all()
        subscribe = 'Подпишитесь на наши новости и вы будете в курсе новостей первыми.'
        context = {'services': services, 'subscribe': subscribe}
        subscriber_form = SubscriberForm()
        context['form'] = subscriber_form
        return render(request, 'index.html', context)

    def post(self, request):
        services = Service.objects.all()
        context = {'services': services}
        subscriber_form = SubscriberForm(request.POST)
        if subscriber_form.is_valid():
            subscriber = Subscriber(
                email=subscriber_form.cleaned_data['email']
            )
            subscriber.save()
            context = {'success': 1}
        return render(request, 'index.html', context)


def form(request):
    context = {}
    if request.method == 'GET':
        order_form = OrderForm()
        context = {'form': order_form, 'words': 'Запись на процедуру:',
                   'words_2': 'Заполните форму и мы свяжемся с вами.', 'success': 'True'}
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        details = request.POST.get('details')
        data = request.POST.get('data')
        Order(name=name, phone=phone, email=email, details=details, data=data).save()
        context.update({'user_name': name, 'words': 'Спасибо!', 'words_2': 'Мы скоро с Вами свяжемся!'})
    return render(request, 'form.html', context)


class ServiceView(View):

    def get(self, request):
        services = Service.objects.all()
        return render(request, 'index.html', {'services': services})


class ServiceDetail(View):

    def get(self, request, pk):
        service = Service.objects.get(id=pk)
        return render(request, 'service_detail.html', {'service': service})


class PostView(View):

    def get(self, request):
        posts = list(Post.objects.all())
        # print(posts.reverse())
        context = {'post_list': posts}
        return render(request, 'news.html', context=context)

    def post(self, request):
        context = {}
        return render(request, 'news.html', context)


# Выводим страницу новости по id
class PostDetail(View):

    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'news_detail.html', {'post': post})


class AddComments(View):
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/news/{pk}')  # Возврат к конкретной новости по id


class SaleView(View):

    def get(self, request):
        info = list(Sale.objects.all())
        # print(info.reverse())
        context = {'info': info}
        return render(request, 'sale.html', context=context)


class SaleDetail(View):

    def get(self, request, pk):
        sale = Sale.objects.get(id=pk)
        return render(request, 'sale_detail.html', {'sale': sale})


class AboutView(View):

    def get(self, request):
        workers = Worker.objects.all()
        our_works = Images.objects.all()
        context = {'workers': workers, 'our_works': our_works}

        return render(request, 'about.html', context)
