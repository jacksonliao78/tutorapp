# Mission

The mission of this application, is to provide a platform for students to get help, especially students from underserved communities, where they might not have the resources to get in-person tutoring.

I also believe in the collective goodness of the people, and this application would provide a platform for volunteers to help those students in need.

# Technical functionalities

- Students and volunteers can sign up for a free account. Its intentionally chosen not to require an email address as some students might not have them. An account is required mainly to help students organize their list of questions, so they can find their questions easier.
- Any user (student or volunteer) can ask a question, and answers a question.
- To ask or answer a question, user have to first log into the account.
- User can log out of the application once they're done. The default timeout of the Flask session is 31 days. So if not explicitly logged out, user remains logged in for 31 days.
- All the data is saved in a sqlite3 database file. It is chosen because it's self contained as a single file so its easier to work with. And would be a lot cheaper to host on the internet.

# Sqlite3

Sqlite3 should come with MacOS, in the prompt type `sqlite3`, it should put you in the sqlite3 prompt:

```
$ sqlite3
sqlite3> 
```

Similarly, from the tutorapp folder, access the database file by:

```
$ sqlite3 tutorapp.db
```

You can now list all the tables in the db file:

```
sqlite> .tables
questions  replies    users
```

Select rows from a table, etc:

```
sqlite> select * from users;
```