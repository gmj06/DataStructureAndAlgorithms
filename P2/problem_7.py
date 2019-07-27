# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler
        self.is_leaf = False

    def insert(self, route_part, route_part_handler = None):
        # Insert the node as before
        self.children[route_part] = RouteTrieNode(route_part_handler)



# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler = None, not_found_handler = None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)  
        self.not_found_handler = not_found_handler

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the insert and find functions,
        # so it should be placed in a function here
        path_sliced = path[:-1] if path.endswith("/") else path
        return path_sliced.split("/")

    def insert(self, path, leaf_handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        if path == "" or path == "/":
            self.root.handler = leaf_handler
            return
            
        current_route = self.root

        for sub_path in self.split_path(path):
            if sub_path not in current_route.children:
                current_route.insert(sub_path)
            current_route = current_route.children[sub_path]

        current_route.is_leaf = True
        current_route.handler = leaf_handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_route = self.root

        for sub_path in self.split_path(path):
            if sub_path not in current_route.children:
                return self.not_found_handler
            current_route = current_route.children[sub_path]

        output = current_route.handler if current_route.is_leaf else self.not_found_handler
        return output if output != "" else None


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routes = RouteTrie(handler, not_found_handler)

    def add_handler(self, path, new_handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        # current_route = self.routes.root

        # for sub_path in self.split_path(path):
        #     if sub_path not in current_route.children:
        #         return self.routes.insert(path, new_handler)
        #     current_route = current_route.children[sub_path]

        # current_route.handler = new_handler
        self.routes.insert(path, new_handler)


    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        
        if path == "" or path == "/":
            root_handler = self.routes.root.handler
            return None if root_handler == "" else root_handler

        return self.routes.find(path)

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        path_sliced = path[:-1] if path.endswith("/") else path
        return path_sliced.split("/")


# Here are some test cases and expected outputs you can use to test your implementation
# create the router and add a route
print("--- router ---\n")
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# # some lookups with the expected output
print(router.lookup("")) # should print 'root handler'
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

print("--- router1 ---\n")
router1 = Router("", "not found handler") 
router1.add_handler("/home/contact", "")  # add a route
router1.add_handler("/home/department/resources", "resources handler")  # add a route

print(router1.lookup("")) # should print '' (empty string) or None, as not provided any handler for the root
print(router1.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router1.lookup("/home/contact/")) # should print '' or None if you did not handle trailing slashes
print(router1.lookup("/home/department/resources")) # should print 'resources handler' or None if you did not handle trailing slashes

router1.add_handler("/home", "Home Page")
print(router1.lookup("/home")) # should print 'Home Page' 

router1.add_handler("", "Landing Page")
print(router1.lookup("/")) # should print 'Landing Page' 
