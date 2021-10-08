'''与えられた単語をなんちゃってラテン語に変換する'''
import sys

# 母音
VOWELS = "aiueoy"

while True:
    word = input("Type a word, you want to transform to PigLatin")

    if word[0] in VOWELS:
        pig_Latin = word + "way"
    else:
        pig_Latin = word[1:] + word[0] + "ay"

    print("\n\n")
    # 「致命的なエラー」の設定を使い、IDLEをごまかして名前を赤く表示する
    print("{}".format(pig_Latin), file=sys.stderr)
    print("\n\n")

    try_again = input("\n\nTry again? (Press Enter else n to quit)\n")
    if try_again.lower() == "n":
        sys.exit()
