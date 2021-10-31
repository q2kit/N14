from django.urls import path, include
from . import views
from django.conf.urls.static import static  # import de upload anh k bi loi
from django.conf import settings  # import de upload anh k bi loi

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('forgot/', views.forgot, name='forgot'),
    path('account/', views.account, name='account'),
    path('logout/', views.logout, name='logout'),
    path('news/', include('news.urls')),
    path('product/<str:id>', views.productDetail),
    path('search/', views.search, name='search'),
    path('iphone/', views.iphone, name='iphone'),
    path('ipad/', views.ipad, name='ipad'),
    path('mac/', views.mac, name='mac'),
    path('watch/', views.watch, name='watch'),
    path('cart/', views.cart, name='cart'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
