from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill
app = Flask(__name__)

candidates = load_candidates_from_json("candidates.json")


@app.route('/')
def main_page():
    return render_template('list.html', candidate=candidates)


@app.route('/candidates/<int:x>')
def candidate_page(x):
    candidate = get_candidate(candidates, x)
    return render_template("single.html", candidate=candidate)


@app.route("/search/<candidate_name>")
def candidates_name_page(candidate_name):
    candidate = get_candidates_by_name(candidates, candidate_name)
    return render_template("search.html", candidate=candidate, count=len(candidate))


@app.route("/skill/<skill_name>")
def candidates_skill_page(skill_name):
    candidate = get_candidates_by_skill(candidates, skill_name=skill_name)
    return render_template("skill.html", candidate=candidate, count=len(candidate), skill_name=skill_name.title())


if __name__ == "__main__":
    app.run(debug=True)
