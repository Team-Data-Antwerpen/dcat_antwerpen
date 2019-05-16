
import sys, json, urllib2
from rdflib import Graph,  URIRef
from distribution import distribution
from dataset import dataset
from ns import ns, namespaces, dcat, dc 
from config import AGS_PORT, TDT_URL, OUT_PATH 
from utils import cleanGraph

def portalJSON(url):
    "Get the json-object from arcgis portal"
    response = urllib2.urlopen(url)
    return json.load(response)   
    
def parseDistribution(distList, graph, idfield="downloadURL", title=""):
    for dist in distList:
        dist_title = title
        if "title" in dist: 
            dist_title = dist["title"] +" van "+ title
    
        identifier = dist[idfield]
        d = distribution(identifier , graph)
        d.dc_title( dist_title )
        
        if "downloadURL" in dist: 
            d.dcat_downloadURL( dist["downloadURL"] )
            
        if "accessURL" in dist: 
            d.dcat_accessURL( dist["accessURL"] )
        else:
            d.dcat_accessURL( dist[idfield] )
            
        if "description" in dist: 
            d.dc_description( dist["description"] )
        else:
            d.dc_description( dist_title ) 
            
        if "mediaType" in dist:     
            d.dcat_mediaType( dist["mediaType"] ) 
        d.dc_license()

def parseDatasets(agsJSON, graph):
    datasets = agsJSON["dataset"]
    dcat_datasets = []
    for ds in datasets:
        identifier = ds["identifier"]
        dcat_datasets.append(identifier)
        
        d = dataset(identifier, graph)
        #set properties
        d.dc_title( ds["title"] ) 
        d.dc_description( ds["description"] ) 
        d.dc_identifier( ds["identifier"] ) 
        d.dc_issued( ds["issued"] ) 
        d.dc_modified( ds["modified"] ) 
        if "landingPage" in ds: 
            d.dcat_landingPage( ds["landingPage"] ) 
        d.dcat_contactPoint() 
        d.dc_publisher() 
        d.dc_language() 
 
        dist_urls = []
        for dist in ds["distribution"]:
            #remove wms and Arcgis-pages
            if "title" in dist and "OGC" in dist["title"].upper(): 
                continue 
            if "title" in dist and "ARCGIS" in dist["title"].upper(): 
                continue 
            if "downloadURL" in dist: 
                dist_urls.append( dist["downloadURL"] )         
            elif "accessURL" in dist: 
                dist_urls.append( dist["accessURL"] )
        
        d.dcat_distribution( dist_urls )
        parseDistribution([i for i in ds["distribution"]  if ("accessURL" in i and i["accessURL"] in dist_urls )], graph, "accessURL", ds["title"])
        parseDistribution([i for i in ds["distribution"]  if ("downloadURL" in i and i["downloadURL"] in dist_urls )], graph, "downloadURL", ds["title"])
    return dcat_datasets
    
def mergePortalTDT(portal=AGS_PORT, tdt=TDT_URL, outpath=OUT_PATH, outtype="xml"):
    
    #make a graph form arcgis-portal json
    gx = Graph( namespace_manager = ns(namespaces).nsManager() )   
    dcat_datasets = parseDatasets( portalJSON(portal + "/data.jsonld" ), gx)
    
    #merge with the datatank
    g1 = Graph().parse(tdt  +"/api/dcat" , format="n3" )
    ## add the new datasets tot catalog
    for dcat_dataset in dcat_datasets:
        g1.add([URIRef(tdt  +"/api/dcat"), dcat.dataset, URIRef(dcat_dataset) ])
    
    g2 = cleanGraph( g1 ) + gx
    
    with open( outpath, 'w') as fl:
        fl.write( g2.serialize(format=outtype) )