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
Link to code:
[Class Implementation](classImplementation.py)
## Test Run
<img width="639" height="194" alt="image" src="https://github.com/user-attachments/assets/f9c62484-284f-462c-b70b-6a2020db9fbf" />


## Object Diagram
<img width="389" height="313" alt="image" src="https://github.com/user-attachments/assets/e1876118-81be-42f8-85dc-371936a3b243" />

## Analysis
### Why did you make your chosen attribute private?
- I made updatePresent() private because the method computes every change in the amount of present, or list_present(), which is not necessary for the user to see.
### Which method changes the state of your object?
- The method that changes the state of object 1 is updatePresent(). It affects the attribute "present", changing its value if a student leaves or arrives in the club venue.
### How did your two objects demonstrate that instances are independent?
- Since each object stored its own variables and were not created dependently to each other, changing the state of object 1, "recorded attendance 1", does not affect object 2, "recorded attendance 2."
### What is the difference between your class diagram and your object diagram?
- The class diagram shows the attributes in the attendance sheet, which contribute to a functioning system or "blueprint." The object diagram shows the two objects that used that blueprint.
