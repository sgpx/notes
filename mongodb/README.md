# mongodb

## setup

```bash
sudo apt install -y mongodb
sudo echo BIND_IP = 172.31.0.2 > /etc/mongodb.conf
sudo echo PORT = 9999 >> /etc/mongodb.conf
sudo systemctl restart mongodb.service
```

## launch mongod manually

```
mkdir dbx
./mongod --dbpath dbx --bind_ip 10.88.0.2 --port 5000 --auth
```

## mongos

mongo DB sharding utility

# SCRAM auth setup

https://docs.mongodb.com/manual/tutorial/configure-scram-client-authentication/

1. start `mongod` without `--auth`
2. connect with `mongo` or `mongosh`
3. run script

```
use admin;
db.createUser(
  {
    user: "myUserAdmin",
    pwd: "blahblah123",
    roles: [
      { role: "userAdminAnyDatabase", db: "admin" },
      { role: "readWriteAnyDatabase", db: "admin" }
    ]
  }
)
```

4. exit
5. restart `mongod` with `--auth`

# mongo shell SCRAM auth error fix


in mongo shell if db is not specified at the end or DB URI, then it tries to connect to "test" db by default

```
2022-01-07T14:05:01.287+0000 I NETWORK  [conn32] received client metadata from XX.XX.XXX.XXX:PORT conn32: { application: { name: "MongoDB Shell"
 }, driver: { name: "MongoDB Internal Client", version: "3.6.8" }, os: { type: "Linux", name: "Ubuntu", architecture: "x86_64", version: "20.04"
 } }
2022-01-07T14:05:01.297+0000 I ACCESS   [conn32] SCRAM-SHA-1 authentication failed for myadmin on test from client XX.XX.XXX.XXX:PORT ; Use
rNotFound: Could not find user myadmin@test
2022-01-07T14:05:01.300+0000 I ACCESS   [conn32] Unauthorized: not authorized on admin to execute command { endSessions: [ { id: UUID("6edd4050-
0a2e-49e3-9931-a6df35893c82") } ], $db: "admin" }
```

use 

```bash
mongo mongodb://myadmin:mypassword@1.2.3.4:27017/mydatabase
```

# SSL/TLS

```
nohup ./mongod --port 27018 --bind_ip 0.0.0.0 --dbpath dbdata --tlsMode requireTLS --tlsCertificateKeyFile mongo.pem &
```
