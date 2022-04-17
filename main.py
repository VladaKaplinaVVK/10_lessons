# import json

from flask import Flask

from body import get_candidate, write_candidate

app = Flask(__name__)


@app.route("/")
def main():
    # candidates_list = get_candidate("candidates.json")
    #
    # return write_candidate(candidates_list)


    with open("candidates.json", "r", encoding="utf-8") as candidates:
        candidates_list = json.load(candidates)

    result = '< pre >'
    for candidate in candidates_list:
        result += (
            f'\tИмя кандидата - {candidate["name"]}\n'
            f'\tПозиция кандидата {candidate["position"]}\n'
            f'\tНавыки через запятую - {candidate["skills"]}\n\n'
        )
    result += '<\npre >'

    return result


@app.route("/candidates/<candidate_id>")
def candidate_page(candidate_id):
    pass
#     with open("candidates.json", "r", encoding="utf-8") as candidates:
#         candidates_list = json.load(candidates)
#
#     for candidate in candidates_list:
#         if candidate["id"] == candidate_id:
#             return candidate_id


@app.route("/skills/<skill>")
def skills(skill):
#     with open("candidates.json", "r", encoding="utf-8") as candidates:
#         candidates_list = json.load(candidates)
    pass

app.run()
