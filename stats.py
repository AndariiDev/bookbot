from typing import Dict, List


def get_num_words(text: str) -> int:
    num_words = text.split()
    return len(num_words)
    # print("{len(num_words)} words found in the document")


def get_num_chars(text: str) -> Dict[str, int]:
    num_chars: Dict[str, int] = {}
    text = text.lower()
    for i in text:
        if i.isalpha():
            if i in num_chars:
                num_chars[i] += 1
            else:
                num_chars[i] = 1
    return num_chars


def sorted_report(num_chars: Dict[str, int]) -> List[Dict[str, int]]:
    char_counts_list = [
        {"char": char, "num": count} for char, count in num_chars.items()
    ]
    sorted_list = sorted(char_counts_list, key=lambda d: d["num"], reverse=True)
    return sorted_list


def sort_on(sorted: tuple[str, int]) -> int:
    return sorted[1]


def char_dict_to_sorted_list(num_chars: tuple[str, int]) -> list[tuple[str, int]]:
    empty_list = []
    for i in num_chars:
        empty_list.append(i)
    sorted_dict = sorted(empty_list, reverse=True, key=sort_on)
    return sorted_dict
