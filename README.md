This repository contains label expressions using label classes for the GeoComm Indoor Mapping Toolkit in ArcGIS Pro. 
It allows for room number and name visualization relative to the size of the room polygon.
It prioritizes featnum over featname if both don't fit within the polygon area.
If the featname contains "ROOM" or "CLASSROOM", that part of the featname will not show up, unless it is the only part of the featname and there is also no featnum.
It puts the featnum on a line above the featname when both are present.
For polygons with featname "CORRIDOR" it puts featname and featnum on same line.
If the room type is "transition" or "bathroom", only the featname will show up if present, otherwise there is no label as they are symbolized by points.
The symbol "&" and "/" cannot be used in the featname per industry standards. 
ArcGIS Settings:
  Placement - Straight in polygon, try horizontal position first
  Regular Arial font (not bold) 
  Overrun set to 0
