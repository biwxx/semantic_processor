from rdflib import Graph, Literal, Namespace, XSD, RDF, RDFS,URIRef,Dataset, BNode
from rdflib.tools import rdf2dot,rdfs2dot, csv2rdf
from rdflib.extras.external_graph_libs import rdflib_to_networkx_multidigraph
from src.csvw_tool import COW
from src.converter.csvw import CSVWConverter, build_schema, extensions
import networkx as nx
import matplotlib.pyplot as plt
import os
from os import path
from os.path import exists
import datetime
import sys
import traceback
from glob import glob
from rdflib import ConjunctiveGraph
from werkzeug.utils import secure_filename
import codecs
from pathlib import Path
import json
from pyld import jsonld
from yaml import load as yaml_load
from graphviz import dot

#script simplificado p/ geracao das amostras
def sample():
	f = open('ms.ttl', mode ='w')
	g = open ('measurements-csv.ttl', mode='r')
	lines = g.readlines()
	count = 0
	for t in lines:
		if count < 6200:
			f.write(t)
			count += 1
	f.close()
	g.close()

def sampleCSV ():
	f = open('/home/biwxx/Documents/IWS/T_final/dados/tabelas/EINSTEIN_Exames_2_SAMPLE.csv', mode ='w')
	g = open('/home/biwxx/Documents/IWS/T_final/dados/tabelas/EINSTEIN_Exames_2.csv', mode='r')

	lines = g.readlines()
	count = 0
	for t in lines:
		if count < 5000:
			f.write(t)
			count += 1
	f.close()
	g.close()

def main():

	#filename = "EINSTEIN_Exames_2_SAMPLE.csv"
	#if not exists("{}-metadata.json".format(files)):
	#	build_json_ld (files)

	#target = "{}-metadata.json".format(files)
	#with open(target, 'r') as json_file:
	#	sample_metadata = json.load(json_file)

	#flattened = jsonld.flatten(dados)
	#normalized = jsonld.normalize(flattened, {'algorithm': 'URDNA2015', 'format': 'application/n-quads'})
	#g = jsonld.to_rdf(dados)
	#COW(mode='build', files=[os.path.join('/home/biwxx/Documents/IWS/T_final/dados/tabelas/', filename)], base="https://repositoriodatasharingfapesp.uspdigital.usp.br/", delimiter='|', quotechar='\"')
	#OW(mode='convert', files=[os.path.join('/home/biwxx/Documents/IWS/T_final/dados/tabelas/', filename)] , delimiter='|', quotechar='\"', processes=4, chunksize=100, base='https://repositoriodatasharingfapesp.uspdigital.usp.br/')

	#for x in sample_metadata["tableSchema"]["columns"]:
	#	print (x["@id"])

	#g.serialize(destination="g.ttl")

	#stream = open('dic.dot', 'w')
	#rdfs2dot.rdfs2dot (g, stream, 'xml')
	#g=Graph().parse(data=json.dumps(sample_metadata),format="json-ld")

	#if not exists ("{}.nq".format(files)):
		#sample = open ("{}.nq".format(files), "w")
		#json.dump(g, sample)
		#sample.close()
		#c = csvw.CSVWConverter(files, delimiter='|', quotechar='\"', encoding=None, processes=4, chunksize=100, output_format='nquads', base="https://repositoriodatasharingfapesp.uspdigital.usp.br/")
		#c.convert()

	g = ConjunctiveGraph()
	g.parse("/home/biwxx/Documents/IWS/T_final/dados/tbox/EINSTEIN_Exames_2_SAMPLE.csv-metadata.json",format="json-ld")
	print (len(g))

	G = rdflib_to_networkx_multidigraph(g,edge_attrs=lambda s, p, o :{})
	#print (g.serialize())
	#g.serialize()



	pos = nx.spring_layout(G, k=0.5, iterations=50)
	edge_labels = nx.get_edge_attributes(G,'title')
	nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
	nx.draw(G, with_labels = True,  font_size=5, alpha=0.6)
	plt.show()

	#consulta(G,1)




if __name__ == '__main__':
    main()
