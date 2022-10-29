from Repositorios.RepositorioPartido import RepositorioPartido
from Repositorios.RepositorioMesa import RepositorioMesa
from Modelos.Partido import Partido
from Modelos.Mesa import Mesa
class ControladorPartido():
    def __init__(self):
        self.repositorioPartido = RepositorioPartido()
        self.repositorioMesa = RepositorioMesa()
    def index(self):
        return self.repositorioPartido.findAll()
    def create(self,infoPartido):
        nuevoPartido=Partido(infoPartido)
        return self.repositorioPartido.save(nuevoPartido)
    def show(self,id):
        elPartido=Partido(self.repositorioPartido.findById(id))
        return elPartido.__dict__
    def update(self,id,infoPartido):
        partidoActual=Partido(self.repositorioPartido.findById(id))
        partidoActual.nombre=infoPartido["nombre"]
        partidoActual.lema = infoPartido["lema"]
        return self.repositorioPartido.save(partidoActual)
    def delete(self,id):
        return self.repositorioPartido.delete(id)
    """
    Relación mesa y partido
    """
    def asignarMesa(self, id, id_mesa):
        partidoActual = Partido(self.repositorioPartido.findById(id))
        mesaActual = Mesa(self.repositorioMesa.findById(id_mesa))
        partidoActual.mesa = mesaActual
        return self.repositorioPartido.save(partidoActual)