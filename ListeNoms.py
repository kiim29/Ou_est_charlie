import os
import pandas as pd

def FaireListe(path):
    data = pd.read_csv(path)

    p = data['filename']
    t=[]
    it=[]
    for i in range(len(p)):
        k = p[i]
        if k in t:
            it[t.index(k)]+=1
        else :
            t.append(p[i])
            it.append(1)
    return t, it

def WriteXML(imgName, imgPath, width, height, coord, path):
    if (path[-1]!="\\" and path[-1]!="/"):
        path = path + "\\"
    name = imgName[:-4]+".xml"
    file = open(path+name, "w")
    file.write("<annotation>\n\t<folder>Waldo</folder>\n\t<filename>"+imgName+"</filename>\n\t<path>"+imgPath+"</path>\n\t<source>\n\t\t<database>Unknown</database>\n\t</source>\n\t<size>\n\t\t<width>"+str(width)+"</width>\n\t\t<height>"+str(height)+"</height>\n\t\t<depth>3</depth>\n\t</size>\n\t<segmented>0</segmented>\n")
    for i in coord:
        file.write("\t<object>\n\t\t<name>waldo</name>\n\t\t<pose>Unspecified</pose>\n\t\t<truncated>0</truncated>\n\t\t<difficult>0</difficult>\n\t\t<bndbox>\n\t\t\t<xmin>"+str(i[0])+"</xmin>\n\t\t\t<ymin>"+str(i[1])+"</ymin>\n\t\t\t<xmax>"+str(i[2])+"</xmax>\n\t\t\t<ymax>"+str(i[3])+"</ymax>\n\t\t</bndbox>\n\t</object>\n")
    file.write("</annotation>\n")
    file.close()