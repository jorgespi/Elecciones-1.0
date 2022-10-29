from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultado import Resultado

from bson import ObjectId

class RepositorioResultado(InterfaceRepositorio[Resultado]):
    def getListadoInscritosEnPartido(self, id_partido):
        theQuery = {"partido.$id": ObjectId(id_partido)}
        return self.query(theQuery)
    def getMayorVotosPorMesa(self):
        query1={
                "$group": {
                    "_id": "$partido",
                    "max": {
                        "$max": "$nota_final"
                    },
                    "doc": {
                        "$first": "$$ROOT"
                    }
                }
            }
        pipeline=  [query1]
        return self.queryAggregation(pipeline)
    def promedioVotosEnPartido(self,id_partido):
        query1 = {
          "$match": {"partido.$id": ObjectId(id_partido)}
        }
        query2 = {
          "$group": {
            "_id": "$partido",
            "promedio": {
              "$avg": "$nota_final"
            }
          }
        }
        pipeline = [query1,query2]
        return self.queryAggregation(pipeline)