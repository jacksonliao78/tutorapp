import datetime
import random
from db import User, Question, Reply

def generate_users():
    users=[]
    for id in range(1, 50):
        utc_time = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=datetime.timezone.utc)
        ts = utc_time + datetime.timedelta(hours=-id)
        ts = ts.timestamp()

        user=User(id, f'user{id}', f'password{id}', int(ts))
        users.append(user)
    return users

def generate_questions():
    questions=[]
    for id in range(1, 100):
        utc_time = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=datetime.timezone.utc)
        ts = utc_time + datetime.timedelta(hours=-id)
        ts = ts.timestamp()
        q=Question(id, random.randint(1,49), 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent lacinia orci non risus tristique porta. Nunc blandit mi tempus consequat imperdiet. Vestibulum ac leo vestibulum, euismod lacus sed, pretium turpis. Suspendisse sit amet tristique lacus. Aliquam ullamcorper magna eu tempor consectetur. Cras sagittis bibendum nisl vitae commodo. Nullam at tellus ut nibh auctor sollicitudin id vitae lacus. Suspendisse ornare diam sit amet lacus maximus, eu feugiat turpis mattis. Phasellus malesuada urna sed condimentum vestibulum. Suspendisse potenti. Quisque aliquam elit ac mi congue, ac ultricies massa convallis.', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent lacinia orci non risus tristique porta. Nunc blandit mi tempus consequat imperdiet. Vestibulum ac leo vestibulum, euismod lacus sed, pretium turpis. Suspendisse sit amet tristique lacus. Aliquam ullamcorper magna eu tempor consectetur. Cras sagittis bibendum nisl vitae commodo. Nullam at tellus ut nibh auctor sollicitudin id vitae lacus. Suspendisse ornare diam sit amet lacus maximus, eu feugiat turpis mattis. Phasellus malesuada urna sed condimentum vestibulum. Suspendisse potenti. Quisque aliquam elit ac mi congue, ac ultricies massa convallis.', 0, 0, int(ts), '')
        questions.append(q)
    return questions

def generate_replies():
    replies=[]
    for id in range(1, 200):
        utc_time = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=datetime.timezone.utc)
        ts = utc_time + datetime.timedelta(hours=-id)
        ts = ts.timestamp()
        r=Reply(id, random.randint(1,99), random.randint(1,49), 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent lacinia orci non risus tristique porta. Nunc blandit mi tempus consequat imperdiet. Vestibulum ac leo vestibulum, euismod lacus sed, pretium turpis. Suspendisse sit amet tristique lacus.', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent lacinia orci non risus tristique porta. Nunc blandit mi tempus consequat imperdiet. Vestibulum ac leo vestibulum, euismod lacus sed, pretium turpis. Suspendisse sit amet tristique lacus.', int(ts))
        replies.append(r)
    return replies

def generate():
    users=generate_users()
    questions=generate_questions()
    replies=generate_replies()

    with  open('dummydata.sql', 'w') as w:
        for u in users:
            w.write(f"insert into users values ({u.id}, '{u.username}', '{u.passwd_hash}', {u.created_ts});\n")

        for q in questions:
            w.write(f"insert into questions values ({q.id}, {q.user_id}, '{q.content_md}', '{q.content_html}', 0, 0, {q.created_ts}, '');\n")
        
        for r in replies:
            w.write(f"insert into replies values ({r.id}, {r.question_id}, {r.user_id}, '{r.content_md}', '{r.content_html}', {r.created_ts});\n")
        

if __name__ == "__main__":
    generate()