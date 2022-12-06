//array of strings
var strings = [
    "The first challenge",
    "The second challenge",
    "The third challenge",
]

//array of numbers 
var numbers = [
    1,
    2,
    3,
]

var result = []

//result contains strings array and numbers array according to indices and put them in an object
for (var i = 0; i < strings.length; i++) {
    result.push({
        id: numbers[i],
        groupName: strings[i],
        
    })
}

console.log(result)



