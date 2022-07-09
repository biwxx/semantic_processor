import rdflib
from rdflib import Graph,ConjunctiveGraph
from rdflib.namespace import XSD,DC,DCTERMS,VOID,XSD,RDF,RDFS,OWL
from rdflib import Graph, URIRef, Literal, Namespace, Dataset
import re

def query_pacientes_id_at(g):
	q1 = '''
			PREFIX: <https://repositoriodatasharingfapesp.uspdigital.usp.br/>
			PREFIX datashIdAt: <https://repositoriodatasharingfapesp.uspdigital.usp.br/graph>
			PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

			SELECT DISTINCT ?id ?IdAtendimento
			WHERE { ?x :Id  ?id .
					?x :IdAtendimento ?IdAtendimento .
					}
	'''
	q2 = '''
			PREFIX: <https://repositoriodatasharingfapesp.uspdigital.usp.br/>
			PREFIX datashIdAt: <https://repositoriodatasharingfapesp.uspdigital.usp.br/graph>
			PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

			SELECT ?idAtendimento ?dtcoleta
			WHERE { ?x :DtColeta  ?dtcoleta .
					?x :IdAtendimento ?idAtendimento .
					}
			ORDER BY ?dtcoleta
	'''



	cnst1 = g.query(q1)

	for x in cnst1:
		print(f" Paciente Id: {x.id}, id de atendimento: {x.IdAtendimento}")

	for x in g.query(q2):
		print(f"{x.dtcoleta}, {x.idAtendimento}")


#identificando quais instâncias de exames pertencem a categoria de Observation conforme a ontolgoia do grupo query_dtsh_Haiss
#match com o termpo (string) na q1 e identificando quais e qntos pacientes no arquivo HC_EXAMES_SAMPLE tem os mesmo id

def query_identify_exams_urea(g):
	q1 = '''
			PREFIX : <https://repositoriodatasharingfapesp.uspdigital.usp.br/>
			PREFIX datashIdAt: <https://repositoriodatasharingfapesp.uspdigital.usp.br/graph>
			PREFIX owl: <http://www.w3.org/2002/07/owl#>
			PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

			SELECT DISTINCT ?exame ?id_ex
			WHERE { ?x :DeExame ?exame  .
					?id_ex :DeExame ?exame  .
					FILTER regex (?exame, "uréia", "i")
				}

	'''
	for x in g.query(q1):
		print(f"{x.id_ex}")


	q2= """
			PREFIX : <https://repositoriodatasharingfapesp.uspdigital.usp.br/>
			PREFIX vocab: <https://iisg.amsterdam/vocab/>
			PREFIX owl: <http://www.w3.org/2002/07/owl#>
			PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
			PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
			PREFIX xml: <http://www.w3.org/XML/1998/namespace>
			PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
			PREFIX schema: <http://schema.org/>
			PREFIX dtsh: <http://www.semanticweb.org/datasharingbr#>

			SELECT DISTINCT ?s ?id

			WHERE {
					?x vocab:ID_PACIENTE ?s.
					?y schema:identifier ?id.
					FILTER regex(?s, ?id)
			}

	"""
	count = 0
	for r in g.query(q2):
		print (r.s, r.id)
		count+= 1
	print (count)

def query_pacientes(g):
	q2 = '''
			PREFIX : <https://repositoriodatasharingfapesp.uspdigital.usp.br/>
			PREFIX datashIdAt: <https://repositoriodatasharingfapesp.uspdigital.usp.br/graph>
			PREFIX owl: <http://www.w3.org/2002/07/owl#>
			PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

			SELECT ?id ?MUNICIPIO
			WHERE { ?x :Id  ?id .
					?x datashIdAt:MUNICIPIO ?MUNICIPIO  .
					FILTER regex (?MUNICIPIO, "sao paulo", "i")
	}

	'''




	cnst2 = g.query(q2)
	#print ("Municipio:\n")
	for x in cnst2:
		print(f"{x.id}")


