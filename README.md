This folder contains label expressions for different classes for the GeoComm Indoor Mapping Toolkit in ArcGIS Pro. 
It allows for room number and name visualization relative to the size of the room polygon.
It prioritizes featnum over featname if both don't fit within the polygon area.
If the featname is "ROOM" it will not show up unless there is also no featnum.
It puts the featnum on a line above the featname when both are present.
For polygons with featname "CORRIDOR" it puts featname and featnum on same line.
If there is a "/" in the featname, it is not in the code to fix, but there must be a space after the "/".
The symbol "&" cannot be used in the featname.
ArcGIS Settings:
  Placement - Straight in polygon, try horizontal position first
  Regular Arial font (not bold) 
  Overrun set to 0
