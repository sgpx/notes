use admin;
admin_username=""
admin_password=""
db.createUser(
  {
    user: admin_username,
    pwd: admin_password,
    roles: [
      { role: "userAdminAnyDatabase", db: "admin" },
      { role: "readWriteAnyDatabase", db: "admin" }
    ]
  }
)
