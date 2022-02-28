poem = "Centre of equal daughters, equal sons, All, all alike endeared, grown, ungrown, young or old, Strong, ample, fair, enduring, capable, rich, Perennial with the Earth, with Freedom, Law and Love, A grand, sane, towering, seated Mother, Chaired in the adamant of Time."
newpoem=poem
for letter in poem:
    if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u':
        newpoem = newpoem.replace(letter, "")
print(newpoem)