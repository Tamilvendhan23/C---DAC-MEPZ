# Set Assignment 1

def get_all_students(batch1: set, batch2: set) -> set:
    if not isinstance(batch1, set) or not isinstance(batch2, set):
        raise TypeError("inputs must be sets")
    return batch1 | batch2


def get_common_students(batch1: set, batch2: set) -> set:
    return batch1 & batch2


def get_exclusive_students(batch1: set, batch2: set) -> set:
    return batch1 - batch2


# Set Assignment 2

def get_unique_skills(skill_list: list) -> set:
    return set(skill_list)


def add_skill(skill_set: set, skill: str) -> None:
    skill_set.add(skill)


def remove_skill(skill_set: set, skill: str) -> None:
    skill_set.discard(skill)
