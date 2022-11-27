from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        words_list: list[tuple[str, str]] = []
        numeric_list: list[tuple[str, str]] = []

        for log in logs:
            log_arr: list[str] = log.split(None, maxsplit=2)
            key: str = log_arr[0]
            value: str = " ".join(log_arr[1:])

            # check if string after the identifier string contains numbers
            if log_arr[1].isdigit():
                numeric_list.append((key, value))
            else:
                words_list.append((key, value))

        sorted_words_list = sorted(words_list, key=lambda row: (row[1], row[0]))

        output: list[str] = []

        for k, v in sorted_words_list:
            output.append(f"{k} {v}")

        for k, v in numeric_list:
            output.append(f"{k} {v}")

        return output


solution = Solution()
solution.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]) #?
solution.reorderLogFiles(["1 n u", "r 527", "j 893", "6 14", "6 82"])  # ?

