from django.shortcuts import render


def index(request):
	return render(request, 'index.html') 


#render(request, templatename, context=None)
#requestにはgetまたはpostの情報や、セッション情報が格納されている
#template_nameには表示させるHTMLファイルを指定する。
#注意点としてはtemplateフォルダをスタートとする相対パスで指定する。
#contextには辞書型のデータを指定する。データベース操作をして取得したデータなどを格納する。