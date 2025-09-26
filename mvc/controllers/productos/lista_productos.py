import web


render = web.template.render('mvc/views/productos/')

class ListaProductos:
    def __init__ (self):
        pass

    def GET(self):
        return render.lista_productos()