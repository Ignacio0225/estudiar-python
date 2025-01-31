from flask import Flask, render_template, request ,redirect, send_file
from extractors.chapter7 import berlin, web3, wework

app = Flask("JobScrapper")

jobscrapper = berlin(url = "https://berlinstartupjobs.com/skill-areas/python/")
jobscrapper2 = web3(url = "https://web3.career/python-jobs")
jobscrapper3 = wework(url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term=python")
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
    jobs1 = jobscrapper.skill_page_keyword(keyword)
    jobs2 = jobscrapper2.skill_page_keyword(keyword)
    jobs3 = jobscrapper3.skill_page_keyword(keyword)
    jobs = jobs1 + jobs2 + jobs3
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
