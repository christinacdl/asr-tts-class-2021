import sys

general_lexicon = sys.argv[1]
wordlist = sys.argv[2]
output_file = sys.argv[3]

with open(general_lexicon) as lex:
    with open(wordlist) as wlist:
        with open(output_file,"w") as ofile:
            gen_lex = {}
            for line in lex:
                cline = line.rstrip()
                line_info = cline.split(" ")
                word = line_info[0]
                pronunciation = " ".join(line_info[1:])
                gen_lex[word] = pronunciation

                for line in wlist:
                    word = line.rstrip()
                    if word in gen_lex:
                        ofile.write("{} {}\n".format(word,gen_lex[word]))
                    else:
                        print("Unknown pronunciation for word: {}".format(word))