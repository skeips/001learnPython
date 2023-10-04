
# A dictionary with nested dictionaries
my_dict = {
    "name": "Alice",
    "age": 25,
    "occupation": "Software Engineer",
    "contacts": {
        "phone": "(123) 456-7890",
        "email": "alice@example.com"
    },
    "courses": ["Python", "Java", "JavaScript"]
}

my_kanji = {
    "日" : {
        "kunyomi": "ひ・び・か",
        "onyomi": "にち・に"
    },
    "meaning": ['Sun', 'Day'],
    "example": ['日曜日', '日本'],

    "月" : {
        "kunyomi": "つき",
        "onyomi": "げつ・がつ"
    },
    "meaning": ['Moon', 'Month'],
    "example": ['月', '月曜日']
}


for key, value in my_kanji.items():
     print(key, value)

# # Get the value associated with a key
# print(my_dict["name"])

# # Check if a key exists in the dictionary
# if "age" in my_dict:
#     print(my_dict["age"])

# # Add a new key-value pair to the dictionary
# my_dict["country"] = "United States"

# # Update the value of an existing key-value pair
# my_dict["age"] = 26

# # Remove a key-value pair from the dictionary
# #del my_dict["occupation"]

# # Iterate over the keys in the dictionary
# for key in my_dict:
#     print(key)

# # Iterate over the values in the dictionary
# for value in my_dict.values():
#     print(value)

# # Iterate over the key-value pairs in the dictionary
# for key, value in my_dict.items():
#     print(key, value)
