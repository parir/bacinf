from ete2 import NCBITaxa
from ete2 import Tree, TreeStyle, AttrFace

ncbi = NCBITaxa()

input = [l.rstrip("\n") for l in open("db/example_input", "r")]

taxid = ncbi.get_name_translator(input)
tree = ncbi.get_topology(taxid.values())

# print tree.get_ascii(attributes=["sci_name", "rank", "taxid"])

# custom layout: adds "rank" on top of branches, and sci_name as tip names


def my_layout(node):
    if getattr(node, "rank", None):
        rank_face = AttrFace("rank", fsize=7, fgcolor="indianred")
        node.add_face(rank_face, column=0, position="branch-top")
    if node.is_leaf():
        sciname_face = AttrFace("sci_name", fsize=9, fgcolor="steelblue")
        node.add_face(sciname_face, column=0, position="branch-right")

ts = TreeStyle()
ts.layout_fn = my_layout
ts.show_leaf_name = False

tree.render("tree.pdf", tree_style=ts)
