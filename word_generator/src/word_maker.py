import random

NUM_WORDS_TO_GENERATE = 1000
words = open('words', 'r')
word_list		= []
#word_length 	= {key: 0 for key in range(1,21)}
word_len_list	= []
alpha_dict		= {chr(key+97): '' for key in range(26)}
word_start		= []

for word in words:	
	word = word.strip().lower()
	for index in range(len(word)-1):
		# print(word[index+1],end='')
		alpha_dict[word[index]] += word[index+1]
	# print("")
	#word_length[len(word)]+=1
	word_start.append(word[0])
	word_len_list.append(len(word))
	word_list.append(word)

new_len = random.choice(word_len_list)

for _ in range(NUM_WORDS_TO_GENERATE):
	len_word = random.choice(word_len_list)
	new_word = ""
	new_word = random.choice(word_start)
	for num in range(len_word-1):
		new_word += random.choice(alpha_dict[new_word[-1]])
	print(new_word,end=",")


