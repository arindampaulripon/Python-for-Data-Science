# Fundamental Types
### ``list``
- Aggregate structure stores values
    - Behaviour governed by how you access structure
- Common idiom for **list** objects
    - Start empty
    - Append values, remove values, search for values
    - (Optional: sort)
    - Process all values in order

### ``Stacks``
- Process collection of values in Last-In First-Out
    - Push value onto ``stack``
    - Pop and retrieve the most recently added value
    - Check if empty

### ``Queues``
- Process collection of values in First-In First-Out
    - Append value to tail (right end) of queue
    - Pop value from head (left end) of queue
    - Check if empty
    
# Python: Built-in Data Types

## Sequence types

### ``list``
- Homogenous structures with order

### ``tuple``
- Immutable heterogenous structures

## Associative types

### ``Dictionary``
- Map hashable keys to arbitrary vales
- Associative look-up
- Unordered

### ``Set``
- Unordered collection of **unique** elements

## More in Collections

### ``Deque``
- Efficient append/remove on either end
- Perhaps least well-known of built-in types
- from collections import deque