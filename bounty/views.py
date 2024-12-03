from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Card, Bounty 


# def index(request):
    # card_list = Card.objects.order_by("card_market_price")[:10]
    # context = {"card_list": card_list}
    # return render(request, "bounty/index.html", context)

class IndexView(generic.ListView):
    template_name = "bounty/index.html"
    context_object_name = "card_list"

    def get_queryset(self):
        return Card.objects.order_by("mp")[:10]
    
class DetailView(generic.DetailView):
    model = Card
    template_name = "bounty/detail.html"

    def get_queryset(self):
        return super().get_queryset()

# def detail(request, card_id):
#     card = get_object_or_404(Card, pk=card_id)
#     return render(request, "bounty/detail.html", {"card": card})

# def bounty(request, card_id):
#     bounty = get_object_or_404(Bounty, pk=card_id)
#     return render(request, "bounty/bounty.html", {"bounty": bounty})
