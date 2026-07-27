class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openings = ["(", "{", "["]
        closings = [")", "}", "]"]
        if len(s) % 2 != 0: return False
        for bracket in s:
            if bracket in openings:
                stack.append(bracket)
            elif bracket in closings:
                if len(stack) == 0:
                    return False
                popped = stack.pop()
                if popped == "(" and bracket != ")":
                    return False
                elif popped == "{" and bracket != "}":
                    return False
                elif popped == "[" and bracket != "]":
                    return False
        if len(stack) == 0:
            return True
        else:
            return False