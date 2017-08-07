English Query
-------------
This is a (very) basic query language with a syntax representing English built as a weekend project for fun.

Examples
---------

### Data storing and querying example:
```
english_query (master) $ python3 repl.py
> Define Foo as an Object
<class 'builtin.ObjectBuiltin'>
> Foo has a name of John
john
> What is Foo's name?
john
> Foo has a color of green
green
> What is Foo's color?
green
> Foo has a location of Switzerland
switzerland
> Where is Foo?
switzerland
```

### Relationship example:
```
english_query (master) $ python3 repl.py
> Define foo as an Object
<class 'builtin.ObjectBuiltin'>
> Define bar as an Object
<class 'builtin.ObjectBuiltin'>
> foo has a unidirectional relationship with bar
<builtin.ObjectBuiltin object at 0x10c6ae940> => <builtin.ObjectBuiltin object at 0x10c6b4a90>
> What is foo's relationship?
<builtin.ObjectBuiltin object at 0x10c6b4a90>
> What is bar's relationship?
None
> Define baz as an Object
<class 'builtin.ObjectBuiltin'>
> baz has a bidirectional relationship with bar
<builtin.ObjectBuiltin object at 0x10c6b4be0> <=> <builtin.ObjectBuiltin object at 0x10c6b4a90>
> What is baz's relationship?
<builtin.ObjectBuiltin object at 0x10c6b4a90>
> What is bar's relationship?
<builtin.ObjectBuiltin object at 0x10c6b4be0>
```
