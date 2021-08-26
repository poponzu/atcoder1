# 計算量O(xn^2)
def joinwords1(words):
    sentence = ""
    for w in words:
        sentence = sentence + w
    return sentence

# 計算量O(xn)?
def joinwords2(words):
    sentence = []
    for w in words:
        sentence.append(w)
    return "".join(sentence)


list = ["abcd", "efgh", "hijk", "lmno", "pqrs"]

print(joinwords1(list))
print(joinwords2(list))
