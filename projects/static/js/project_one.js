var firstName = prompt("First Name?")

var lastName = prompt("Last Name?")

var age = prompt("Age?")

var height = prompt("Height (cm)?")

var petName = prompt("Pet name?")


if(firstName[0] === lastName[0]
    && age >= 20 && age <= 30
    && height > 170
    && petName[petName.length-1] === "y"){
    console.log("You are a spy!")
}
else{
    console.log('Nothing to see here...')
}