def query(g):
	consulta1= """
			PREFIX : <https://repositoriodatasharingfapesp.uspdigital.usp.br/>
			PREFIX vocab: <https://repositoriodatasharingfapesp.uspdigital.usp.br/vocab/>
			PREFIX owl: <http://www.w3.org/2002/07/owl#>
			PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
			PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
			PREFIX xml: <http://www.w3.org/XML/1998/namespace>
			PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

			SELECT ?s ?sexo

			WHERE {
					?x vocab:ID_PACIENTE ?s.
					?x   vocab:IC_SEXO ?sexo.
					FILTER regex (?sexo, "F")
			}
	"""
	for r in g.query(consulta1):
			print(r.s,r.sexo)



#listagem das instâncias segundo o modelo de propriedades utilizado
def query_dtsh_Haiss(g):
	consulta_paciente_id = """
			PREFIX schema: <http://schema.org/>
			PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
			PREFIX owl: <http://www.w3.org/2002/07/owl#>
			PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
			PREFIX foaf: <http://xmlns.com/foaf/0.1/>


			SELECT ?id

			WHERE {
					?x schema:identifier ?id.
					FILTER regex (?id, "00006490d57666d73747c29c01079b60b1353002")
			}
	"""
	for r in g.query(consulta1):
			print(r.id)


	ct2_scale= """
			PREFIX schema: <http://schema.org/>
			PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
			PREFIX owl: <http://www.w3.org/2002/07/owl#>
			PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
			PREFIX foaf: <http://xmlns.com/foaf/0.1/>
			PREFIX dtsh: <http://www.semanticweb.org/datasharingbr#>

			SELECT DISTINCT ?scale

			WHERE {
					?x ?id_atendimento dtsh:Measurement.
					?y schema:codeValue ?scale
					FILTER regex (?scale, "LP7753-9")
			}


	"""
	count = 0
	for x in g.query(ct2_scale):
		print(x.scale)
		count +=1
	print ('- datasharingbr#hasScale',count)



	ct2_unit= """
			PREFIX schema: <http://schema.org/>
			PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
			PREFIX owl: <http://www.w3.org/2002/07/owl#>
			PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
			PREFIX foaf: <http://xmlns.com/foaf/0.1/>
			PREFIX dtsh: <http://www.semanticweb.org/datasharingbr#>

			SELECT DISTINCT ?unit

			WHERE {
					?x dtsh:hasUnit ?unit
			}


	"""

	count = 0
	for x in g.query(ct2_unit):
		print (x.unit)
		count +=1
	print ('- datasharingbr#hasUnit',count)


	ct2_careSite="""
			PREFIX schema: <http://schema.org/>
			PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
			PREFIX owl: <http://www.w3.org/2002/07/owl#>
			PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
			PREFIX foaf: <http://xmlns.com/foaf/0.1/>
			PREFIX dtsh: <http://www.semanticweb.org/datasharingbr#>

			SELECT DISTINCT ?care_site

			WHERE {
					?x dtsh:hasCareSite ?care_site
			}

	"""
	count = 0
	for x in g.query(ct2_careSite):
		print (x.care_site)
		count +=1
	print ('- datasharingbr#hasCareSite',count)

	ct2_property="""
			PREFIX schema: <http://schema.org/>
			PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
			PREFIX owl: <http://www.w3.org/2002/07/owl#>
			PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
			PREFIX foaf: <http://xmlns.com/foaf/0.1/>
			PREFIX dtsh: <http://www.semanticweb.org/datasharingbr#>

			SELECT DISTINCT ?property

			WHERE {
					?x dtsh:hasProperty ?property
			}

	"""
	count = 0
	for x in g.query(ct2_property):
		print (x.property)
		count +=1
	print ('- datasharingbr#hasProperty',count)

	ct2_patient="""
			PREFIX schema: <http://schema.org/>
			PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
			PREFIX owl: <http://www.w3.org/2002/07/owl#>
			PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
			PREFIX foaf: <http://xmlns.com/foaf/0.1/>
			PREFIX dtsh: <http://www.semanticweb.org/datasharingbr#>

			SELECT DISTINCT ?patient

			WHERE {
					?x dtsh:hasPatient ?patient
			}

	"""
	count = 0
	for x in g.query(ct2_patient):
		#print (x.patient)
		count +=1
	print ('- datasharingbr#hasPatient',count)

	ct2_concept="""
			PREFIX schema: <http://schema.org/>
			PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
			PREFIX owl: <http://www.w3.org/2002/07/owl#>
			PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
			PREFIX foaf: <http://xmlns.com/foaf/0.1/>
			PREFIX dtsh: <http://www.semanticweb.org/datasharingbr#>

			SELECT DISTINCT ?concept

			WHERE {
					?x dtsh:hasConcept ?concept
			}

	"""
	count = 0
	for x in g.query(ct2_concept):
		print (x.concept)
		count +=1
	print ('- datasharingbr#hasConcept',count)

