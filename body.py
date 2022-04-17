import json


def get_candidate(path):
    with open(path, "r", encoding="utf-8") as candidates:
        return json.load(candidates)


def write_candidate(candidates_list):
    result = '< pre >'
    for candidate in candidates_list:
        result += (
            f'\tИмя кандидата - {candidate["name"]}\n'
            f'\tПозиция кандидата {candidate["position"]}\n'
            f'\tНавыки через запятую - {candidate["skills"]}\n\n'
        )
    result += '<\npre >'

    return result
