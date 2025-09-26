import web

render = web.template.render('mvc/views/productos/')

class DetalleProducto:
    def __init__ (self):
        pass

    def GET(self):
        return render.detalle_producto()
        