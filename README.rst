Introduction
============

Quick Debug functions to print informations on the context.

Each function has 3 optional keyword-only argumuments :
- ``i`` : indent level (defaults to 0)
- ``indent_str`` : indent string for one level (defaults to 2 spaces)
- ``stream`` : file-like object to output (defaults to stderr)

These two last parameter are actually defaulted to the modules variables `dbug._Dindent_str` and `dbug._Dstream`.

Each functions ``F`` exist in 2 flavours :
- ``F`` : normal
- ``nF`` : print a new line before

Functions available
===================

- ``[n]D(*args, **kw)`` : Simply prints ``*args``
- ``[n]Dvar(*expr, **kw)`` : Print for each expression ``expr`` : ``f'{expr} = {eval(expr)}\n'``
- ``[n]DWAI(**kw)`` : Print *W*-here *A*-m *I* with this format : ``module.function(param=val_param, param2=val_param2...) # /path/to/function/definition:line_of_DWAI_call``
- ``[n]DNL(**kw)`` : Print a *N*-ew *L*-ine (``i`` and ``indeit_str`` have no effect on this one

Installation
============

``pip install dbug``


