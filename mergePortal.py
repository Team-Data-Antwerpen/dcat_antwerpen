#   Arcgis Portal to DCAt RDF 
#   -------------------------
#   Merge a tdt-dcat service and a arcgis opendata portal-jsonld into one dcat-file. 
#   The output file should be compatible with the DCAT-AP VL specifications
#   See: https://data.vlaanderen.be/doc/applicatieprofiel/DCAT-AP-VL
#   
#   Requires: RDFLIB and RDFLIB-JSONLD 
#   https://rdflib.readthedocs.io/en/stable/index.html
#   https://github.com/RDFLib/rdflib-jsonld
#   
#   pip install rdflib
#   pip install rdflib-jsonld

from portal2dcat import mergePortal
from optparse import OptionParser
from portal2dcat.config import AGS_PORT

OUT_PATH = r"dcat.xml" 

def main():
    parser = OptionParser( 
        usage='Convert a arcgis opendata portal-jsonld into one dcat-file.')

    parser.add_option('-a', '--arcgisportal',  dest="AGS", default= AGS_PORT , 
                         help='A the Arcgis opendata service, default: ' + AGS_PORT )
    parser.add_option('-o', '--output',  dest="OUTFILE", default= OUT_PATH , 
                         help='The output file, default: ' + OUT_PATH )
    parser.add_option('-t', '--type',  dest="RDF_TYPE", default= 'xml' , 
                         help='The output file format like n3, ttl or XML, default: XML' )
    parser.add_option('-f', '--filter',  dest="FILTER", default= '' , 
                         help='Filter by one or more keywords, comma separated list.' )
                         
    opts = parser.parse_args()[0]
  
    # try:  

    mergePortal(opts.AGS, opts.OUTFILE, opts.RDF_TYPE, opts.FILTER )
    # except Exception as e:
    #     parser.print_help()
    #     raise e 
   
if __name__ == "__main__":
   main()