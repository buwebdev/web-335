/**
	Title: users.js
    Author: Professor Krasso
    Date: 11 August 2022
    Description: MongoDB Shell Scripts for the users collection.
 */

/**
 * User document clean-up. 
 */
db.users.deleteOne({"email": "jbach@me.com"})
db.users.deleteOne({"email": "lbeethoven@me.com"})
db.users.deleteOne({"email": "wmozart@me.com"})
db.users.deleteOne({"email": "jbrahms@me.com"})
db.users.deleteOne({"email": "rwagner@me.com"})
db.users.deleteOne({"email": "cdebussy@me.com"})

/**
 * Create six User documents. 
 */
bach = {
	"firstName": "Johann",
	"lastName": "Bach",
	"employeeId": "1007",
	"email": "jbach@me.com",
	"dateCreated": new Date()
}

ludwig = {
	"firstName": "Ludwig",
	"lastName": "Beethoven",
	"employeeId": "1008",
	"email": "lbeethoven@me.com",
	"dateCreated": new Date()
}

mozart = {
	"firstName": "Wolfgang",
	"lastName": "Mozart",
	"employeeId": "1009",
	"email": "wmozart@me.com",
	"dateCreated": new Date()
}

brahms = {
	"firstName": "Johannes",
	"lastName": "Brahms",
	"employeeId": "1010",
	"email": "jbrahms@me.com",
	"dateCreated": new Date()
}

wagner = {
	"firstName": "Richard",
	"lastName": "Wagner",
	"employeeId": "1011",
	"email": "rwagner@me.com",
	"dateCreated": new Date()
}

debussy = {
	"firstName": "Claude",
	"lastName": "Debussy",
	"employeeId": "1012",
	"email": "cdebussy@me.com",
	"dateCreated": new Date()
}

/**
 * Insert the newly created user documents.
 */
db.users.insertOne(bach)
db.users.insertOne(ludwig)
db.users.insertOne(mozart)
db.users.insertOne(brahms)
db.users.insertOne(wagner)
db.users.insertOne(debussy)