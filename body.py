import json


def get_candidate(path):
    with open(path, "r", encoding="utf-8") as candidates:
        return json.load(candidates)


def write_candidate(candidates_list):
    result = '<pre>'
    for candidate in candidates_list:
        result += (
            f'Имя кандидата - {candidate["name"]}\n'
            f'Позиция кандидата {candidate["position"]}\n'
            f'Навыки через запятую - {candidate["skills"]}\n\n'
        )
    result += '</pre >'

    return result


def choose_id(candidates_list, candidate_id):
    candidate_id = int(candidate_id)
    for candidate in candidates_list:
        if candidate['id'] == candidate_id:
            return candidate


def get_candidate_skills(candidates_list, candidate_skill):
    result = []

    for candidate in candidates_list:
        candidate_skills = candidate['skills'].lower().split(", ")
        if candidate_skill.lower() in candidate_skills:
            result.append(candidate)

    return result
