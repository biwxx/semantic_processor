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

	dataset.default_context.parse('/T/dados/tbox/ontology_pacientes.ttl',format='turtle')
	dataset.bind('datashIdAt', repoDtSh)

	with open('/T/dados/tabelas/HC_PACIENTES_1.csv', mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file,delimiter='|')
		line_count = 0
		for row in csv_reader:
			if line_count == 0:
				line_count += 1
			#print(f'\t{row["ID_PACIENTE"]} mora em {row["CD_MUNICIPIO"]} e nasceu em {row["AA_NASCIMENTO"]}.')
			else:
				graph.add(( URIRef (graph_uri+row["ID_PACIENTE"]), DATA.Id, Literal(row["ID_PACIENTE"],datatype = XSD.string)))

				if row["IC_SEXO"] == 'F':
					graph.add(( URIRef(graph_uri+row["ID_PACIENTE"]), OWL.Class,  DATA.Woman ))
				else:
					graph.add(( URIRef(graph_uri+row["ID_PACIENTE"]), OWL.Class,  DATA.man ))

				graph.add((URIRef(graph_uri+row["ID_PACIENTE"]), DATA.CEP, Literal(row["CD_CEPREDUZIDO"], datatype=XSD.string)))
				if row["CD_MUNICIPIO"] != 'MMMM':
					graph.add(( URIRef (graph_uri+row["ID_PACIENTE"]), repoDtSh['MUNICIPIO'], Literal(row["CD_MUNICIPIO"],datatype = XSD.string)))
				line_count += 1

		print(f'Processadas {line_count} linhas.')
	csv_file.close()

	with open('/T/dados/tabelas/exames_test.csv', mode='r') as csv_file:
			csv_reader = csv.DictReader(csv_file,delimiter='|')
			line_count = 0
			for row in csv_reader:
				if line_count == 0:
					line_count += 1
				else:
					graph.add(( URIRef (graph_uri+row["ID_PACIENTE"]), DATA.IdAtendimento, Literal(row["ID_aTENDIMENTO"],datatype = XSD.string)))
					line_count += 1
	csv_file.close()
	graph.serialize(destination='/T/dados/abox/pacientes.ttl',format='turtle')
	#print(graph.serialize(format='turtle').decode('UTF-8'))


if __name__ == "__main__":
	main()
