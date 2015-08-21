import xml.etree.ElementTree as ET

tree = ET.parse('xml.tml')  # copy the xml into the folder
foundation = ET.parse('FND.xml')
root = tree.getroot()
foundaroot = foundation.getroot()

info ={}
info_tag = ["cciBuNum","cciSiteName","cciWorkOrderNum","applicationNum","revisionNum"]

for child in root:
    if child.tag == "towerMetadata":
        for grandchild in child:
            if grandchild.tag == "cciInfo":
                for grandgrandchild in grandchild:
                    if grandgrandchild.tag in info_tag:
                        info[grandgrandchild.tag]=grandgrandchild.text
    if child.tag == "discreteLoadData":
        data = []
        for elem in child:
            key = elem.findtext("USName")
            data.append((key, elem))
        data.sort()
        child[:]=[item[-1] for item in data]

for child in foundaroot:
    if child.tag == "General":
        for grandchild in child:
            if grandchild.tag=="BUNum":
                grandchild.text=info["cciBuNum"]
            if grandchild.tag=="SiteName":
                grandchild.text=info["cciSiteName"]
            if grandchild.tag=="AppNumber":
                grandchild.text=info["applicationNum"]+" rev."+info["revisionNum"]
            if grandchild.tag=="WO":
                grandchild.text=info["cciWorkOrderNum"]

#sort the discrete load by 

                
foundation.write("NEW FOUND.xml")
tree.write("xml new.xml")
