# heroku

## setup (macOS)

`brew install heroku/brew/heroku`

`heroku login`

CLI has automatic project detection through `.git` folder

## dyno

app containers

All Heroku applications run in a collection of lightweight Linux containers called dynos. Container OS is Ubuntu 20.04 as of Dec 2021.

## create an app

`heroku create`

## get list of apps

`heroku apps`

```bash
$ heroku apps                           
=== abc@example.com Apps
my-app-123
```

## get info about particular app

`heroku apps:info my-app-name`

```
=== my-app-123
Addons:         heroku-postgresql:hobby-dev
Auto Cert Mgmt: false
Dynos:          web: 1, run: 1
Git URL:        https://git.heroku.com/my-app-123.git
Owner:          abc@xyz.com
Region:         us
Repo Size:      3 KB
Slug Size:      59 MB
Stack:          heroku-20
Web URL:        https://my-app-123.herokuapp.com/
```

## access git repo

```bash
$ heroku apps:info --shell | grep git_url
```

```bash
# if only one app
$ heroku apps:info  --json | jq '.app.git_url'
"https://git.heroku.com/my-app-123.git"

# specify app
$ heroku apps:info --app=tranquil-harbor-43885 --json | jq '.app.git_url'
```

```bash
git clone https://git.heroku.com/my-app-123.git
```

## get app logs

`heroku logs --tail`

## run a shell or other commands on heroku container

container OS is Ubuntu 20.04 as of Dec 2021

`heroku run bash`

`heroku run env`

## add PostgreSQL addon

`heroku addons:create heroku-postgresql`

## get PostgreSQL database URL

```bash
$ 2>/dev/null heroku run env | grep DATABASE_URL

DATABASE_URL=postgres://username:password@ec2-XX-XXX-XXX-XXX.compute-1.amazonaws.com:5432/mydatabase

$ psql postgres://username:password@ec2-XX-XXX-XXX-XXX.compute-1.amazonaws.com:5432/mydatabase

mydatabase=>
```

## Procfile

Procfile specifies the commands that are executed by the app on startup

https://devcenter.heroku.com/articles/procfile

procfile syntax:

```
<process type>: <command>
```

example:

```
procfoo: ls
```

`web` is a special procfile process name as the process created by the `web` command is the only process that has access to external HTTP

```
web: flask run
web: bundle exec
web: node index.js
```

`web` process must bind to port number specified in app container's $PORT environment variable, or it will be terminated within 30 seconds. example:

```
web: flask run --host 0.0.0.0 --port $PORT
```

```
web: gunicorn app:app --bind 0.0.0.0:$PORT
```

## python/flask example


see folder: `heroku-flask-example/`

0. login with `heroku login`
1. create app with `heroku create`
2. clone app repository with `git clone https://git.heroku.com/my-app-name` and cd to it
3. create `virtualenv` for app with `virtualenv venv --python=python3`
4. install dependencies with `pip3`
5. create `requirements.txt` with `pip3 freeze > requirements.txt`
6. create a `runtime.txt` for heroku to specify the runtime for the app. example `echo python-3.10.0 > runtime.txt`
7. create `app.py` and other files
8. add `venv/` to gitignore with `echo venv/ > .gitignore`
9. add files, create a commit and push changes with `git push`. app will be built and deployed through the connected git webhook automatically.

