import json


def load_candidates_from_json(path):
    """ Получаем из файла .json список кандидатов """

    with open(path, encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_candidate(candidates, candidate_id):
    """
    Возвращаем кандидата по id
    """
    candidate = next(filter(lambda word: str(word["id"]).lower() == str(candidate_id), candidates))
    return candidate


def get_candidates_by_name(candidates, candidate_name):
    list_candidates = []
    for item in candidates:
        candidate = list(map(lambda word: word.lower(), item["name"].split(" ")))
        if candidate_name.lower() in candidate:
            list_candidates.append(item)

    return list_candidates


def get_candidates_by_skill(candidates, skill_name):
    list_candidates = []
    for item in candidates:
        split_skill = list(map(lambda word: word.lower(), item["skills"].split(", ")))
        if skill_name.lower() in split_skill:
            list_candidates.append(item)

    return list_candidates
