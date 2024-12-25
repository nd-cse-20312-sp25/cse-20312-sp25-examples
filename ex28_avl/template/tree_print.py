# Derived from: https://github.com/joowani/binarytree/blob/master/binarytree/__init__.py
# The following license applies to the TreePrint.py file only.
# MIT License

# Copyright (c) 2016 Joohwan Oh

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
def _pretty_tree_helper(root, curr_index=0):
    if root is None:
        return [], 0, 0, 0

    line1 = []
    line2 = []
    node_repr = str(root.key)

    new_root_width = gap_size = len(node_repr)
    
    # Get the left and right sub-boxes, their widths, and root repr positions
    l_box, l_box_width, l_root_start, l_root_end = _pretty_tree_helper(root.left, 2 * curr_index + 1)
    r_box, r_box_width, r_root_start, r_root_end = _pretty_tree_helper(root.right, 2 * curr_index + 2)

    # Draw the branch connecting the current root to the left sub-box
    # Pad with whitespaces where necessary
    if l_box_width > 0:
        l_root = (l_root_start + l_root_end) // 2 + 1
        line1.append(' ' * (l_root + 1))
        line1.append('_' * (l_box_width - l_root))
        line2.append(' ' * l_root + '/')
        line2.append(' ' * (l_box_width - l_root))
        new_root_start = l_box_width + 1
        gap_size += 1
    else:
        new_root_start = 0

    # Draw the representation of the current root
    line1.append(node_repr)
    line2.append(' ' * new_root_width)

    # Draw the branch connecting the current root to the right sub-box
    # Pad with whitespaces where necessary
    if r_box_width > 0:
        r_root = (r_root_start + r_root_end) // 2
        line1.append('_' * r_root)
        line1.append(' ' * (r_box_width - r_root + 1))
        line2.append(' ' * r_root + '\\')
        line2.append(' ' * (r_box_width - r_root))
        gap_size += 1
    new_root_end = new_root_start + new_root_width - 1

    # Combine the left and right sub-boxes with the branches drawn above
    gap = ' ' * gap_size
    new_box = [''.join(line1), ''.join(line2)]
    for i in range(max(len(l_box), len(r_box))):
        l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
        r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
        new_box.append(l_line + gap + r_line)

    # Return the new box, its width and its root positions
    return new_box, len(new_box[0]), new_root_start, new_root_end
    
def pretty_tree(tree):
    lines = _pretty_tree_helper(tree.root, 0)[0]
    return '\n' + '\n'.join((line.rstrip() for line in lines))
