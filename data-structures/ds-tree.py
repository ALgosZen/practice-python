class TreeNode:
    def __init__(self, data):
        self.data   = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):


    def print_tree(self):
        print(self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()



def build_product_tree():
        root = TreeNode("Electronics")
        laptop = TreeNode("Laptop")
        laptop.add_child(TreeNode("Mac"))
        laptop.add_child(TreeNode("Thinkpad"))
        laptop.add_child(TreeNode("Surface"))

        cellphone = TreeNode("CellPhone")
        cellphone.add_child(TreeNode("iPhone"))
        cellphone.add_child(TreeNode("Google Pixel"))
        cellphone.add_child(TreeNode("Samsung"))

        root.add_child("laptop")
        root.add_child("CellPhone")
        return root

if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()