#listagem mais detalhada conforme o modelo de conceito e vocabulario(vocab)
def observation_specimen_dtsh_Haiss(g):
	observation="""
			PREFIX schema: <http://schema.org/>
			PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
			PREFIX owl: <http://www.w3.org/2002/07/owl#>
			PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
			PREFIX foaf: <http://xmlns.com/foaf/0.1/>
			PREFIX dtsh: <http://www.semanticweb.org/datasharingbr#>

			SELECT DISTINCT ?concept ?vocab

			WHERE {
					?x schema:codeValue ?concept .
					?x schema:codeSystem ?vocab
					FILTER regex (?concept, "LP14288-2")
			}

		"""
	count = 0
	for x in g.query(observation):
		print (x.concept, x.vocab)

	ct2_observation="""
			PREFIX schema: <http://schema.org/>
			PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
			PREFIX owl: <http://www.w3.org/2002/07/owl#>
			PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
			PREFIX foaf: <http://xmlns.com/foaf/0.1/>
			PREFIX dtsh: <http://www.semanticweb.org/datasharingbr#>

			SELECT ?observation

			WHERE {
					?x dtsh:hasObservation ?observation
			}
	"""
	count = 0
	for x in g.query(ct2_observation):
		count +=1
	print(count)
	print (x.observation)



	specimen = """
			PREFIX schema: <http://schema.org/>
			PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
			PREFIX owl: <http://www.w3.org/2002/07/owl#>
			PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
			PREFIX foaf: <http://xmlns.com/foaf/0.1/>
			PREFIX dtsh: <http://www.semanticweb.org/datasharingbr#>

			SELECT DISTINCT ?concept ?vocab

			WHERE {
					?x a dtsh:Specimen .
					?x schema:codeValue ?concept .
					?x dtsh:codeSystem ?vocab
			}


		"""
	count = 0
	for x in g.query(specimen):
		print (x.concept, x.vocab)


	ct2_specimen= """
						PREFIX schema: <http://schema.org/>
						PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
						PREFIX owl: <http://www.w3.org/2002/07/owl#>
						PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
						PREFIX foaf: <http://xmlns.com/foaf/0.1/>
						PREFIX dtsh: <http://www.semanticweb.org/datasharingbr#>

						SELECT ?specimen

						WHERE {
								?x ?id_atendimento dtsh:Measurement.
								?y schema:codeValue ?specimen
								FILTER regex (?specimen, "119364003")
						}


				"""

	count = 0
	for x in g.query(ct2_specimen):
		count +=1
	print (count)
	print(x.specimen)





def conjunctive_dtsh():
	gnq = ConjunctiveGraph()

	#gnq.parse('dados/abox/pacientes_id_at.ttl',format='ttl')
	gnq.parse('dados/abox/test_exames.ttl',format='ttl')
	#gnq.parse('dados/abox/HC_PACIENTES_1.nq', format='nquads')
	gnq.parse('dados/abox/measurements-csv-sample.ttl', format='ttl')
	gnq.parse('dados/abox/EINSTEIN_Exames_2_SAMPLE.csv.nq')

	#query_identify_exams_urea(gnq)
	query_pacientes_id_at(gnq)
	#query_dtsh_Haiss(gnq)
	#observation_specimen_dtsh_Haiss(gnq)


if __name__ == "__main__":
	conjunctive_dtsh()
