Arcgis Portal to DCAT RDF 
=========================

Convert a arcgis opendata portal-jsonld into one dcat-file. 
The output file should be compatible with the DCAT-AP VL specifications. 
See: https://data.vlaanderen.be/doc/applicatieprofiel/DCAT-AP-VL

This tool is made specificaly for the city of Antwerp and is only tested with their services.

- Arcgis opendata portal of Antwerp: "https://portaal-stadantwerpen.opendata.arcgis.com"
- -> The resulting dcat will be shared to thsi repo: [dcat.xml](dcat.xml)

End goal is usage on https://opendata.vlaanderen.be/ .
    
Dependencies 
------------
python 2.7+

https://rdflib.readthedocs.io/en/stable/index.html
https://github.com/RDFLib/rdflib-jsonld

    pip install rdflib
    pip install rdflib-jsonld

Usage
-----

First modify [config.py](portal2dcat/config.py) to your portal, licenc etc. 

    ## URLs
    AGS_PORT = <YOUR ARCGIS PORTAL: https://<something>.opendata.arcgis.com>
    AOD_LIC  = <LINK TO YOUR LICENCE>
    CONTACT  = <YOUR CONTACT-EMAIL>
    HOME_URL = <YOUR UNIQUE HOMEPAGE>
    
    ## defaults
    OUT_PATH = "dcat.xml"

run mergePortal.py to create the dcat.xml.
    
Updating dcat file on github
----------------------------

Run the script again then commit, then push

    mergePortal.py 
    git add dcat.xml
    git commit -m "updated dcat.xml"
    git push origin master

    
    
