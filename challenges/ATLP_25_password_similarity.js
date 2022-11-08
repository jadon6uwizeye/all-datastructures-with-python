function pwdSimilar(arr) {

    // array of vowels
    const vowels = ['a', 'e', 'i', 'o', 'u'];

    // check if the number of vowels in arr is equal to the number of consonants
    let vowelCount = 0;
    let consonantCount = 0;
    for (let i = 0; i < arr.length; i++) {
        if (vowels.includes(arr[i])) {  
            vowelCount++;
        } else {
            consonantCount++;
        }
    }

    if (vowelCount === consonantCount) {
        return 0;
    }else if (vowelCount > consonantCount) {
        return 1;
    } else {
        return 2;
    }
}


function countMinimumOperations(password) {
    // Write your code here
    let count = 0;

    const vowels = ['a', 'e', 'i', 'o', 'u'];

    // all alphabets in lowercase
    const alphabets = 'abcdefghijklmnopqrstuvwxyz';

    let arr = password.split("");

    
    while (pwdSimilar(arr) != 0) {
        // console.log(pwdSimilar(arr));
        // encrement or decrement the character in arr if it is not a or z
        for (let i = 0; i < arr.length; i++) {
            // print the array
            console.log(arr);
            if (arr[i] != 'a' && arr[i] != 'z') {
                let index = alphabets.indexOf(arr[i]);
                if (pwdSimilar(arr) === 2)  {
                    if(vowels.includes(alphabets[index + 1])) {
                        arr[i] = alphabets[index + 1];
                        count++;
                        continue;
                    }else if(vowels.includes(alphabets[index - 1])) {
                        arr[i] = alphabets[index - 1];
                        count++;
                        continue;
                    }
                    continue;
                }else if(pwdSimilar(arr) === 1) {
                    if(!vowels.includes(alphabets[index + 1])) {
                        arr[i] = alphabets[index + 1];
                        count++;
                        continue;
                    }else if(!vowels.includes(alphabets[index - 1])) {
                        arr[i] = alphabets[index - 1];
                        count++;
                        continue;
                    }
                    continue;
                }
            }else{
                continue;
            }
        }
    }
    
    return count;
}

console.log(countMinimumOperations("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"));