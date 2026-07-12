from rich import inspect

print(inspect(inspect))

"""
def inspect(obj: Any, *, console: Optional[ForwardRef('Console')] = None, title: Optional[str] =  │
│ None, help: bool = False, methods: bool = False, docs: bool = True, private: bool = False,        │
│ dunder: bool = False, sort: bool = True, all: bool = False, value: bool = True) -> None:          │
│                                                                                                   │
│ Inspect any Python object.                                                                        │
│                                                                                                   │
│ * inspect(<OBJECT>) to see summarized info.                                                       │
│ * inspect(<OBJECT>, methods=True) to see methods.                                                 │
│ * inspect(<OBJECT>, help=True) to see full (non-abbreviated) help.                                │
│ * inspect(<OBJECT>, private=True) to see private attributes (single underscore).                  │
│ * inspect(<OBJECT>, dunder=True) to see attributes beginning with double underscore.              │
│ * inspect(<OBJECT>, all=True) to see all attributes.                                              │
│                                                                                                   │
│ Args:                                                                                             │
│     obj (Any): An object to inspect.                                                              │
│     title (str, optional): Title to display over inspect result, or None use type. Defaults to    │
│ None.                                                                                             │
│     help (bool, optional): Show full help text rather than just first paragraph. Defaults to      │
│ False.                                                                                            │
│     methods (bool, optional): Enable inspection of callables. Defaults to False.                  │
│     docs (bool, optional): Also render doc strings. Defaults to True.                             │
│     private (bool, optional): Show private attributes (beginning with underscore). Defaults to    │
│ False.                                                                                            │
│     dunder (bool, optional): Show attributes starting with double underscore. Defaults to False.  │
│     sort (bool, optional):  Sort attributes alphabetically, callables at the top, leading and     │
│ trailing underscores ignored. Defaults to True.                                                   │
│     all (bool, optional): Show all attributes. Defaults to False.                                 │
│     value (bool, optional): Pretty print value. Defaults to True. 

"""

inspect(int)