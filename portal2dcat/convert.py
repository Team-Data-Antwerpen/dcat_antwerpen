import json
from urllib.request import urlopen
from rdflib import Graph,  URIRef
from .distribution import distribution
from .dataset import dataset
from .ns import ns, namespaces, dcat
from .utils import cleanGraph

def portalJSON(url):
    "Get the json-object from arcgis portal"
    response = urlopen(url)
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

def parseDatasets(agsJSON, graph, tagfilter=None):
    datasets = agsJSON["dataset"]
    dcat_datasets = []
    filterList = []
    if tagfilter: 
        if type(tagfilter) == list: filterList = []
        if type(tagfilter) == str: filterList = tagfilter.split(",")

    for ds in datasets:
        identifier = ds["identifier"]

        if len(filterList) > 0:
           if len([ n for n in ds["keyword"] if n in filterList]) == 0: 
                continue

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
        if "keyword" in ds: 
            d.dcat_theme(ds["keyword"])
        
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
    
def mergePortal(portal, outpath, outtype="xml", tagfilter=None ):
    
    # make a graph 
    gx = Graph( namespace_manager = ns(namespaces).nsManager() ) 

    # get data form arcgis-portal json 
    dcat_datasets = parseDatasets( portalJSON(portal + "/data.jsonld" ), gx, tagfilter)

    ## add the new datasets tot catalog
    for dcat_dataset in dcat_datasets:
        uri = URIRef(portal + "/data.jsonld")
        gx.add([uri, dcat.dataset, URIRef(dcat_dataset) ])

    #merge
    g2 = cleanGraph(gx)

    with open( outpath, 'w', encoding="utf-8") as fl:
        fl.write( g2.serialize(format=outtype) )