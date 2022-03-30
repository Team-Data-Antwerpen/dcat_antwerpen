#!/usr/bin/env python
# coding: utf-8

# In[46]:


## pip install rdflib
from rdflib import Graph, URIRef, Namespace, Literal, BNode
from rdflib.namespace import RDF, FOAF
AGS_PORT = "https://portaal-stadantwerpen.opendata.arcgis.com/data.jsonld"
AOD_LIC = "https://www.antwerpen.be/info/5c9c967180779f42723823c9/gratis-open-data-licentie"
CONTACT = "gis@antwerpen.be"
HOME_URL = "https://antwerpen.be"


# In[47]:


def dcat_theme(keywords=[]):
    "Find theme using keywords"
    for key in keywords:
        if key.lower() == "economie":
            return Literal('Economie') #URIRef("http://vocab.belgif.be/auth/datatheme/ECON")
        elif key.lower() in ["cultuur", "sport" ]:
            return Literal('Cultuur') #URIRef("http://vocab.belgif.be/auth/datatheme/CULT")
        elif key.lower() == "onderwijs":
            return Literal('Onderwijs') #URIRef("http://vocab.belgif.be/auth/datatheme/EDUC")
        elif key.lower() in ["afval", "bodem", "milieu", "groeninventaris"]:
            return Literal('Milieu') #URIRef("http://vocab.belgif.be/auth/datatheme/ENVI")
        elif key.lower() in ["publieke diensten"]:
            return Literal('Overheid') #URIRef("http://vocab.belgif.be/auth/datatheme/GOVE")
        elif key.lower() == "zorg":
            return Literal('Gezondheidszorg') #URIRef("http://vocab.belgif.be/auth/datatheme/HEAL")
        elif key.lower() in ["grenzen", "structuurplan"]:
            return Literal('Grenzen') #URIRef("http://vocab.belgif.be/auth/datatheme/REGI")
        elif key.lower() == "mobiliteit":
            return Literal('Transport en Mobiliteit') #URIRef("http://vocab.belgif.be/auth/datatheme/TRAN")   
    return Literal('geospatial')


# In[48]:


## read graph and namespaces
g = Graph()
g.parse(AGS_PORT, format='json-ld')
dc = Namespace( "http://purl.org/dc/terms/" )
dcat = Namespace("http://www.w3.org/ns/dcat#")
g.namespace_manager.bind("foaf", FOAF)
g.namespace_manager.bind("dcat", URIRef("http://www.w3.org/ns/dcat#"))
g.namespace_manager.bind("dc", URIRef("http://purl.org/dc/terms/") )


# In[49]:


## add license
g.add( [URIRef(AOD_LIC), RDF.type, dc.LicenseDocument ] ) 
g.add( [URIRef(AOD_LIC), dc.type, Literal("Public domain") ] ) 
g.add( (URIRef(HOME_URL), RDF.type, FOAF.Agent ) )
g.add( (URIRef(HOME_URL), FOAF.name, Literal('Stad Antwerpen') ) )


# In[50]:


## add extra properties of the catalog
for s, p, o in g.triples(( None,  RDF.type, dcat.Catalog )):
    g.add( (s, dc.title, Literal("Opendata portaal Antwerpen")  ) )
    g.add( (s, dc.description, Literal("""
De stad Antwerpen beschikt over een schat aan geografische data over de stad. 
Via dit portaal wordt u de mogelijkheid geboden om deze geografische data te verkennen, 
visualiseren en te downloaden. Deze data is open data en mag u vrij en kosteloos gebruiken. 
Met de datasets kunt u bijvoorbeeld nieuwe mobiele toepassingen ontwikkelen die de dienstverlening voor bewoners kunnen verbeteren. 
Ontdek de data door hieronder te zoeken op de verschillende thema’s of door een trefwoord in te vullen.""") ) )
    g.add( (s , dc.publisher , Literal("Stad Antwerpen")  ) )
    g.add( (s , dc.license , URIRef(AOD_LIC)  ) )
    g.add( (s , dc.language , URIRef("http://id.loc.gov/vocabulary/iso639-1/nl")  ) )
    


# In[51]:


## add extra properties of the Datasets
for s, p, o in g.triples(( None, RDF.type, dcat.Dataset)):
    keyw = []
    g.add( (s , dc.language , URIRef("http://id.loc.gov/vocabulary/iso639-1/nl") ) )
    for s, p, o in g.triples(( s,  dc.license, None)):
        g.remove((s, p, o))
        g.add( (s , dc.license , URIRef(AOD_LIC)  ) )
    for s, p, o in g.triples(( s,  dcat.keyword, None)):
        keyw.append(str(o))
    for s, p, o in g.triples(( s,  dcat.theme, None)):
         g.remove((s, p, o))
         g.add((s, p, dcat_theme(keyw) ))


# In[52]:


## write xml
n3 = g.serialize(format='application/rdf+xml', indent=4)
with open("dcat.xml", 'w', encoding='utf-8' ) as f:
    f.write(n3)

