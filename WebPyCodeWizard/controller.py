import web
from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')

urls = (
    '/', 'home'
)

render = web.template.render("Views/Templates", base="MainLayout")
app = web.application(urls, globals())


class home:
    def GET(self):
        return render.Home()


if __name__ == "__main__":
    app.run()