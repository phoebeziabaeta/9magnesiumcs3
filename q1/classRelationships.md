# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)


[Part II - Class Attributes and Methods](classAttributesMethods.md)
## Existing Class
Class: Attendance Sheet


Description: School club sheet for attendance checking
## New Related Class
Class: Record Book


Description: Records of every time the attendance was checked
## Association
Relationship: Manages


Explanation: The record book manages the attendance sheet data
## Multiplicity
Multiplicity: 0..*


Explanation: A record book typically contains many pieces of data, which are typically in the form of records. Since these records often classify as objects, the class can have zero or more depending on how much data has been or is being recorded.
## UML Class Relationship Diagram
<img width="164" height="323" alt="image" src="https://github.com/user-attachments/assets/455a58d3-96bb-4c16-80f4-dfd74b8007ff" />

## Python Implementation
View [Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](images/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)
## Analysis
### What is the association between your two classes?
### What multiplicity did you choose and why?
### How did you implement the relationship in Python?
### Why did you store an object reference instead of copying its data?
### If your relationship uses many, why is a list appropriate?
