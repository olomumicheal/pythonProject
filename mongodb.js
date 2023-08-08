#Data Types, mongodb uses a languange called BSON
JSON = {
    string: "String of text",
    int: 405,
    float: 3.5,
    boolean: false,
    array: ["this", 607, true],
    object: {attr1: "attr1", attr2: "attr2"},
    date: new Date("<YYY-mm-dd").
    object_id: <ObjectId>,
    no_value: null
}

insertOne({})

//Single database of a student
db.students.insertOne({name: "Jack", major: "Biology", gpa: 3.5})

//Adding another student to the database
db.students.insertOne({_id: 2, name: "Claire", major: "Marketing", gpa: 3.7,
awards:["Valecdictorian", "Summa cum Laude"]})

//Adding another student to the database
db.students.insertOne({name: "Evan", major: "Astronomy", gpa: 3.7})

//Adding another student to the database
db.students.insertOne({name: "Kate", major: "Sociology", gpa: 3.2,
contact: {phone: "333-333", email: "student@gmail.com"}})

//Adding another student to the database
db.students.insertOne({name: "Phil", major: "Chemistry", gpa: 2.5, startdate: new Date("2012-08-23")})

//Adding multiple students data using insertMany()
db.students.insertMany([{name: "Mike", major: "Computer Science", gpa: 2.7},
{name: "Andrea", major: "Math", gpa: 4.0, awards: ["Best Footballer", "Valecdictorian Award"]},
{name: "Suleiman", age: 26, gpa: 3.5, awards: ("Best Basket Baller", "Best Mathematician")}])

//Important keywords when working with Mongosh and Mongodb Compass

//how to find collection
db.students.find({})

//query database
db.students.find({}, {_id: 0})

//Find database with awards
db.students.find({}, [])

//How To limit data Collection
db.students.find({}, {_id: 0}).limit(3)


//To sort Data Collection
db.students.find({}, {_id: 0}).sort({name: 1})

//To sort student who major in a particular course
db.students.find({major: "Chemistry"})

//To find student with gpa greater than 3.5
db.students.find({gpa: {$gt: 3.5}}, {_id:0})

//To find student with gpa less than or equal to 3.2 and to arrange the data in descending order
db.students.find({gpa: {$lt: 3.2}}, {_id: 0}).sort({gpa: -1})

//To return data collection that have award
db.students.find({awards: {$exists: true}}, {_id: 0})



