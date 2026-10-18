use mydb;
authorized_username=""
authorized_password=""
db.createUser(
  {
    user: authorized_username,
    pwd: authorized_password,
    roles: [
      { role: "userAdminAnyDatabase", db: "admin" },
      { role: "readWriteAnyDatabase", db: "admin" }
    ],
    passwordDigestor: "server"
  }
)
