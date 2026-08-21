# ILA 3-1: Applying The Four Pillars of OOP
## Sari-Sari Store Inventory System


### 1. Encapsulation

Encapsulation can be used to group all of the items into one unit, avoiding the issue of having too many variables. It can also help with the clutter that usually comes with large amounts of variables and it makes it easier to read through the code. Encapsulation just helps with storage in general. This concept may involve the product as the object, private price and quantity as the properties, and updateStock() and getPrice() as methods.
### 2. Abstraction

Abstraction makes the checkout process easier at the point of sale. It hides the unnecessary details, e.g. tax calculations, database saving scripts, that are running in the background and shows only what is relevant. This concept may involve the transaction as the object, the total amount as the properties, and pressCheckoutButton() as the method, which comes with other hidden methods such as calculateVAT(), deductFromInventory(), and logDailySales().
### 3. Inheritance

Inheritance prevents the repetition of code for different kinds of retail items. Instead of writing a separate code framework for each and every grocery item, you can create a general blueprint for a product, then extend that for items that need special handling. This concept may involve the product as the parent class, which has common attributes like name, barcode, costPrice, and ExpirableProduct as a child class.
### 4. Polymorphism

Polymorphism lets the system smoothly process a checkout list containing a mix of different item types using a single uniform command, even though different items calculate their final costs differently. This concept may involve calculateFinalPrice() as the method, calculateFinalPrice() for behavior A, which returns the base retail price for a normal sachet of coffee, and calculateFinalPrice(), which overrides the base method to multiply pricePerKilo * totalWeight for a heavy item sold by weight, for behavior B.
## Reflection

Based on what I learned about the four pillars of OOP, encapsulation is the most helpful in the case of the sari-sari store problem. The code would probably work well enough without the other pillars, but without encapsulation, the code would be too cluttered and hard to navigate. Without encapsulation, mistakes are harder to spot and data is harder to store.
