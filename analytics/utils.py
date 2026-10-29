from django.db.models import Count
from django.db.models.functions import TruncDate
from chat.models import Message

""" Role: centralise les statistiques de messages d un utilisateur.
    Function: calcule totaux et aggregations par agent et par jour.
    Context: utilise par les vues analytics et profil utilisateur."""
def build_message_stats(user):
    user_messages = Message.objects.filter(sender=user)

    total_messages = user_messages.count()
    total_ai_messages = Message.objects.filter(
        agent__owner=user,
        is_user=False
    ).count()

    messages_per_agent = user_messages.values('agent__name').annotate(
        count=Count('id')
    ).order_by('-count')

    messages_per_day = user_messages.annotate(
        date=TruncDate('timestamp')
    ).values('date').annotate(
        count=Count('id')
    ).order_by('date')

    return {
        "total_messages": total_messages,
        "total_ai_messages": total_ai_messages,
        "messages_per_agent": messages_per_agent,
        "messages_per_day": messages_per_day,
    }
