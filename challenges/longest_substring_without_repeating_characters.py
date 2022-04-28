from typing import Set, List

char = str


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        curr_window: List[char] = list()
        uniq_chars: Set[char] = set()
        for idx, c in enumerate(s):
            if c in uniq_chars:
                split_idx = 0
                while split_idx <= (len(curr_window) - 1):
                    c2 = curr_window[split_idx]
                    # 1. remove from uniq_chars
                    uniq_chars.remove(c2)
                    if c2 == c:
                        break
                    # 3. continue moving
                    split_idx += 1
                # 2. split curr_window using this duplicate char
                curr_window = curr_window[split_idx + 1:]
            curr_window.append(c)
            result = max(len(curr_window), result)
            uniq_chars.add(c)
        return result