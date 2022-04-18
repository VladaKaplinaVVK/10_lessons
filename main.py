from flask import Flask

from body import get_candidate, write_candidate, choose_id, get_candidate_skills

app = Flask(__name__)


@app.route('/')
def main():
    candidates_list = get_candidate('candidates.json')

    return write_candidate(candidates_list)


@app.route('/candidate/<int:candidate_id>')
def candidate_page(candidate_id):
    candidates_list = get_candidate('candidates.json')

    candidate = choose_id(candidates_list, candidate_id)
    result = f'<img src="{candidate["picture"]}">'

    return result + write_candidate([candidate])


@app.route('/skills/<skill>')
def skills(skill):
    candidates_list = get_candidate('candidates.json')

    return write_candidate(get_candidate_skills(candidates_list, skill))


app.run()
