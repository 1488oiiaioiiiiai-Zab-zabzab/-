from flask import Flask, render_template
from data import db_session
from data.users_py import UserC
from data.jobs_py import JobsC

app = Flask(__name__)
app.config["SECRET_KEY"] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/alch1.db")
    app.run()


@app.route("/")
def tables_with_jobs():
    session = db_session.create_session()
    jobs = session.query(JobsC).all()
    return render_template("tables_jobs.html", jobs=jobs)


if __name__ == "__main__":
    """db_session.global_init("db/alch1.db")
    session = db_session.create_session()
    user = UserC()
    user.surname = "Qwerty"
    user.name = "Amogus"
    user.age = 32
    user.position = "not captain"
    user.speciality = "qqwerty"
    user.address = "module_2"
    user.email = "amogus@mars.org"
    session.add(user)
    session.commit()

    job = JobsC()
    job.team_leader = 2
    job.job = 'qw'
    job.work_size = 20
    job.collaborators = '1, 3'
    job.is_finished = False
    session.add(job)
    session.commit()

    user = UserC()
    user.surname = "y"
    user.name = "Ay"
    user.age = 32
    user.position = "nin"
    user.speciality = "qyy"
    user.address = "module_3"
    user.email = "s@mars.org"
    session.add(user)
    session.commit()

    job = JobsC()
    job.team_leader = 3
    job.job = 'rty'
    job.work_size = 5
    job.collaborators = '1, 2'
    job.is_finished = True
    session.add(job)
    session.commit()

    session.close()"""
    main()
