from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .models import TodoList

def index(request): 
    todos = TodoList.objects.all() 
    if request.method == "POST":
        if "taskAdd" in request.POST:
            title = request.POST["thetitle"] 
            date = str(request.POST["date"])
            content = request.POST["description"]  
            complete = request.POST.get('taskComplete', False) 
            category = request.POST["category_select"] 
            Todo = TodoList(title=title, content=content, category=category, due_date=date)
            Todo.save() 
            return redirect("/") 
        if "taskDelete" in request.POST:
            checkedlist = request.POST.getlist("checkedbox") 
            for todo_id in checkedlist:
                todo_id = int(todo_id)
                todo = TodoList.objects.get(id = todo_id)
                
            todo.delete() 
            return redirect("/") 
    return render(request, "index.html", {"todos": todos})