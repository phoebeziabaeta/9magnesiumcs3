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
<img width="169" height="324" alt="image" src="https://github.com/user-attachments/assets/6759a226-6d9f-4845-ad30-29a52d045edf" />


## Python Implementation
View [Python Source](classRelationships.py)
## Test Run
<img width="554" height="326" alt="image" src="https://github.com/user-attachments/assets/75202506-ce1d-4ed4-bf84-8d2c1e6c565c" />

## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)
## Analysis
### What is the association between your two classes?
- My first class, Attendance Sheet, is managed by my Record Book class. 
### What multiplicity did you choose and why?
- I chose the one-to-many multiplicity, because it fit with the classes' relationship logically. A record book can contain either zero or many attendance sheets as records.
### How did you implement the relationship in Python?
- 
### Why did you store an object reference instead of copying its data?
### If your relationship uses many, why is a list appropriate?
- So that storing data and adding onto that existing data is easier and more effective.
