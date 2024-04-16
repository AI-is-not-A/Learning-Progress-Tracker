string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
vowels_counter = 0
for char in string:
    if char in vowels:
        vowels_counter += 1
print(vowels_counter)
