# Built-in Types Complexity
- Time complexity of operations
    - Determines efficiency of your program
    - Length is O(1) in all cases

|                |Add                          |Remove               |Contains        |
|----------------|-----------------------------|---------------------|----------------|
|List ``l``      |``insert:O(n), append: O(1)``|``O(n)``             |``O(n)``        |
|Tuple ``t``     |-                            |-                    |``O(n)``        |
|Dictionary ``d``|``O(1) to O(n)``             |``O(1) to O(n)``     |``O(1) to O(n)``|
|Set ``s``       |``O(1) to O(n)``             |``O(1) to O(n)``     |``O(1) to O(n)``|
|Deque ``q``     |``O(1)``                     |``pop: O(1), remove: O(n)`` |``O(n)`` |       |

# Amortized Constant Performance of Method
- Amortized constant O(1)
    - Means that given sufficient number of requests, the average performance time is constant.
    - Occassionally one operation could require O(n) in the worst case.
- Most frequently occurs with hashing whose performance depends on statistical estimates.

# Python is Extensible Using Classes
- Users can define new Python types at will
    - Use object-oriented capability
- Classes represent new types
    - Methods are functions associate with class
    - Attributes are associated data

# Relationships between ADT and DS
- Data Structure
    - Organize data efficiently using existing types
- Abstract Data Types
    - Modeling approach to define new Data Type by its behaviour from user's perspective
    - Analyze properties of its operations such as **space and time complexity**

# Data Type Design Principles
- Space vs. Time tradeoff
    - Often you can improve performance of a method by increasing extra storage
    - Extra O(1) storage is usually good idea
    - Requiring O(n) storage must be convincing
- Recursive data structures
    - It is often easy to write code using **lists** but performance might suffer
    - Tree-like structures are more efficient but resulting code can be more complicated
    - Benefit through **Divide and Conquer** approach
- Separate structure from behaviour
    - Control access to internal representation
    - **Information Hiding** to allow internal changes without breaking other code

# Interaction with Algorithms
- New data types are designed for specific use
    - Most commonly with **algorithms**
    - Algorithm is step-by-step set of operations to solve a problem