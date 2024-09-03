from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def home(request):
    topics = Topic.objects.order_by('-date_added')
    context = {
        'topics':topics
    }
    return render(request, 'logs/topics.html', context)

def topic_detail(request, id):
    topic = Topic.objects.get(id = id)
    entries = topic.entry_set.all()

    context = {
        'topic':topic,
        'entries':entries,
    }
    return render(request, 'logs/topic_detail.html', context )

def index(request):
    return render(request, 'logs/home.html')

def new_topic(request):
    if request.method == ('POST' or None):
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logs_views')

    else:
        form = TopicForm()
    context = {
        'form':form
    }    
    return render(request, 'logs/new_topic.html', context)
def new_entry(request):
    if request.method == ('POST' or None ):
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logs_views')
    else:
        form = EntryForm() 
    return render(request, 'logs/new_entry.html', { 'form':form }) 

def list_entries(request, id):
    topic = Topic.objects.get(id = id)
    entries = topic.entry_set.all() 
    context = {
        'topic':topic,
        'entries':entries,
    }
    return render(request, 'logs/entries.html', context)

def edit_topic(request, id):
    topic = Topic.objects.get( id = id )
    if request.method == ('POST' or None):
        form = TopicForm(request.POST, instance = topic)
        if form.is_valid():
            form.save()
            return redirect('logs_views')
    else:
        form = TopicForm( instance = topic)
    context = {
        'form':form
    }    
    return render(request,'logs/edit_topic.html', context)


def edit_entry(request, entry_id):
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic
    
    print('entry:', entry)
    if request.method == ('POST' or None):
        instance = entry
        topic = entry.topic
        form = EntryForm( instance = entry, data=request.POST )
        if form.is_valid():
            form.save()
            return redirect('/')
        

    else:
        
        form = EntryForm(instance = entry)

    context = { 
        'topic':topic,
        'form':form,
        'entry':entry,

    }   
    
    return render(request, 'logs/edit_entry.html', context)

def delete_entry(request, entry_id):
    entry = Entry.objects.get(id = entry_id)
    entry.delete()
    return render(request, 'logs/delete_entry.html')

def confirm_delete(request, entry_id):
    entry = Entry.objects.get(id = entry_id)
    
    context =  {
        'entry':entry
    }
    return render(request, 'logs/confirm_delete.html', context)


    
    
    
