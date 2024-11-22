from django.urls import path
from . import views

urlpatterns = [
    #list
    path('', views.index, name='index'),
    path('list/',views.list, name='list' ),
    path('write/',views.write, name='write'),
    path('write/write_ok/', views.write_ok, name='write_ok'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('update/update_ok/<int:id>', views.update_ok, name='update_ok'),
    
    path('login/', views.login, name='login'),
    path('login/login_ok/', views.login_ok, name='login_ok'),
    path('logout/', views.logout, name='logout'),
    
    #board
    path('boardlist/', views.boardlist, name='boardlist'),
    path('boardlist/write/',views.board_write, name='board_write'),
    path('boardlist/board_write_ok',views.board_write_ok, name='board_write_ok'),
    path('boardlist/content/<int:id>',views.board_content, name='board_content'),
    path('boardlist/update/<int:id>/',views.board_update, name='board_update'),
    path('boardlist/update/update_ok/<int:id>',views.board_update_ok, name='board_update_ok'),
    path('boardlist/delete/<int:id>/', views.board_delete, name='board_delete'),
    
    #template
    path('template1/', views.test1, name='template1'),
    path('template2/', views.test2, name='template2'),
    path('template3/', views.test3, name='template3'),
    path('template4/', views.test4, name='template4'),
    path('template5/', views.test5, name='template5'),
    path('template6/', views.test6, name='template6'),
    path('template7/', views.test7, name='template7'),
    path('template8/', views.test8, name='template8'),
    

]

