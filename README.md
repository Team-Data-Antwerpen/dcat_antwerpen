Arcgis Portal to DCAt RDF 
=========================

Merge a tht-dcat service and a arcgis opendata portal-jsonld into one dcat-file. 
The output file should be compatible with the DCAT-AP VL specifications. 
See: https://data.vlaanderen.be/doc/applicatieprofiel/DCAT-AP-VL

This is mke specificaly for the city of Antwerp and is only tested with their services.
    - The Datatank of Antwerp:  "http://datasets7.antwerpen.be"
    - Arcgis opendata portal of Antwerp: "https://portaal-stadantwerpen.opendata.arcgis.com"
    - > The resulting dcat will be shared to thsi repo: https://raw.githubusercontent.com/warrieka/dcat_antwerpen/master/dcat.xml

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

    mergePortalTDT.py --thedatatank <TDT> --arcgisportal <AGS> --output <OUTFILE> --type <RDF_TYPE>

    Usage: Merge a tht-dcat service and a arcgis opendata portal-jsonld into one dcat-file.

    Options:
      -h, --help            show this help message and exit
      -d TDT, --thedatatank=TDT
                            A the datatank dcat service, default:
                            http://datasets7.antwerpen.be
      -a AGS, --arcgisportal=AGS
                            A the Arcgis opendata service, default: https
                            ://portaal-stadantwerpen.opendata.arcgis.com
      -o OUTFILE, --output=OUTFILE
                            The output file, default: dcat.xml
      -t RDF_TYPE, --type=RDF_TYPE
                            The output file format like n3 or XML, default: XML

    If any option is ommited, the default value will be used. 
    
    
Updating dcat file on github
----------------------------

Run the script again then commit, then push

    mergePortalTDT.py --output dcat.xml
    git add dcat.xml
    git commit -m "updated dcat.xml"
    git push origin master

    
    