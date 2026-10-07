class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        left_remove = 0
        right_remove = 0

        # Find minimum number of '(' and ')' to remove
        for ch in s:

            if ch == '(':
                left_remove += 1

            elif ch == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        ans = set()

        def is_valid(string):
            balance = 0

            for ch in string:
                if ch == '(':
                    balance += 1

                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        def dfs(index, left_remove, right_remove, path):

            # Finished processing string
            if index == len(s):

                if left_remove == 0 and right_remove == 0:
                    result = ''.join(path)

                    if is_valid(result):
                        ans.add(result)

                return

            ch = s[index]

            # OPTION 1: Remove current bracket
            if ch == '(' and left_remove > 0:
                dfs(
                    index + 1,
                    left_remove - 1,
                    right_remove,
                    path
                )

            elif ch == ')' and right_remove > 0:
                dfs(
                    index + 1,
                    left_remove,
                    right_remove - 1,
                    path
                )

            # OPTION 2: Keep current character
            path.append(ch)

            dfs(
                index + 1,
                left_remove,
                right_remove,
                path
            )

            path.pop()

        dfs(0, left_remove, right_remove, [])

        return list(ans)
