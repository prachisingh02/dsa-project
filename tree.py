# Tree Example - Folder Structure

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

# Root folder
root = TreeNode("C:")

documents = TreeNode("Documents")
pictures = TreeNode("Pictures")

root.add_child(documents)
root.add_child(pictures)

documents.add_child(TreeNode("Notes"))
documents.add_child(TreeNode("Projects"))

pictures.add_child(TreeNode("Photos"))
pictures.add_child(TreeNode("Screenshots"))

# Display Tree
print(root.data)

for child in root.children:
    print("|--", child.data)

    for subchild in child.children:
        print("    |--", subchild.data)