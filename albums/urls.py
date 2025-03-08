from django.urls import path
from .views import CreateAlbumView, GetAllAlbumView, GetAllSongByAlbumIdView, DeleteAlbumByIdView

urlpatterns = [
    path('', GetAllAlbumView.as_view(), name='get-all-album'),
    path('create-album/<uuid:userId>/', CreateAlbumView.as_view(), name='create-album'),
    path('get-all-song-by-album-id/<uuid:albumId>/', GetAllSongByAlbumIdView.as_view(), name='get-all-song-by-album-id'),
    path('delete-album-by-id/<uuid:albumId>/', DeleteAlbumByIdView.as_view(), name='delete-album-by-id'),
]
