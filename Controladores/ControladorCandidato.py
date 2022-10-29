from Repositorios.RepositorioCandidato import RepositorioCandidato
from Modelos.Candidato import Candidato
class ControladorCandidato():
    def __init__(self):
        self.repositorioCandidato = RepositorioCandidato()
    def index(self):
        return self.repositorioCandidato.findAll()
    def create(self,infoCandidato):
        nuevoCandidato=Candidato(infoCandidato)
        return self.repositorioCandidato.save(nuevoCandidato)
    def show(self,id):
        elCandidato=Candidato(self.repositorioCandidato.findById(id))
        return elCandidato.__dict__
    def update(self,id,infoCandidato):
        CandidatoActual=Candidato(self.repositorioCandidato.findById(id))
        CandidatoActual.cedula=infoCandidato["cedula"]
        CandidatoActual.nombre = infoCandidato["nombre"]
        CandidatoActual.apellido = infoCandidato["apellido"]
        CandidatoActual.No_Resolucion = infoCandidato["No_Resolucion"]
        return self.repositorioCandidato.save(CandidatoActual)
    def delete(self,id):
        return self.repositorioCandidato.delete(id)