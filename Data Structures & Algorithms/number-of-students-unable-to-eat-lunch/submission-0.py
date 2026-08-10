class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = [students.count(0), students.count(1)]
        # check each sandwich
        for i in sandwiches:
            # if there is any kid that will eat the sanwich, they'll rotate around eventually, so remove them now
            if count[i] > 0:
                count[i] -= 1
            else:
                # otherwise, return how many kids are left
                return sum(count)

        # if you've made it this far, everyone is fed
        return 0
            