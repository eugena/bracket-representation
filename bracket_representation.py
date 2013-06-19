# -*- coding: utf-8 -*-

"""
Operations with bracket representations
of trees
"""
import re


class BracketRepresentation(object):
    """
    BracketRepresentation object
    """
    # Direction of representation constants
    LEFT = 'left'
    RIGHT = 'right'

    def __init__(self, br, direction=LEFT):
        """
        Initialization
        :param br: string
        :param direction: string
        :return: None
        """
        if direction in (self.LEFT, self.RIGHT):
            self.direction = direction
        else:
            raise ValueError('Invalid direction')
        if self.validate(br):
            self.br = br.replace(' (', '(').replace(') ', ')')
        else:
            raise ValueError('Invalid representation')

    def validate(self, br):
        """
        Validates representation
        :param br: string
        :return: bool
        """
        valid = True
        if br.count('(') != br.count(')'):
            valid = False
        return valid

    def get_children(self, node, include_self=False):
        """
        Returns a list containing children of tree
        :param node: string
        :return: list
        """
        if self.LEFT == self.direction:
            exp = r'%s\(([^)]+)\)'
        else:
            exp = r'\(([^(]+)\)%s'
        children = re.search(exp % node, self.br)
        prepared = []
        if children:
            prepared = re.sub(
                r'[\(\)]',
                ',',
                children.group(1)).split(',')
        if include_self:
            prepared = [node, ] + prepared
        return prepared

    def get_ancestors(self, node, include_self=False):
        """
        Returns a list containing ancestors of tree
        :param node: string
        :return: list
        """
        prepared = []
        try:
            if self.LEFT == self.direction:
                br = self.br[:self.br.index(node)]
                exp = r'([^(\,]+)\('
            else:
                br = self.br[self.br.index(node) + len(node):]
                exp = r'\)([^)\,]+)'
            prepared = re.findall(exp, br)
            if self.RIGHT == self.direction:
                prepared.reverse()
            if include_self:
                prepared += [node, ]
        except ValueError:
            pass
        return prepared

    def get_level(self, node):
        """
        Returns the level of node (distance from root)
        :param node: string
        :return: integer
        """
        level = 0
        try:
            if self.LEFT == self.direction:
                level = self.br[:self.br.index(node)].count('(')
            else:
                level = self.br[self.br.index(node):].count(')')
        except ValueError:
            pass
        return level
