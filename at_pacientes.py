import rdflib
from rdflib.namespace import XSD,DC,DCTERMS,VOID,XSD,RDF,RDFS,OWL
from rdflib import Graph, URIRef, Literal, Namespace, Dataset
from rdflib.tools import csv2rdf
import linecache
from iribaker import to_iri
import csv


def main():
	data = 'https://repositoriodatasharingfapesp.uspdigital.usp.br/'
	DATA = Namespace (data)

	graph_uri = URIRef('https://repositoriodatasharingfapesp.uspdigital.usp.br/graph')
	repoDtSh = Namespace ('https://repositoriodatasharingfapesp.uspdigital.usp.br/graph')
	dataset = Dataset()
	graph = dataset.graph(graph_uri)

	dataset.default_context.parse('',format='turtle')
	dataset.bind('datashIdAt', repoDtSh)

	#print(graph.serialize(format='turtle').decode('UTF-8'))
	with open('../dados/tabelas/HC_EXAMES_1.csv', mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file,delimiter='|')
		line_count = 0
		for row in csv_reader:
			if line_count == 0:
				line_count += 1
			else:
				graph.add((URIRef(graph_uri+row["ID_aTENDIMENTO"]),DATA.IdAtendimento, Literal(row["ID_aTENDIMENTO"])))
				graph.add((URIRef(graph_uri+row["ID_aTENDIMENTO"]), DATA.Id, Literal(row["ID_PACIENTE"], datatype=XSD.string)))
				graph.add((URIRef(graph_uri+row["ID_aTENDIMENTO"]), DATA.DtColeta, Literal(row["DT_COLETA"], datatype=XSD.date)))
				line_count += 1
	csv_file.close()
	graph.serialize(destination='../dados/abox/pacientes_id_at.ttl',format='turtle')

if __name__ == "__main__":
	main()
