from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from app.models import Todo

def todoapp(request):
	todo_lists = Todo.objects.all()
	context={'skills':["HTML",
            "CSS",
            "javascript",
            "python",
            "django",
            "C言語",
            "java",
            "MySQL",
            "git",],'todo_lists': todo_lists}

	return render(request, "index.html",context)

#新しいtodoタスクが入力されたら保存
#HTMLにリダイレクト
def todo_post(request):
	todo_task = Todo(content = request.POST['content'])
	todo_task.save()
	return HttpResponseRedirect('/todo/')





#render(request, templatename, context=None)
#requestにはgetまたはpostの情報や、セッション情報が格納されている
#template_nameには表示させるHTMLファイルを指定する。
#注意点としてはtemplateフォルダをスタートとする相対パスで指定する。
#contextには辞書型のデータを指定する。データベース操作をして取得したデータなどを格納する。