class Tree:
    def __init__(self, root = None):
        self.root = root

    def get_element_by_id(self, id):
        # if the current node has an id, return it if it matches the desired id
        if self.root is not None and self.root.id == id:
            return self.root
        # if the current node has children, recursively search each child
        if self.root is not None and self.root.children:
            for child in self.root.children:
                result = child.get_element_by_id(id)
                if result:
                    return result
                
        # return None if the desired id was not found
        return None                    
