from django.views.generic import TemplateView


class Index(TemplateView):
	template_name = "index.html"

	def get_context_data(self):
		ctxt = super().get_context_data()
		ctxt["skills"] = [
			"HTML",
            "CSS",
            "javascript",
            "python",
            "django",
            "C言語",
            "java",
            "MySQL",
            "git",
		]
		return ctxt




#render(request, templatename, context=None)
#requestにはgetまたはpostの情報や、セッション情報が格納されている
#template_nameには表示させるHTMLファイルを指定する。
#注意点としてはtemplateフォルダをスタートとする相対パスで指定する。
#contextには辞書型のデータを指定する。データベース操作をして取得したデータなどを格納する。