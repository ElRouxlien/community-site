from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from agents.models import Agent
from .models import Message
from agents.ai import generate_reply
from django.utils import timezone
from datetime import timedelta
from django.http import JsonResponse



"""Role: gere la conversation avec un agent.
    Function: enregistre le message utilisateur, genere la reponse IA.
    Context: utilise par la page de chat principale."""
@login_required
def chat_view(request, pk):
    
    agent = get_object_or_404(Agent, pk=pk)

    if request.method == "POST":
        user_message = request.POST.get("message")

        if user_message and user_message.strip():

            last_message = Message.objects.filter(
                sender=request.user,
                agent=agent,
                is_user=True
            ).order_by('-timestamp').first()

            if last_message:
                elapsed = timezone.now() - last_message.timestamp
                if elapsed < timedelta(seconds=agent.cooldown):
                    return render(
                        request,
                        "chat/chat_page.html",
                        {
                            "agent": agent,
                            "messages": Message.objects.filter(agent=agent),
                            "error": f"Veuillez attendre {agent.cooldown} secondes entre deux messages."
                        }
                    )

            Message.objects.create(
                sender=request.user,
                agent=agent,
                content=user_message,
                is_user=True,
            )

            ai_answer = generate_reply(agent, user_message)

            Message.objects.create(
                sender=request.user,
                agent=agent,
                content=ai_answer,
                is_user=False,
            )

        return redirect("chat-view", pk=agent.pk)

    messages = Message.objects.filter(agent=agent).order_by("timestamp")
    return render(request, "chat/chat_page.html", {"agent": agent, "messages": messages})


""" Role: expose les messages d un agent en JSON.
    Function: serialize les messages pour le rafraichissement cote client.
    Context: utilise par la page de chat pour recuperer les messages."""
@login_required
def chat_messages_api(request, pk):
    
    messages = Message.objects.filter(agent_id=pk).order_by("timestamp")

    data = []
    for msg in messages:
        data.append({
            "id": msg.id,
            "sender": msg.sender.username if msg.is_user else msg.agent.name,
            "sender_id": msg.sender.id if msg.is_user else None,
            "agent_id": msg.agent.id,
            "content": msg.content,
            "is_user": msg.is_user,
        })

    return JsonResponse({"messages": data})
