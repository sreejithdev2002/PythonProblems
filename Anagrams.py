string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if len(string1) != len(string2):
    print("The strings are not anagrams.")
else:
    sorted_string1 = sorted(string1.lower())
    sorted_string2 = sorted(string2.lower())

    if sorted_string1 == sorted_string2:
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")