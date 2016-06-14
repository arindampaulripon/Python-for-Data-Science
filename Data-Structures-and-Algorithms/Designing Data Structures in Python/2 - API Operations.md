# Built-in Data Types API
|                |Size       |Add                    |Remove               |Contains      |
|----------------|-----------|-----------------------|---------------------|--------------|
|List ``l``      |``len(l)`` |``insert``, ``append`` |``del, pop, remove`` |``in, index`` |
|Tuple ``t``     |``len(t)`` |                       |                     |``in``        |
|Dictionary ``d``|``len(t)`` |``d[k]=v``           |``del, pop``         |``in``        |
|Set ``s``       |``len(s)`` |``add``                |``remove``           |``in``        |
|Deque ``q``     |``len(q)`` |``append``             |``del, pop``         |``in``        |

# API Considerations for Data Structures
- An aggregate may provide ``Set Semantics``
    - Uniqueness of values within set
    - Should return meaningful response to differentiate these two requests