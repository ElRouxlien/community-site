from django.shortcuts import render, redirect, get_object_or_404
from .models import Agent
from django.contrib.auth.decorators import login_required
from .forms import AgentForm



def agent_list(request):
    
    agents = Agent.objects.all()
    return render(request, 'agents/agent_list.html', {'agents': agents})


def agent_detail(request, pk):
    
    agent = get_object_or_404(Agent, pk=pk)
    return render(request, 'agents/agent_detail.html', {'agent': agent})
    

"""Role: cree un agent pour l utilisateur courant.
    Function: valide le formulaire et sauvegarde l agent.
    Context: accessible depuis l interface de creation d agent."""
@login_required
def agent_create(request):    
    if request.method == 'POST':
        form = AgentForm(request.POST, request.FILES)
        if form.is_valid():
            agent = form.save(commit=False)
            agent.owner = request.user
            agent.is_public = True
            agent.save()
            return redirect('agent-list')
    else:
        form = AgentForm()

    return render(request, 'agents/agent_create.html', {'form': form})

@login_required
def my_agents_view(request):
    agents = Agent.objects.filter(owner=request.user).order_by('-created_at')
    return render(request, 'agents/my_agents.html', {'agents': agents})


""" Role: modifie un agent de l utilisateur courant.
    Function: charge l agent, valide le formulaire et enregistre.
    Context: utilise depuis la page d edition d agent."""
@login_required
def agent_edit(request, pk):
    agent = get_object_or_404(Agent, pk=pk, owner=request.user)

    if request.method == "POST":
        form = AgentForm(request.POST, request.FILES, instance=agent)
        if form.is_valid():
            form.save()
            return redirect('my-agents')
    else:
        form = AgentForm(instance=agent)

    return render(request, 'agents/agent_edit.html', {'form': form, 'agent': agent})

@login_required
def agent_delete(request, pk):
    agent = get_object_or_404(Agent, pk=pk, owner=request.user)

    if request.method == "POST":
        agent.delete()
        return redirect('my-agents')

    return render(request, 'agents/agent_delete.html', {'agent': agent})

