from trie import Trie


class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list) or not all(
                isinstance(s, str) for s in strings
        ):
            raise TypeError("Input must be a list of strings.")

        if not strings:
            return ""

        # Ініціалізація Trie
        for string in strings:
            self.put(string)

        # Find the longest common prefix
        current = self.root
        longest_prefix = []

        for _ in range(
                len(strings[0])
        ):  # Maximum length of the longest common prefix
            if len(current.children) != 1 or current.value is not None:
                break
            char, next_node = next(iter(current.children.items()))
            longest_prefix.append(char)
            current = next_node

        return "".join(longest_prefix)


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    print("All tests passed!")
