Bracket representations
=======================

Operations with bracket representations of trees. Supports right and left directions of representations.

Operations
----------

List containing children of node:

**get_children** (node, include_self=False)

List containing ancestors of node:

**get_ancestors** (self, node, include_self=False)

Level of node (distance from root):

**get_level** (self, node)

Usage
-----

::

    >>> left_br = 'root(node1_1,node1_2(node2_1,node2_2,node2_3))'
    >>> br = BracketRepresentation(left_br)
    >>> b.get_children('node1_2')
    ['node2_1', 'node2_2', 'node2_3']
    >>> b.get_ancestors('node1_2')
    ['root']
    >>> b.get_level('node1_2')
    1
    >>>
    >>>
    >>> right_br = '((node2_1,node2_2,node2_3)node1_1,node1_2)root'
    >>> br = BracketRepresentation(right_br, BracketRepresentation.RIGHT)
    >>> b.get_children('node1_2')
    []
    >>> b.get_ancestors('node1_2')
    ['root']
    >>> b.get_level('node1_2')
    1
