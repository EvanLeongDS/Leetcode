class Solution:
    def simplifyPath(self, path: str) -> str:
        # overall strategy, split then concatenate back together with strings 
        stack = []
        components = path.split('/')
        print(components)
        
        for component in components: 
            if component == "" or component == ".":
                # we are on the same directory and are getting rid of extra slashes, therefore we dont have to change anything about our final string 
                continue
            elif stack and component == "..":
                # get rid of the thing before it and pop it off the stack
                stack.pop()
            elif component == "..":
                continue
            else:
                stack.append(component)
        string = ""
        for word in stack:
            string += "/" + word
        if len(string) == 0:
            return "/"
        else:
            return string

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna