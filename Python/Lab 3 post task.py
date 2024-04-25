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
        if self.root is None:
            self.root = Node(val)
        else:
            self.insertRecursive(self.root, val)

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
        
# creating object
tree = Tree()
# inserting values
tree.insert(10)
tree.insert(20)
tree.insert(5)
tree.insert(15)
tree.insert(30)
tree.insert(25)
tree.insert(23)
tree.insert(27)
tree.insert(24)
tree.insert(26)
tree.insert(28)
tree.insert(29)
tree.insert(31)
# traversing
tree.traversing()

# searching
print(tree.search(20))

