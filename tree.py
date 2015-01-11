# A leaf in tree structure
# For example: FAST => 3278, CAR =>227, FASTCAR => 3278227
# So the tree is:
#                 3
#                /
#               2
#              /
#             7
#            /
#           8(WORD_END)
#          /
#         2
#        /
#       2
#      /
#     7(LAST)


class Leaf(object):
    children_list = None
    parent = None
    value = None
    end = False

    def __init__(self, value):
        self.children_list = []
        self.value = value

    def append_child(self, leaf):
        if leaf not in self.children_list:
            self.children_list.append(leaf)
            leaf.parent = self
            return leaf
        else:
            for l in self.children_list:
                if l == leaf:
                    return l

    def get_children(self, leaf):
        if isinstance(leaf, Leaf):
            to_find = leaf
        else:
            to_find = Leaf(leaf)
        for child in self.children_list:
            if child == to_find:
                return child

    def has_child(self, leaf):
        if isinstance(leaf, Leaf):
            to_find = leaf
        else:
            to_find = Leaf(leaf)
        return True if to_find in self.children_list else False

    def is_last(self):
        return True if len(self.children_list) == 0 else False

    def is_word_end(self):
        return self.end

    def __eq__(self, other):
        return self.value == other.value
