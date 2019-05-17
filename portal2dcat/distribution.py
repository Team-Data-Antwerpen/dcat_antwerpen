from datetime import datetime
from rdflib import Graph, BNode, URIRef,  Literal
from rdflib.namespace import RDF, FOAF, Namespace, NamespaceManager
from ns import ns, namespaces, dcat, dc
from config import AOD_LIC
from utils import obj2dateLiteral

class distribution:
    def __init__(self, subject=None, graph=None):
        "subject must be URIREF, if graph is given data wil be append to graph"
        self.s = URIRef( subject ) if subject is not None else  BNode() #subject
        
        if graph is None:
            self.gx = Graph( namespace_manager = ns(namespaces).nsManager() )   
        else:
            self.gx = graph
        self.gx.add( (self.s, RDF.type, dcat.Distribution ) ) #subject predicate object
        #add licence document, just in case, doubles are allowed and wont be in output
        self.gx.add( (URIRef(AOD_LIC), RDF.type, dc.LicenseDocument ) ) 
        ####self.gx.add( (URIRef(AOD_LIC), dc.type, Literal("Open data") ) ) 
        
    def dcat_accessURL(self, accessURL):
        self.accessURL = URIRef(accessURL)
        self.gx.add( (self.s, dcat.accessURL, self.accessURL ) )
        
    def dcat_downloadURL(self, downloadURL ): 
        self.downloadURL = URIRef( downloadURL )
        self.gx.add( (self.s, dcat.downloadURL, self.downloadURL ) )
        
    def dcat_mediaType(self, mediaType = "application/json"):
        self.mediaType =  Literal(mediaType)
        self.gx.add( (self.s, dcat.mediaType, self.mediaType ) )
        
    def dc_title(self, title="" ):
        self.title =  Literal(title)
        self.gx.add( (self.s, dc.title, self.title ) )
        
    def dc_description(self, description="" ):
        self.description =  Literal(description)
        self.gx.add( (self.s, dc.description, self.description ) )
        
    def dc_issued(self, issued=None ):
        if issued is None: 
            issued = datetime.now()
        else: 
           issued = obj2dateLiteral( issued )
        self.issued = Literal( issued )
        self.gx.add( (self.s, dc.issued, self.issued ) )
        
    def dc_license(self , license=AOD_LIC ):
        self.license = URIRef( license )
        self.gx.add( (self.s, dc.license, self.license ) )
           
    def asText(self):
        return self.gx.serialize(format='n3')