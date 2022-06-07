from django.shortcuts import render
from django.http import HttpResponseRedirect
from app.models import Todo
from app.models import Skill
from datetime import date
from dateutil.relativedelta import relativedelta

d0 = date(1999,9,26) #私の生年月日
d1 = date.today() #今日の年月日
myage = relativedelta(d1,d0) #今日の年月日-私の生年月日
myage = myage.years #現在の自分の年齢

def portfolioapp(request):
    todo_lists = Todo.objects.all()     
    skill_lists = Skill.objects.all()

    context={
            'todo_lists': todo_lists,
            'skill_lists': skill_lists,
            "myage":myage,}
    

    return render(request, "index.html",context)

#新しいtodoタスクが入力されたら保存
#HTMLにリダイレクト
def todo_post(request):
	add_task = Todo(content = request.POST['content'])
	add_task.save()
	return HttpResponseRedirect('/todo/')

def todo_remove(request,task_id):
    remove_task = Todo.objects.get(id=task_id)
    remove_task.delete()
    return HttpResponseRedirect('/todo/#index3')

#render(request, templatename, context=None)
#requestにはgetまたはpostの情報や、セッション情報が格納されている
#template_nameには表示させるHTMLファイルを指定する。
#注意点としてはtemplateフォルダをスタートとする相対パスで指定する。
#contextには辞書型のデータを指定する。データベース操作をして取得したデータなどを格納する。