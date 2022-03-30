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
python 3.7+

<https://rdflib.readthedocs.io/en/stable/index.html><br>
<https://nbconvert.readthedocs.io/>

    pip install rdflib
    pip install nbconvert


Usage
------

You can use the [jupyternotebook dcat.ipynb](dcat.ipynb) to make the <dcat.xml> file.

Or you can use script from the cmd-line. 
We also a separate script to upload the output to our s3-cloud storage. 
This script is not in this repo.

    python dcat.py
    python uploadS3.py

    
    
