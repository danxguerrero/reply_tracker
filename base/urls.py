from django.urls import path
from .views import ReplyList, ReplyDetail, ReplyCreate, ReplyUpdate, DeleteView, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', ReplyList.as_view(), name='replies'),
    path('reply/<int:pk>/', ReplyDetail.as_view(), name='reply'),
    path('reply-create/', ReplyCreate.as_view(), name='reply-create'),
    path('reply-update/<int:pk>/', ReplyUpdate.as_view(), name='reply-update'),
    path('reply-delete/<int:pk>/', DeleteView.as_view(), name='reply-delete'),
]