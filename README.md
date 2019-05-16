Arcgis Portal to DCAt RDF 
=========================

Merge a tht-dcat service and a arcgis opendata portal-jsonld into one dcat-file. 
The output file should be compatible with the DCAT-AP VL specifications. 
See: https://data.vlaanderen.be/doc/applicatieprofiel/DCAT-AP-VL

This is mke specificaly for the city of Antwerp and is only tested with their services.
    - The Datatank of Antwerp:  "http://datasets7.antwerpen.be"
    - Arcgis opendata portal of Antwerp: "https://portaal-stadantwerpen.opendata.arcgis.com"

Dependencies 
------------
python 2.7+

https://rdflib.readthedocs.io/en/stable/index.html
https://github.com/RDFLib/rdflib-jsonld

    pip install rdflib
    pip install rdflib-jsonld

Usage
-----

    mergePortalTDT.py --thedatatank <TDT> --arcgisportal <AGS> --output <OUTFILE> 

    Usage: Merge a tht-dcat service and a arcgis opendata portal-jsonld into one dcat-file.

    Options:
      --thedatatank TDT   A the datatank dcat service, default:
                          http://datasets7.antwerpen.be
      --arcgisportal AGS  A the Arcgis opendata service, default: https://portaal-
                          stadantwerpen.opendata.arcgis.com
      --output OUTFILE    The output file, default:
                          I:\2_05_03_Projecten\Open_Data\dcat\portal2dcat.xml

    If any option is ommited, the default value will be used. 