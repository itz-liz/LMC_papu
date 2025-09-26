import web

urls = (
    '/', 'mvc.controllers.index.Index',
    '/lista_usuarios', 'mvc.controllers.usuarios.lista_usuarios.ListaUsuarios',
    '/detalle_usuarios', 'mvc.controllers.usuarios.detalle_usuarios.DetalleUsuarios',
    '/insertar_usuarios', 'mvc.controllers.usuarios.insertar_usuarios.InsertarUsuarios',
    '/detalle_producto', 'mvc.controllers.productos.detalle_producto.DetalleProducto',
    '/lista_productos', 'mvc.controllers.productos.lista_productos.ListaProductos',
    '/insertar_producto', 'mvc.controllers.productos.insertar_producto.InsertarProducto'
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
