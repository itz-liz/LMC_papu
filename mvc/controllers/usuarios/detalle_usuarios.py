import web

render = web.template.render('mvc/views/usuarios/')

class DetalleUsuarios:
    def __init__ (self):
        pass

    def GET(self):
        return render.detalle_usuarios()
        