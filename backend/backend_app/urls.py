from django.urls import path
from . import views 

urlpatterns = [
    path('index' , views.index , name= 'index'),
    path('teams' , views.teams , name= 'teams'),
    path('update/<int:id>' , views.update , name= 'update'),
    path('delete/<int:id>' , views.delete , name= 'delete'),
    path('member_add' , views.add_member , name= 'add_member'),
    path('members_list' , views.members_list , name= 'members_list'),
    path('member_detail/<int:id>' , views.member_detail , name= 'member_detail'),
    path('revenue/add' , views.revenue_add , name= 'revenue_add'),
    path('revenues' , views.revenue_list , name= 'revenue_list'),
    path('revenue/<int:id>', views.revenue_detail, name='revenue_detail'),
    path('member/update/<int:id>', views.update_member, name='update_member'),
    path('member/delete/<int:id>/', views.delete_member, name='delete_member'),
    path('revenue/update/<int:id>/', views.update_revenue, name='update_revenue'),
    path('revenue/delete/<int:id>/', views.delete_revenue, name='delete_revenue'),
    path('expences/list', views.expences_list, name='expences_list'),
    path('expences/add/', views.expences_add, name='expences_add'),
    path('expences/<int:id>/remove/', views.expences_remove, name='expences_remove'),
    path('expences/<int:id>/update/', views.expences_update, name='expences_update'),
    path('expences/<int:id>/', views.expences_show, name='expences_show'),
    path('expences/main', views.expences, name='expences'),
    path('', views.login_view, name='login'),
    path('logout/', views.custom_logout, name='logout'),

]