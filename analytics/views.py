from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .utils import build_message_stats


"""Role: expose la page de statistiques utilisateur.
    Function: recupere les statistiques et rend le template.
    Context: utilise par le module analytics protege par login."""
@login_required
def stats_view(request):    
    context = build_message_stats(request.user)
    return render(request, "analytics/stats.html", context)
