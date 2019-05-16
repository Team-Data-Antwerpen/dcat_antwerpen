from datetime import datetime
from rdflib import Graph, BNode, URIRef,  Literal
from ns import dcat, dc

def obj2dateLiteral(obj, strict=False):
    dateObj = obj
    if isinstance( obj, (str, unicode) ): 
       try: 
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
    graph.add( rTriple )
    graph.remove( inTriple )
    return graph
    
    
def cleanGraph(graph):
    
    ## clean Dates
    datePredicats = [dc.issued, dc.modified]
    gx = []
    graphOut = graph
    for dp in datePredicats: 
        gx += graph.triples([None, dp, None])
    fixedDates = [( [s,p,o], [s, p, obj2dateLiteral(o)]) for s,p,o in gx]
    for fix in fixedDates:
        inTrip, rTrip = fix
        findReplaceInGraph(inTrip, rTrip, graphOut)
    
    return graphOut