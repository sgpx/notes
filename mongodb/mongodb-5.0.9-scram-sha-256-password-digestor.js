use admin;
db.createUser({
  user: "myAdminUser",
  pwd: "lol",
  roles: [
    { role: "userAdminAnyDatabase", db: "admin" },
    { role: "readWriteAnyDatabase", db: "admin" },
  ],
  passwordDigestor: "server",
});
