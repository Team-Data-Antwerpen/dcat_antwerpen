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

from portal2dcat import mergePortalTDT
from optparse import OptionParser

TDT_URL =  "http://datasets7.antwerpen.be"
AGS_PORT = "https://portaal-stadantwerpen.opendata.arcgis.com"
OUT_PATH = "dcat.xml" 


def main():
    parser = OptionParser(usage='Merge a tht-dcat service and a arcgis opendata portal-jsonld into one dcat-file.')

    parser.add_option( '--thedatatank', dest="TDT", default= TDT_URL , 
                         help='A the datatank dcat service, default: ' + TDT_URL )
    parser.add_option( '--arcgisportal',  dest="AGS", default= AGS_PORT , 
                         help='A the Arcgis opendata service, default: ' + AGS_PORT )
    parser.add_option( '--output',  dest="OUTFILE", default= OUT_PATH , 
                         help='The output file, default: ' + OUT_PATH )

    opts, args  = parser.parse_args()

    try: 
        mergePortalTDT(opts.AGS, opts.TDT, opts.OUTFILE )
    except Exception as e:
        parser.print_help()
        raise e
   
if __name__ == "__main__":
   main()