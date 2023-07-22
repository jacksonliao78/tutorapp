import sqlite3
import datetime

class Db:
    def __init__(self) -> None:
        self.conn = con = sqlite3.connect("tutorapp.db")

    def add_user(self, user):
        sql = ''' INSERT INTO users(username,passwd_hash,created_ts)
              VALUES(?,?,?) '''
        cur=self.conn.cursor()
        cur.execute(sql, [user.username, user.passwd_hash, user.created_ts])
        self.conn.commit()
        return cur.lastrowid
    
    def login_user(self, username, passwd_hash):
        cur=self.conn.cursor()
        res = cur.execute("SELECT * FROM users where username=? and passwd_hash=?", [username, passwd_hash])
        row=res.fetchone()
        try:
            user=User(*row)
            return user
        except Exception as e:
            print(e)
            return None

    def get_users(self):
        cur=self.conn.cursor()
        res = cur.execute("SELECT * FROM users")
        users=res.fetchall()
        for user in users:
            print(user)

    def get_questions(self):
        cur=self.conn.cursor()
        res = cur.execute("select q.id, q.content_html, q.created_ts, q.img_path, u.username, (select count(*) from replies where question_id=q.id) as num_replies from questions q join users u on u.id=q.user_id order by q.created_ts desc limit 100")
        ret=[]
        for row in res:
            q = QuestionSimple(*row)
            q.datestr = str(datetime.datetime.fromtimestamp(q.created_ts))
            ret.append(q)
        return ret

    def get_questions_by_user(self, username):
        cur=self.conn.cursor()
        res = cur.execute("select q.id, q.content_html, q.created_ts, q.img_path, u.username, (select count(*) from replies where question_id=q.id) as num_replies from questions q join users u on u.id=q.user_id where u.username=? order by q.created_ts desc limit 100", [username])
        ret=[]
        for row in res:
            q = QuestionSimple(*row)
            q.datestr = str(datetime.datetime.fromtimestamp(q.created_ts))
            ret.append(q)
        return ret

    def get_replies(self, question_id):
        cur=self.conn.cursor()
        res = cur.execute("select r.*, u.username from replies r join users u on u.id = r.user_id where question_id=? order by created_ts desc", [question_id])
        ret=[]
        for row in res:
            r = ReplySimple(*row)
            r.datestr = str(datetime.datetime.fromtimestamp(r.created_ts))
            ret.append(r)
        return ret
    

    def get_question_by_id(self, id):
        cur=self.conn.cursor()
        res = cur.execute("SELECT q.id, q.content_html, q.created_ts, q.img_path, u.username, (SELECT COUNT(*) FROM replies WHERE question_id=q.id) AS num_replies FROM questions q JOIN users u ON u.id=q.user_id WHERE q.id=?", [id])
        row=res.fetchone()
        try:
            question=QuestionSimple(*row)
            question.datestr = str(datetime.datetime.fromtimestamp(question.created_ts))
            return question
        except Exception as e:
            print(e)
            return None
    
    def add_reply(self, reply):
        sql = ''' INSERT INTO replies(question_id, user_id, content_md, content_html, created_ts)
              VALUES(?,?,?,?,?)'''
        cur=self.conn.cursor()
        cur.execute(sql, [reply.question_id, reply.user_id, reply.content_md, reply.content_html, reply.created_ts])
        self.conn.commit()
        return cur.lastrowid
    
    def add_question(self, question):
        sql = ''' INSERT INTO questions(user_id, content_md, content_html, created_ts, img_path)
              VALUES(?,?,?,?,?)'''
        cur=self.conn.cursor()
        cur.execute(sql, [question.user_id, question.content_md, question.content_html, question.created_ts, question.img_path])
        self.conn.commit()
        return cur.lastrowid

class QuestionSimple:
    def __init__(self, id, content_html, created_ts, img_path, author, num_replies) -> None:
        self.id=id
        self.content_html=content_html
        self.created_ts=created_ts
        self.img_path=img_path
        self.author=author
        self.datestr=''
        self.num_replies=num_replies

class Question:
    def __init__(self, id, user_id, content_md, content_html, subject_id, grade_id, created_ts, img_path) -> None:
        self.id=id
        self.user_id=user_id
        self.content_md=content_md
        self.content_html=content_html
        self.subject_id=subject_id
        self.grade_id=grade_id
        self.created_ts=created_ts
        self.datestr=''
        self.img_path=img_path

class User:
    def __init__(self, id, username, passwd_hash, created_ts) -> None:
        self.id=id
        self.username=username
        self.passwd_hash=passwd_hash
        self.created_ts=created_ts

class Reply:
    def __init__(self, id, question_id, user_id, content_md, content_html, created_ts) -> None:
        self.id=id
        self.question_id=question_id
        self.user_id=user_id
        self.content_md=content_md
        self.content_html=content_html
        self.created_ts=created_ts


class ReplySimple:
    def __init__(self, id, question_id, user_id, content_md, content_html, created_ts, author) -> None:
        self.id=id
        self.question_id=question_id
        self.user_id=user_id
        self.content_md=content_md
        self.content_html=content_html
        self.created_ts=created_ts
        self.author=author
        self.datestr=''