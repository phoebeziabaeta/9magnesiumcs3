# Class Attributes and Methods
## Previous Design
Link to my previous activity:
[classObjectUML.md](classObjectUML.md)
## Design Revision
I changed the names for methods members() and present(), changing them to list_members() and list_present() for more efficiency and to be more specific.
## Visibility Decisions
| Attribute | Data Type | Visibility | Why Public/Private? |
|---|---|---|---|
| names | string | Public | Displays every member's name |
| date | integer | Public | Displays date of attendance checking |
| present | integer | Public | Displays every member present |
| excused | boolean | Public | Displays every excused absent member |
| list_members() | string | Public | Displays the list of members |
| list_present() | integer | Public | Displays amount of members present |
| updatePresent() | integer | Private |	Updates present() if the amount of members present changes |

## Updated UML Class Diagram
<img width="247" height="227" alt="image" src="https://github.com/user-attachments/assets/881ba0a3-0045-495a-9fb7-e5703a4a07ab" />


## Python Implementation

[View Python Source](classImplementation.py)
## Test Run
<img width="792" height="339" alt="image" src="https://github.com/user-attachments/assets/56e45899-880f-4725-a355-aa621242606d" />

## Object Diagram
![Object Diagram](images/objectDiagram.png)
## Analysis
### Why did you make your chosen attribute private?
### Which method changes the state of your object?
### How did your two objects demonstrate that instances are independent?
### What is the difference between your class diagram and your object diagram?
