import json
from pyld import jsonld
from rdflib import Graph
from rdflib.tools import rdf2dot, rdfs2dot

def make_visual_graph(grafo):
    stream = open('grafo.dot','w')
    rdf2dot.rdf2dot(grafo, stream, format='json-ld')

#script para manipulação do arquivo de descrição dos dados tabulares
def main():
    file = 'HC_PACIENTES_1.csv-metadata.json'

    with open (file, 'r') as json_file:
        metadata = json.load(json_file)
        print(metadata["@context"][0])
        print(metadata["@context"][1]['@base'])

    #g = Graph().parse(data=file, format='json-ld')
    #make_visual_graph(g)

    #for x in metadata["tableSchema"]["columns"]:
    #    if x['@id'] == 'https://repositoriodatasharingfapesp.uspdigital.usp.br/HC_PACIENTES_1.csv/column/AA_NASCIMENTO':
            #print (x['datatype'])
    #        x['datatype'] = 'xsd:gYear'
            #print (x['@id'][:120])
    #with open ('PACIENTES.csv-metadata.json','w') as new_json:
    #    new_json.write (json.dumps(metadata, indent=True))
    #id_prefix = 'https://repositoriodatasharingfapesp.uspdigital.usp.br/HC_PACIENTES_1.csv/column/'



if __name__ == '__main__':
    main()
