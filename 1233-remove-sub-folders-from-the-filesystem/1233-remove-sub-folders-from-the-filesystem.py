class Solution:
    def removeSubfolders(self, paths) -> list[str]:
        # Convert the list of folders to a set for quick lookups
        setArrFolders = set(paths)
        valid_directories = []

        # Iterate over each folder path
        for directory in setArrFolders:
            subfolder_found = False
            current_path = directory

            # Check each parent path of the current folder
            while current_path:
                separator_index = current_path.rfind("/")
                
                if separator_index == -1:
                    break
                
                # Trim the path to get the parent folder
                current_path = current_path[:separator_index]

                # If a parent folder exists, mark it as a subfolder
                if current_path in setArrFolders:
                    subfolder_found = True
                    break

            # If no parent folder was found, add the directory to the result
            if not subfolder_found:
                valid_directories.append(directory)

        return valid_directories


# T = N * L^2
# if each path is length L we will comapre n n-1 n-2 n-3 by reducing the size... that is L^2

# S = N*L for set


class Solution:
    def removeSubfolders(self, paths):
        # Sort the folder paths to bring parent folders before their sub-folders
        paths.sort()

        # Store the first folder as the starting point for comparison
        filtered_paths = []
        filtered_paths.append(paths[0])

        # Iterate over the remaining folders
        for idx in range(1, len(paths)):
            previous_folder = filtered_paths[-1] + "/"

            # Only add the current folder if it's not a subfolder of the last added one
            if paths[idx].startswith(previous_folder) == False:
                filtered_paths.append(paths[idx])

        # Return the filtered list containing only top-level folders
        return filtered_paths

# T = NL*logN ==> there will be logN iterations and in each itr we have to compare N strign and each comp will be L
# S = N for sorting

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class Solution:
    def removeSubfolders(self, paths):
        # Initialize root of our directory tree
        root = TrieNode()
        
        # Construct directory tree
        self.buildDirectoryTree(root, paths)
        
        # Find non-nested directories
        return self._findNonNestedPaths(root, paths)
    
    def buildDirectoryTree(self, base, directories):
        for dir_path in directories:
            current = base
            # Split path and skip empty strings
            components = [d for d in dir_path.split("/") if d]
            
            # Build tree structure
            for component in components:
                if component not in current.children:
                    current.children[component] = TrieNode()
                current = current.children[component]
            
            # Mark end of valid directory path
            current.is_end = True
    
    def _findNonNestedPaths(self, base, directories):
        standalone_dirs = []
        
        for dir_path in directories:
            current = base
            # Split path and skip empty strings
            components = [d for d in dir_path.split("/") if d]
            has_parent = False
            
            # Check each component
            for idx, component in enumerate(components):
                if component in current.children:
                    next_level = current.children[component]
                    
                    # Check if this is a terminal node and it's not the last component
                    if next_level.is_end and idx < len(components) - 1:
                        has_parent = True
                        break
                    current = next_level
                else:
                    break  # Component not in tree, no need to continue

            # Add path if it's not nested under another path
            if not has_parent:
                standalone_dirs.append(dir_path)
        
        return standalone_dirs

# T = S = N*L