# Collection of Jupyter Notebooks for manipulating geojson annotation

These operations currently involve manipulation of geojson annotation files from segmentation or pancreas sections using HALO. 

Output is initially being tested in QuPath. 

Scripts enable:
1. Expansion of islet annotations without overlapping neighbours.
2. Creation of "doughnut" annotations by removing original islet annotations from expanded islet annotations.
3. Use of multiple tissue annotations to create annotations with holes included. These are otherwise lost when moving from HALO to QuPath holes are separately recoded as filled annotations.

NB. Many of these issues relating to holes appear to be due to a distinction uesed between HALO and QuPath with how they classify annotations. QuPath uses "polygon" geometies which can be programmed to have holes. HALO used "linestring" geometries by default, which cannot have holes.
