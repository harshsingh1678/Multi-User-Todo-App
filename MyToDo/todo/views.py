from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'todo/home.html')

def todo_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority', 'M')
        
        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            due_date=due_date or None,
            priority=priority
        )
        return redirect('home')





    return render(request, 'todo/todo_list.html')