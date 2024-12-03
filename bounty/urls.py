from django.urls import path

from . import views

app_name = "bounty"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # path("<int:card_id>/bounty/", views.BountyView.as_view(), name="bounty"),
    # path("<int[]:decklist>/", views.decklist, name="decklist")
    # path("<int[]:decklist>/bounty/" views.decklistbounty, name="decklistbounty")
]