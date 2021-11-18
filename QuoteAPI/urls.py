from django.contrib import admin
from django.urls import path, include
from quoteapp.views import APIViewQuotes, APIQuoteDetail, APIViewCategory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/quotes/', APIViewQuotes.as_view()),
    path('api/quotes/<str:pk>', APIQuoteDetail.as_view()),
    path('api/categories/', APIViewCategory.as_view()),
]
