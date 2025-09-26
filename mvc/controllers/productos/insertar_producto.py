import web


render = web.template.render('mvc/views/productos/')

class InsertarProducto:
    def __init__ (self):
        pass

    def GET(self):
        return render.insertar_producto()
        