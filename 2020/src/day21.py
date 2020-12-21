# https://adventofcode.com/2020/day/21

day = "21"

#part 1
# # txt = open("../input/day" + day + ".txt", "r")
# txt = open("../tst/day" + day + "_test.txt", "r")
# txt = txt.readlines()
# txt.append("\n")
# result = 0

# allergen_counter = {}
# total_allergs = set()
# max_terms = 0
# allergen_map = {}
# all_ingredients = set()
# all_ingredients_ls = []

# for l in txt:
#     if l == "\n":
#         ''
#     l = l.strip()
#     terms = l.split(' ')
#     ingredients = True
#     ingredient_ls = []
#     allergen_ls = []
#     for t in terms:
#         if t == "(contains":
#             ingredients = False
#             continue
#         if ingredients:
#             ingredient_ls.append(t)
#         else:
#             allergen_ls.append(t[:-1])
#     # print(ingredient_ls)
#     # print(allergen_ls)
#     first_iter = True
#     for a in allergen_ls:
#         total_allergs.add(a)
#         for i in ingredient_ls:
#             all_ingredients.add(i)
#             if first_iter:
#                 all_ingredients_ls.append(i)
#             if (a,i) not in allergen_counter:
#                 allergen_counter[(a,i)] = 0
#             allergen_counter[(a,i)] += 1
#             if allergen_counter[(a,i)] > max_terms:
#                 max_terms = allergen_counter[(a,i)]
#         first_iter = False
#     # print(terms)

# while True:
#     for e in allergen_counter:
#         if allergen_counter[e] == max_terms and e[0] not in allergen_map.keys() and e[1] not in allergen_map.values():
#             allergen_map[e[0]] = e[1]
#     if len(allergen_map) == len(total_allergs):
#         break
#     max_terms -= 1
# # print(allergen_map)

# missing_ingredients = set()
# for i in all_ingredients:
#     if i not in allergen_map.values():
#         missing_ingredients.add(i)
# # print(missing_ingredients)

# for i in all_ingredients_ls:
#     if i in missing_ingredients:
#         result += 1
# print(result)

#part 2
txt = open("../input/day" + day + ".txt", "r")
# txt = open("../tst/day" + day + "_test.txt", "r")
txt = txt.readlines()
txt.append("\n")
result = 0

allergen_counter = {}
total_allergs = set()
max_terms = 0
allergen_map = {}
all_ingredients = set()
all_ingredients_ls = []

for l in txt:
    if l == "\n":
        ''
    l = l.strip()
    terms = l.split(' ')
    ingredients = True
    ingredient_ls = []
    allergen_ls = []
    for t in terms:
        if t == "(contains":
            ingredients = False
            continue
        if ingredients:
            ingredient_ls.append(t)
        else:
            allergen_ls.append(t[:-1])
    first_iter = True
    for a in allergen_ls:
        total_allergs.add(a)
        for i in ingredient_ls:
            all_ingredients.add(i)
            if first_iter:
                all_ingredients_ls.append(i)
            if (a,i) not in allergen_counter:
                allergen_counter[(a,i)] = 0
            allergen_counter[(a,i)] += 1
            if allergen_counter[(a,i)] > max_terms:
                max_terms = allergen_counter[(a,i)]
        first_iter = False

true_allergen_counter = {}
max_occurrence_counter = {}

for e in allergen_counter:
    occurences = allergen_counter[e]
    key = e[0]
    if key not in max_occurrence_counter:
        max_occurrence_counter[key] = 0
    if occurences > max_occurrence_counter[key]:
        max_occurrence_counter[key] = occurences

for m in max_occurrence_counter:
    for e in allergen_counter:
        allergen, ingredient = e
        occurences = allergen_counter[e]
        if occurences == max_occurrence_counter[allergen]:
            true_allergen_counter[e] = occurences

allergen_map = {}
import copy
remaining_allergens = copy.deepcopy(total_allergs)

while True:
    if len(allergen_map) == len(total_allergs):
        break
    check_list = list(remaining_allergens)
    for allergen in check_list:
        occurences = 0
        for c in true_allergen_counter:
            if c[0] != allergen or c[1] in allergen_map.values():
                continue
            occurences += 1
            ingredient = c[1]
        if occurences == 1:
            allergen_map[allergen] = ingredient
            remaining_allergens.remove(allergen)


deadly_ings = list(allergen_map.keys())
deadly_ings.sort()

result = ""
for d in deadly_ings:
    result += allergen_map[d] + ","
print(result[:-1])
