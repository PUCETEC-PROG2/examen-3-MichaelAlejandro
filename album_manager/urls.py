from django.urls import path

from . import views

app_name = "album_manager"
urlpatterns = [
    path("", views.artist, name="artist"),
    path("artist/<int:artist_id>/", views.artist_info, name="artist_info"),
    path("add_artist/", views.add_artist, name="add_artist"),
    path("edit_artist/<int:id>/", views.edit_artist, name="edit_artist"),
    path("delete_artist/<int:id>/", views.delete_artist, name="delete_artist"),
    path("album/", views.album, name="album"),
    path("album/<int:album_id>/", views.album_info, name="album_info"),
    path("add_album/", views.add_album, name="add_album"),
    path("edit_album/<int:id>/", views.edit_album, name="edit_album"),
    path("delete_album/<int:id>/", views.delete_album, name="delete_album"),
]