class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for char in s:
            if char=="(":
                stack.append(")")
            elif char=="{":
                stack.append("}")
            elif char=="[":
                stack.append("]")        
            else:
                if not stack or char != stack.pop():
                    return False
        return not stack
