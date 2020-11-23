from django.urls import path
from . import views

urlpatterns=[
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path('emp', views.emp),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    path('candidate',views.candidate_view),
    path('data',views.data_view)

   ]



