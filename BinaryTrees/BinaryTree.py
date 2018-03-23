"""
	Lets focus on binary tree for now.
"""

# This is the private node class
class _NodeClass:
	def __init__(self, data):
		self.left = None;
		self.right = None;
		self.data = data;


class TreeClass:

	# The init will not take any specific input
	def __init__(self):
		self.Tree = None;

	"""
		This function will take in a list of ints and will sort them.
		Then it will create a tree from it.
	"""
	def MakeTreeFromMyIntList(self, input_Data):
		# First thing, we will sort the list from small to large
		sortedList = sorted(input_Data);

		# Here is what we want to do:
		"""
		Take the list and take the middle element:
		- This will be the root.
		All elemenets to the left, will be the left sub tree, and the elemnets should be less than root
		
		"""
	
