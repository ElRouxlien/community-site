from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from chat.models import Message
from agents.models import Agent
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from analytics.utils import build_message_stats


"""Role: gere l inscription d un nouvel utilisateur.
    Function: valide le formulaire et cree le compte.
    Context: utilise par la page d inscription publique."""
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

"""Role: affiche et met a jour le profil courant.
    Function: gere les formulaires utilisateur et profil, affiche stats.
    Context: utilise par la page profil connectee."""
@login_required
def profile(request):
    stats_context = build_message_stats(request.user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    context.update(stats_context)

    return render(request, 'users/profile.html', context)



"""Role: affiche le profil public d un utilisateur.
    Function: liste ses agents et statistiques publiques.
    Context: utilise par les pages publiques de profil."""
@login_required
def public_profile(request, user_id):
    profile_user = get_object_or_404(User, pk=user_id)

    agents = Agent.objects.filter(owner=profile_user).order_by('-created_at')

    user_messages = Message.objects.filter(sender=profile_user)
    messages_per_agent = user_messages.values('agent__name').annotate(
        count=Count('id')
    ).order_by('-count')

    messages_per_day = None
    if request.user.is_authenticated and request.user == profile_user:
        messages_per_day = user_messages.annotate(
            date=TruncDate('timestamp')
        ).values('date').annotate(
            count=Count('id')
        ).order_by('date')

    context = {
        "profile_user": profile_user,
        "agents": agents,
        "messages_per_agent": messages_per_agent,
        "messages_per_day": messages_per_day,
    }

    return render(request, "users/public_profile.html", context)
