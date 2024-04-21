class person:


    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def age(self):
        # Assuming date_of_birth is in the format "DD/MM/YYYY. so i will be getting string from 6 to end string"
        birth_year = int(self.date_of_birth[6:])
        current_year = 2024  
        age = current_year - birth_year
        print("Age of ", self.name, " is", age)
    
obj = person("rahim", "Pakistan", "03/08/1996")
#print(obj.age())


class Node:
    left = None
    right = None

    def __init__(self, key):
        self.key = key
        

class Tree:
    
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self.insertRecursive(self.root, val)

    def insertRecursive(self, root, val):
        if(root is None):
            return Node(val)
        
        if(val > root.key):
            root.right = self.insertRecursive(root.right, val)
        elif(val < root.key):
            root.left = self.insertRecursive(root.left, val)

        return root
    def traversing(self):
        self.traverse(self.root)

    def traverse(self, root):
        if root is not None:
            self.traverse(root.left)
            print(root.key)
            self.traverse(root.right)

    def search(self, val):
        return self.insertRecursiveSearch(self.root, val)

    def insertRecursiveSearch(self, parent, val):
        if(parent is None):
            return False
        elif(parent.key == val):
            return True
        
        if(val < parent.key):
            return self.insertRecursiveSearch(parent.left, val)
        elif(val > parent.key):
            return self.insertRecursiveSearch(parent.right, val)

tree = Tree()
tree.insert(2)
tree.insert(4)
tree.insert(9)
tree.insert(1)
tree.insert(20)
tree.traverse(tree.root)
print(tree.search(2))
