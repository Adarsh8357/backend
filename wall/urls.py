from django.urls import path
from . import views
from .views import register_view
urlpatterns = [
    path('', views.sticky_wall, name='sticky_wall'),  # Home page
    path('login/', views.login_view, name='login'),
    path('wall/', views.sticky_wall, name='sticky_wall'),
    path('complete/<int:note_id>/', views.complete_note, name='complete_note'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
    path('edit/<int:note_id>/', views.edit_note, name='edit_note'),
    # API endpoints
    path('api/notes/', views.NoteListCreateAPIView.as_view(), name='note-list-create'),
    path('api/notes/<int:pk>/', views.NoteRetrieveUpdateDestroyAPIView.as_view(), name='note-detail'),
    path('register/', register_view, name='register'),
]
