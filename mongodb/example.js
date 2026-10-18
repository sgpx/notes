use admin;
authorized_username="mdbuser1"
authorized_password="abc123"
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
