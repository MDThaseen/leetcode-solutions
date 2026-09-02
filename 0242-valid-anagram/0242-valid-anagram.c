bool isAnagram(char* s, char* t) {
    if (strlen(s) != strlen(t)) {
        return false;
    }

    int countS[26] = {0};
    int countT[26] = {0};

    for (int i = 0; s[i] != '\0'; i++) {
        countS[s[i] - 'a']++;
        countT[t[i] - 'a']++;
    }

    for (int i = 0; i < 26; i++) {
        if (countS[i] != countT[i]) {
            return false;
        }
    }

    return true;
}
