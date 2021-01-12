from datetime import datetime
from rdflib import Graph, BNode, URIRef,  Literal
from ns import dcat, dc, RDF
from config import CONTACT, HOME_URL, AOD_LIC

def obj2dateLiteral(obj, strict=False):
    dateObj = obj
    if isinstance( obj, (str, unicode) ): 
       try: 
           dateObj = datetime.strptime(obj, "%Y-%m-%dT%H:%M:%S")
       except ValueError: 
           dateObj = datetime.strptime(obj, "%Y-%m-%dT%H:%M:%S.%fZ")
       except ValueError: 
           dateObj = datetime.strptime(obj, "%Y-%m-%dT%H:%M:%S+0000")
       except Exception as e:
            print( "WARNING: Could not convert {} to datetime".format(obj) )
            if strict: raise e
    elif  isinstance( obj, (int, long, float) ): 
        dateObj = datetime.fromtimestamp(obj)
    return Literal( dateObj )
    
    
def findReplaceInGraph( inTriple, rTriple, graph):
    graph.remove( inTriple )
    graph.add( rTriple )
    return graph
    
    
def cleanGraph(graph, fixDates=True, setDefaultContact=True, setDefaultPub=True, fixLicences=True):
    #do not override input graph
    graphOut = graph
    #list all dataset in graph
    ds = [s for s,p,o in graph.triples([None, RDF.type , dcat.Dataset])]
    
    ## clean Dates
    if fixDates:
        datePredicats = [dc.issued, dc.modified]
        gx = []
        for dp in datePredicats: 
            gx += graph.triples([None, dp, None])
        fixedDates = [( [s,p,o], [s, p, obj2dateLiteral(o)]) for s,p,o in gx]
        for fix in fixedDates:
            inTrip, rTrip = fix
            findReplaceInGraph(inTrip, rTrip, graphOut)
        
    #set default contact
    if setDefaultContact:
        for d in ds:         
            #add or update contactPoint, remove old contact
            graphOut.remove([d, dcat.contactPoint, None])
            graphOut.add([d, dcat.contactPoint, URIRef(CONTACT)])
    # set default publisher
    if setDefaultPub:
        for d in ds:
            #add or update publisher, remove old publisher
            graphOut.remove([d, dc.publisher, None])
            graphOut.add([d, dc.publisher, URIRef(HOME_URL)])
    
    #license: TODO
    if fixLicences:  
       licenses = graph.triples( (None, RDF.type, dc.LicenseDocument ) )
       for lic in licenses:
          graphOut.add( [lic[0], dc.type, Literal("Public domain") ] ) 
    
    return graphOut