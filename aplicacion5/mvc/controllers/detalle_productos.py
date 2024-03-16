import web
from ..models.modelo_productos import ModeloProductos

PRODUCTO = ModeloProductos()
render = web.template.render('mvc/views/', base='layout')
class DetalleProductos:

    def GET(self, idProductos):
        try:
            producto = PRODUCTO.detalleProductos(idProductos)
            return render.detalle_productos(producto)
        except Exception as error:
            print(f'Ocurrió un error {error} - 103 | Controlador')
            return 'Ocurrió un error'