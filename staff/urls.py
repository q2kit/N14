from django.urls import path, include
from . import views
from django.conf.urls.static import static  # import de upload anh k bi loi
from django.conf import settings  # import de upload anh k bi loi

urlpatterns = [
    path('', views.index, name='index'),
    path('addProduct', views.addProduct, name='addProduct'),
    path('order', views.order, name='order'),
    path('order/shipping/<str:id>', views.shipping, name='shipping'),
    path('order/done/<str:id>', views.done, name='done'),
    path('deleteProduct/<str:id>', views.deleteProduct, name='deleteProduct'),
    path('editProduct/<str:id>', views.editProduct, name='editProduct'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

