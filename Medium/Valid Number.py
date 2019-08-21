class Solution:
    def isNumber(self, s: str) -> bool:
        l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '+', '-', 'e']
        num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        s = s.lstrip().rstrip()
        for i in s:
            if i not in l:
                return False

        if len(s.split('e')) > 2:
            return False
        part1 = s.split('e')[0]
        f = False
        for i in part1:
            if i in num:
                f = True
                break
        if not f:
            return False
        if not part1:
            return False
        if part1 == 'e' or part1 == '.' or part1 == '+' or part1 == '-':
            return False

        point_count = 0
        for index, i in enumerate(part1):
            if i == '+' and index != 0:
                return False
            if i == '-' and index != 0:
                return False
            if i == '.':
                point_count += 1
        if point_count > 1:
            return False

        if len(s.split('e')) == 2:
            part2 = s.split('e')[1]
            if not part2:
                return False
            if part2 == '.' or part2 == '+' or part2 == '-':
                return False
            for index, i in enumerate(part2):
                if i == '+' and index != 0:
                    return False
                if i == '-' and index != 0:
                    return False
                if i == '.':
                    return False

        return True