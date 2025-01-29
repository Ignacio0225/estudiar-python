from flask import Flask, render_template, request ,redirect, send_file
from extractors.chapter7 import challenge4

app = Flask("JobScrapper")

jobscrapper = challenge4(url = "https://berlinstartupjobs.com/skill-areas/python/")

db = {
}

@app.route("/")
def home():
  return render_template("home.html", name = "nico")

@app.route("/search")
def hello():
  keyword = request.args.get("keyword")
  if keyword == None:
    return redirect("/")
  if keyword in db:
    jobs = db[keyword]
  else: 
    jobs = jobscrapper.skill_page_keyword(keyword)
    db[keyword] = jobs
  return render_template("search.html",keyword = keyword, jobs = jobs)


@app.route("/export")
def export():
  keyword = request.args.get("keyword")
  if keyword == None:
    return redirect("/")
  if keyword not in db:
    return redirect(f"/search?keyword={keyword}")
  jobscrapper.saveForUser(keyword,db[keyword])
  return send_file(f"{keyword}.csv", as_attachment= True)
    

app.run("0.0.0.0")
