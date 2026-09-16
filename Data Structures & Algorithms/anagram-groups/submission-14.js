class Solution {
    groupAnagrams(strs) {


        const groups = {};
        for (const str of strs) {
            const key = str.split('').sort().join('');
            if (!groups[key]) {
                groups[key] = [];
            }

            groups[key].push(str)
        }

        return Object.values(groups);
    }
}

// remove already scanned elements
// account for duplicated strings

// loop through strings
// compare current string with the next string and repeat
// array -> sort -> join === (compare)
// if true, add in dynamically created array variable
// remove strings that have already been checked