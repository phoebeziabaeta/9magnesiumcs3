# Class Attributes and Methods
## Previous Design
Link to my previous activity:
[classObjectUML.md](classObjectUML.md)
## Design Revision
Describe any changes made to your original class.
## Visibility Decisions
| Attribute | Data Type | Visibility | Why Public/Private? |
|---|---|---|---|
| names | string | Public | Displays every member's name |
| date | integer | Public | Displays date of attendance checking |
| present | integer | Public | Displays every member present |
| excused | boolean | Public | Displays every excused absent member |
| members() | string | Public | Displays the list of members |
| present() | integer | Public | Displays amount of members present |
| updatePresent() | Private |	Updates present() if the amount of members present changes |

## Updated UML Class Diagram
<img width="346" height="392" alt="image" src="https://github.com/user-attachments/assets/05d77c02-85c5-4fce-84d3-8ca86379ac8f" />

## Python Implementation

[View Python Source](classImplementation.py)
## Test Run
![Test Run](images/classTestRun.png)
## Object Diagram
![Object Diagram](images/objectDiagram.png)
## Analysis
### Why did you make your chosen attribute private?
### Which method changes the state of your object?
### How did your two objects demonstrate that instances are independent?
### What is the difference between your class diagram and your object diagram?
