from django.urls import path, include
from . import views
from django.conf.urls.static import static  # import de upload anh k bi loi
from django.conf import settings  # import de upload anh k bi loi
urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('forgot/', views.forgot, name='forgot'),
    path('news/', include('news.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
