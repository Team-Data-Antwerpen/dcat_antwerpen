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
from portal2dcat.config import AGS_PORT, OUT_PATH

RDF_TYPE = "xml" 
OUTFILE = OUT_PATH   # change to output filename 
FILTER = ''

def main():
    mergePortal(AGS_PORT, OUTFILE, RDF_TYPE, FILTER )

if __name__ == "__main__":
   main()