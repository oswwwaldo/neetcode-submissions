class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {

        let matchingCharsA = [...s].sort().join("");
        let matchingCharsB = [...t].sort().join("");

        if (matchingCharsA === matchingCharsB) {
            return true;
        }

        return false;
    
    }
}
