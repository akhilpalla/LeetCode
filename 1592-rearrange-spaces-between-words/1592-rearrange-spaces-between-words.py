class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()        
        space_count = text.count(' ')
        
        if len(words) > 1:
            between, at_end = divmod(space_count, len(words) - 1)
        else:
            between, at_end = 0, space_count
        
        spaces_between = " " * between
        spaces_at_end = " " * at_end
        
        return spaces_between.join(words) + spaces_at_end