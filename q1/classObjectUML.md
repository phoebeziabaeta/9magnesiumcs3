# SG4 - Understanding Classes and Objects
## Attendance Sheet
## School club sheet for attendance checking
## Properties
| Property | Data Type | Description |
|---|---|---|
| names | string | Names of the club members |
| date | integer | The date of when the attendance was checked |
| present | integer | Amount of members present |
| excused | boolean | Shows if the member/s' absence is excused |
## Methods
| Method | Description |
|---|---|
| members() | Displays the list of members |
| present() | Displays amount of members present |
| updatePresent(present: int) | Updates present() if the amount of members present changes |
## Class Diagram
<img width="246" height="226" alt="image" src="https://github.com/user-attachments/assets/514aa322-3118-41bc-9e0f-a16c22277a52" />


## Design Explanation
### Why did you choose this class? 
**Answer:** I chose this class because it is something I am already familiar with, which made deciding the properties and methods easier and quicker.
### Which property is the most important? Why?
**Answer:** The names property, because you could check the attendance with that property alone by doing a roll call, the others are there to make things easier and organized.
### Which method is the most useful? Why?
**Answer:** updatePresent(present: int), because it helps with keeping track of the members present.
