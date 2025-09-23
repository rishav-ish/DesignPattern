# CREATIONAL DESIGN PATTERN


## Singleton Pattern

- One instance of a class is created
- Use for DB, cache etc.


## Factory Pattern

## Abstract Factory Pattern

## Builder Pattern

- when you have class with huge constructor.
- Think about using builder pattern.
- Builder Pattern emphasie that there should be a builder that build the object.
- It's like on the builder object you set all parameter and then call build
- You might have seen this use a lot in typeorm sql query build up other places as well.

## Prototype Pattern

- Many times you will want to copy an object rather than creating a brand new one. The reason being is time it takes to create that object or may be cost associated with it.

- Now most of things in object can be private and not exposed outside. So how can we clone the object without knowing its all state ?

- There is were prototype pattern comes. The object itself provide a clone method that provide copy of itself since object have all of its state with it.

- Here we also need to think about shallow cloning and deep cloning<br>
When you create an object with clone method you can set all the current state to newly created object. This is just shallow cloning.
Considering that we also have object inside our object the clone that we did right now will have same reference to the internal object. So we require deep cloning here to make sure state are totally indepedant. So even on underlying object we need to call clone method

