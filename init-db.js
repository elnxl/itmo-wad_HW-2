db = db.getSiblingDB("wad_db");
db.wad_tb.drop();

db.wad_tb.insertMany([
    {
        "username": "Admin",
        "password": "Admin",
    },
    {
        "username": "Test",
        "password": "Test",
    },
    ]);