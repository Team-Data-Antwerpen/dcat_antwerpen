#   Examples usage rdflib
#   
#   Requires: RDFLIB and RDFLIB-JSONLD 
#   https://rdflib.readthedocs.io/en/stable/index.html
#   https://github.com/RDFLib/rdflib-jsonld
#   
#   pip install rdflib
#   pip install rdflib-jsonld

import  os, sys, json, urllib
from rdflib import Graph, URIRef,  Literal
from rdflib.namespace import RDF, FOAF, Namespace, NamespaceManager

## URLS
TDT_URL = "https://datasets7.antwerpen.be"
AGS_PORT = "https://portaal-stadantwerpen.opendata.arcgis.com"
SIC_URL = "https://stadincijfers.antwerpen.be/databank"

## Create new Namespaces
dcat = Namespace("http://www.w3.org/ns/dcat#")
dc = Namespace( "http://purl.org/dc/terms/" )

## load existing dcats-graphs
g1 = Graph().parse(TDT_URL  +"/api/dcat" , format="n3" )
g2 = Graph().parse(AGS_PORT +"/data.json", format="json-ld" )

## merge 2 graph:
g3 = g1 + g2

## create a new graph
nsmanager = NamespaceManager(Graph())
nsmanager.bind('dcat' , dcat)
nsmanager.bind('dc' , dc)
gx = Graph( namespace_manager = nsmanager )

## add new record
###TYPE
s_sic = URIRef( SIC_URL  )
gx.add( (s_sic, RDF.type, dcat.Dataset ) )
###title
gx.add( [s_sic, dc.title, Literal("Stad in cijfers")] )
###description
p_sic = dc.description 
o_sic = Literal('Op de buurtmonitor vindt u demografische, sociale en economische gegevens over de stad Antwerpen.')
gx.add( (s_sic, p_sic, o_sic ) )

## create output dcat
gx_out = gx.serialize(format='n3')
print( gx_out )

## Query dcat: find the description of sic in gx
qry = list( gx.triples( ( URIRef( SIC_URL ), dc.description, None) ) ) 
print( qry )
