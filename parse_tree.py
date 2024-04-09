import nltk
from nltk.tree import Tree

sentence = "The dog is chasing the cat."

parse_tree_string = "(S(NP(Det The)(N dog))(VP(V is)(NP(V chasing)(Det the)(N cat))))"

# Convert parse tree string into an NLTK Tree object
parse_tree = Tree.fromstring(parse_tree_string)

parse_tree.pretty_print()