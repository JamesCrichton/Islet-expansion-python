# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 12:07:49 2024

@author: jcc234
"""

#Program to read GeoJson annotations files from Halo
#Expand islet annotations and exclusion of islets overlapping tissue boundaries

import geojson
import numpy as np
import skimage as ski
import matplotlib.pyplot as plt
from skimage.color import label2rgb


# Load the GeoJSON file
with open('C:/Users/jcc234/OneDrive - University of Exeter/Documents/Projects/Bec/Islet expansion python/2024_5_13_RDT1.30_6232_MSC Panel _x40_Scan1.unmixed.qptiff - resolution #1.geojson') as f:
    data = geojson.load(f)


#This is a dict of dicts

# Print the data to see its structure
print(data)
print(data.keys())
print(data.values())
print(data.items())
len(data.items())


#list the name of each object
obj_names = [obj["properties"]["classification"]["name"]for obj in data["features"]]
unique_names_set=set(obj_names)

#Calculate the array limits for plotting everything necessary
obj_coords_list = [obj["geometry"]["coordinates"] for obj in data["features"]]

max_x_per_obj=[]
max_y_per_obj=[]

total_anotation_count=len(data["features"])

for obj in data["features"]:
    coords=obj["geometry"]["coordinates"] 
    max_x_per_obj.append(max([xy[0] for xy in coords]))
    max_y_per_obj.append(max([xy[1] for xy in coords]))

x_lim=max(max_x_per_obj)+20
y_lim=max(max_y_per_obj)+20


#Loop through islet annotations and plot to a single array. Number labels by position in annotations file

position=1#initialise counter through annotations
islet_array=np.zeros((x_lim,y_lim), dtype=int)

for obj in data["features"]:
    name=obj["properties"]["classification"]["name"]
   

    if (name != "Acinar+Islets_inside mapped tissue"):
                     
        #plot the annotations to np arrays
        polygon=np.array(obj["geometry"]["coordinates"])
        mask=ski.draw.polygon2mask((x_lim, y_lim), polygon)
        islet_array[mask]=position # assign px in the mask the value of the annotation position in the geojson file to make a label image        

    print("Annotation ",position," of", total_anotation_count, " processed")

    position+=1 #add 1 to the annotation position number

plt.imshow(islet_array)
plt.show()



## Expand the islets
islet_array_expanded=ski.segmentation.expand_labels(islet_array, distance=100)

plt.imshow(islet_array_expanded)
plt.show()


##Checking tissue annotations. V slow to process to masks
test_array=np.zeros((x_lim,y_lim), dtype=int)
counter=0

for obj in data["features"]:
    name=obj["properties"]["classification"]["name"]
   
    if (name == "Acinar+Islets_inside mapped tissue"):
        print("processing annotation ", counter)             
        print(len(obj["geometry"]["coordinates"]), " coords")
        polygon=np.array(obj["geometry"]["coordinates"])
        mask=ski.draw.polygon2mask((x_lim, y_lim), polygon)
        test_array[mask]=1
        print("done")
    
    
    counter+=1


#polygon=np.array(data["features"][337]["geometry"]["coordinates"])
polygon=np.array(data["features"][50]["geometry"]["coordinates"])
mask=ski.draw.polygon2mask((x_lim, y_lim), polygon)
test_array


data["features"][337]

data["type"]
data["features"]