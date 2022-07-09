import rdflib
from rdflib.namespace import XSD,DC,DCTERMS,VOID,XSD,RDF,RDFS,OWL
from rdflib import Graph,Namespace
from rdflib.tools import csv2rdf
from rdflib.tools import rdf2dot, rdfs2dot
import linecache
import csv

def main():

	#fapesp = Namespace("https://repositoriodatasharingfapesp.uspdigital.usp.br#")
	#g = Graph().parse('ontology_pacientes.ttl',format='turtle')
	#test = Graph().parse('test.ttl',format='turtle')
	ontology_hosp = Graph().parse("DTSH-FAP-USP_ontology.ttl",format='ttl')
	#assigment_5_1.serialize(destination='simpJoin',format='xml')

	for s in ontology_hosp.subjects():
		print (s)



	stream = open('ontology.dot','w')
	rdf2dot.rdf2dot (ontology_hosp, stream, 'ttl')
	stream.close()


if __name__ == "__main__":
	main()
