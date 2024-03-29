from rdflib.namespace import FOAF, Namespace, NamespaceManager
from rdflib import Graph

## namespaces 
dcat = Namespace("http://www.w3.org/ns/dcat#")
dc = Namespace( "http://purl.org/dc/terms/" )
namespaces={'dcat': dcat, 'dc': dc, 'foaf': FOAF}


class ns:
    """create Namespaces"""
    def __init__(self, namespaces=namespaces):
        self.namespaces = namespaces 
    
    def nsManager(self):
        nsmanager = NamespaceManager(Graph())
        for n in self.namespaces:
            nsmanager.bind(n, self.namespaces[n])
        return nsmanager