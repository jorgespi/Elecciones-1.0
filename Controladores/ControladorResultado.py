from Modelos.Resultado import Resultado
from Modelos.Candidato import Candidato
from Modelos.Partido import Partido
from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioPartido import RepositorioPartido
class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioPartido = RepositorioPartido()
    def index(self):
        return self.repositorioResultado.findAll()
    """
    Asignacion candidato y partido a resultado
    """
    def create(self,infoResultado,id_Candidato,id_Partido):
        nuevaResultado=Resultado(infoResultado)
        elCandidato=Candidato(self.repositorioCandidato.findById(id_Candidato))
        elPartido=Partido(self.repositorioPartido.findById(id_Partido))
        nuevaResultado.Candidato=elCandidato
        nuevaResultado.Resultado=elPartido
        return self.repositorioResultado.save(nuevaResultado)
    def show(self,id):
        elResultado=Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__
    """
    Modificación de Resultado (candidato y partido)
    """
    def update(self,id,infoResultado,id_Candidato,id_Partido):
        elResultado=Resultado(self.repositorioResultado.findById(id))
        elResultado.partido=infoResultado["partido"]
        elResultado.candidato = infoResultado["candidato"]
        elResultado.votoFinal=infoResultado["Voto_final"]
        elCandidato = Candidato(self.repositorioCandidato.findById(id_Candidato))
        elPartido = Partido(self.repositorioPartido.findById(id_Partido))
        elResultado.Candidato = elCandidato
        elResultado.Partido = elPartido
        return self.repositorioResultado.save(elResultado)
    def delete(self, id):
        return self.repositorioResultado.delete(id)
    "Obtener todos los resultados en un partido"
    def listarResultadosEnPartido(self,id_Partido):
        return self.repositorioResultado.getListadoInscritosEnPartido(id_Partido)
    "Obtener votos mas altos por mesa"
    def votosMasAltosPorMesa(self):
        return self.repositorioResultado.getMayorVotosPorMesa()
    "Obtener promedio de votos en partido"
    def promedioVotosEnPartido(self,id_Partido):
        return self.repositorioResultado.promedioVotosEnPartido(id_Partido)