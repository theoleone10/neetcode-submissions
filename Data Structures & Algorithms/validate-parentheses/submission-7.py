class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for ch in s:
            match ch:
                case '(' | '[' | '{':
                    st.append(ch)
                case ')':
                    if not st or st.pop() != '(':
                        return False
                case ']':
                    if not st or st.pop() != '[':
                        return False
                case '}':
                    if not st or st.pop() != '{':
                        return False

        return not st
