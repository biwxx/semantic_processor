import rdflib
from rdflib.namespace import XSD,DC,DCTERMS,VOID,XSD,RDF,RDFS,OWL
from rdflib import Graph, URIRef, Literal, Namespace, Dataset
from rdflib.tools import csv2rdf
import linecache
from iribaker import to_iri
import csv


def create():
	data = 'https://repositoriodatasharingfapesp.uspdigital.usp.br/'
	DATA = Namespace (data)

	graph_uri = URIRef('https://repositoriodatasharingfapesp.uspdigital.usp.br/graph')
	repoDtSh = Namespace ('https://repositoriodatasharingfapesp.uspdigital.usp.br/graph')
	dataset = Dataset()
	graph = dataset.graph(graph_uri)

	dataset.default_context.parse('/T/dados/tbox/ontology_pacientes.ttl',format='turtle')
	dataset.bind('datashIdAt', repoDtSh)


	with open('/T/dados/tabelas/exames_test.csv', mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file,delimiter='|')
		line_count = 0
		id_exame = 0
		id_analito = 0
		for row in csv_reader:
			if line_count == 0:
				print(f' {", ".join(row)}')
				line_count += 1
			else:
				graph.add((URIRef(graph_uri+'_id_EXAME-'+str(id_exame)),DATA.DeExame,Literal(row["DE_EXAME"], datatype=XSD.string) ))
				graph.add((URIRef(graph_uri+'_id_ANALITO-'+str(id_analito)),DATA.DeAnalito,Literal(row["DE_ANALITO"], datatype=XSD.string) ))
				line_count += 1
				id_exame += 1
				id_analito += 1
	csv_file.close()
	graph.serialize(destination='/home/biwxx/Documents/IWS/T_final/dados/abox/test_exames.ttl',format='turtle')

#script p insercao das propriedades do common data model
def include_property():
	gnq = Graph()
	gnq.parse('dados/abox/test_exames.ttl',format='ttl')

	datashIdAt = Namespace("https://repositoriodatasharingfapesp.uspdigital.usp.br/")
	schema = Namespace("http://schema.org/")
	for s in gnq.subjects(RDF.type,datashIdAt.):
		print(s)
		for objects in gnq.objects (s, datashIdAt.DeAnalito):
			if Literal(objects, datatype=XSD.string) == Literal('URÉIA',datatype=XSD.string):
				gnq.add(s, schema.codeValue, Literal("LP14288-2", datatype=XSD.string))



if __name__ == "__main__":
	create()
	#include_property()
