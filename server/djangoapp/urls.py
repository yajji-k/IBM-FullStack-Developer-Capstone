from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # path for registration
    path('register', views.registration, name='register'),

    # path for login
    path('login', views.login_user, name='login'),

    # path for logout
    path('logout', views.logout_request, name='logout'),

    # path to get cars
    path('get_cars', views.get_cars, name='getcars'),

    # path to get dealers
    path('get_dealers/', views.get_dealerships, name='get_dealers'),

    # path to get dealers by state
    path(
        'get_dealers/<str:state>',
        views.get_dealerships,
        name='get_dealers_by_state'
    ),

    # path to get dealer details
    path(
        'dealer/<int:dealer_id>',
        views.get_dealer_details,
        name='dealer_details'
    ),

    # path for dealer reviews view
    path(
        'reviews/dealer/<int:dealer_id>',
        views.get_dealer_reviews,
        name='dealer_details'
    ),

    # path for add a review view
    path('add_review', views.add_review, name='add_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
