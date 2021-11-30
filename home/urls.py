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
    path('edit/', views.edit, name='edit'),
    path('logout/', views.logout, name='logout'),
    path('product/<str:id>', views.productDetail),
    path('addtocart/<str:id>', views.addToCart),
    # path('remove/<str:id>', views.removeFromCart),
    path('remove/', views.removeFromCart),
    # path('add/<str:id>', views.add),
    # path('sub/<str:id>', views.sub),
    path('add/', views.add),
    path('sub/', views.sub),
    path('search/', views.search, name='search'),
    path('order/', views.order, name='order'),
    path('pay/', views.pay, name='pay'),
    path('<str:category>/', views.category),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

