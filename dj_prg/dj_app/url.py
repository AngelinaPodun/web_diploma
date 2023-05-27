from django.urls import path
from dj_app.views import *

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('news/', PostView.as_view(), name='news'),
    # Ссылка на конкретную новость по id (pk)
    path('news/<int:pk>/', PostDetail.as_view(), name='the_news'),
    path('review/<int:pk>/', AddComments.as_view(), name='add_comments'),
    path('form/', form, name='form'),
    path('<int:pk>/', ServiceDetail.as_view(), name='service'),
    path('sale/', SaleView.as_view(), name='sale'),
    path('sale/<int:pk>/', SaleDetail.as_view(), name='sale_detail'),
    path('about/', AboutView.as_view(), name='about'),
]