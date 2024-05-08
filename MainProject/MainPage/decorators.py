from django.shortcuts import redirect

def CheckGroup(view_fun):
    def innerFun(request):
        if request.user.groups.all()[0].name == 'owner':
            return view_fun(request)
        else:
            return redirect('entranceurl')
    return innerFun

def CheckpgSearch(view_fun):
    def innerFun(request):
        if request.user.groups.all()[0].name == 'student':
            return view_fun(request)
        else:
            return redirect('entranceurl')
    return innerFun