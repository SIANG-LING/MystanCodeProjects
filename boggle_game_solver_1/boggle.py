"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
# store all words in a list
dictionary_lst = []
# store words pre 2 alphabet
dictionary_lst_2 = []
# store words pre 3 alphabet
dictionary_lst_3 = []
# store found word
ans_lst = []
def main():
	"""
	TODO:
	"""
	start = time.time()
	####################
	#                  #
	#       TODO:      #
	#                  #
	####################
	read_dictionary()


	while True:
		print('1 row of letters: ',end='')
		first_row = input('').lower()
		first_row_lst = []
		if len(first_row) > 7:
			print('Illegal Input')
			break
		else:
			for i in range(7):
				if first_row[i].isalpha():
					first_row_lst.append(first_row[i])


			print('2 row of letters: ',end='')
			second_row = input('').lower()
			second_row_lst = []
			if len(second_row) > 7:
				print('Illegal Input')
				break
			else:
				for i in range(7):
					if second_row[i].isalpha():
						second_row_lst.append(second_row[i])

				print('3 row of letters: ',end='')
				third_row = input('').lower()
				third_row_lst =[]
				if len(third_row) >7:
					print('Illegal Input')
					break
				else:
					for i in range(7):
						if third_row[i].isalpha():
							third_row_lst.append(third_row[i])


					print('4 row of letters: ',end='')
					four_row = input('').lower()
					four_row_lst = []
					if len(four_row) > 7:
						print('Illegal Input')
						break
					else:
						for i in range(7):
							if four_row[i].isalpha():
								four_row_lst.append(four_row[i])


					#------------------------------#
					word_lst = [first_row_lst, second_row_lst, third_row_lst, four_row_lst]
					# i 當y
					# j 當x
					two_word = ''
					for i in range(4):
						for j in range(4):
							# 開頭字母
							first = word_lst[i][j]
							first_y = i
							first_x = j
							# print('start is :'+first)
							# k -> y
							# l -> x
							for k in range(-1, 2, 1):
								for l in range(-1, 2, 1):
									#print('first is ------------- i is :'+str(i)+'k is '+str(k)+'----- j is:'+str(j)+'l is :'+str(l))
									# 第二個
									if 0 <= l + j <= 3:
										if 0 <= k + i <= 3:
											sec= word_lst[k + i][l + j]
											sec_y = k+i
											sec_x = l+j
											#print('next word is  :' + sec)
											# avoid itself
											if l + j != j or k + i != i:
												two_word = first + sec
												#print('two word :'+two_word)
												# check if two_word in dictionary
												if has_prefix(two_word):
													#print('has prefix is true')
													# keep doing for the third word
													for m in range(-1, 2, 1):
														for n in range(-1, 2, 1):
															if 0 <= l + j + n <= 3:
																if 0 <= k + i + m <= 3:
																	# avoid itself ( 第三個不要等於第二個）
																	if l + j + n != l + j or k + i + m != k + i:
																		# avoid equal to first (do not repeat)
																		if (l + j + n) != first_x or (k + i + m)!= first_y:
																			#print('first x :'+str(first_x) +'and first y :'+ str(first_y))
																			#print('---------------------------------------')
																			#print('l : ' + str(l) + ' j: ' + str(j) + '  m:' + str(m))
																			#print('k : '+str(k)+' i: '+str(i)+'  n:'+str(n))
																			third = word_lst[k + i + m][l + j + n]
																			third_word = two_word + third
																			#print(third_word)
																			if has_prefix(third_word):
																				#print(third_word + '---->True')

																				for o in range(-1,2,1):
																					for p in range(-1,2,1):
																						if 0 <= l + j + n + p<= 3:
																							if 0 <= k + i + m+o <= 3:
																								# avoid itself ( 第四個不要等於第三個）
																								if l + j + n + p!= l + j +n or k + i + m+o != k + i+m:
																									# four != second
																									if  (l + j + n + p!= sec_x or k + i + m+o  != sec_y):
																										four = word_lst[ k + i + m+o][l + j + n + p]
																										four_word = third_word+four
																										#print(four_word)
																										if has_prefix(four_word) and four_word not in ans_lst:
																											ans_lst.append(four_word)
																											print('Found "'+four_word + '"')
																											for q in range(-1,2,1):
																												for r in range(-1,2,1):
																													#print('-------------------')
																													#print('l : '+str(l)+' j: '+str(j)+'  n:'+str(n)+' p: '+str(p)+' r: '+str(r))
																													#print('k : '+str(k)+' i: '+str(i)+'  m:'+str(m)+' o: '+str(o)+' q: '+str(q))
																													if 0<= l + j + n + p+r<=3:
																														if 0<=k + i + m+o+q <=3:
																															# fif != four
																															if l + j + n + p+r !=l + j + n + p or k + i + m+o+q!=k + i + m+o:
																																fif = word_lst[k + i + m+o+q][l + j + n + p+r]
																																fif_word = four_word+fif
																																#print(fif_word)
																																if has_prefix(fif_word):
																																	ans_lst.append(fif_word)
																																	print('Found '+fif_word)
					print('There are '+str(len(ans_lst))+'words in total.')
					break




	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open('dictionary.txt','r') as f:
		for line in f:
			line_lst = line.split(' ')
			dictionary_lst.append(line_lst[0][:-1])

			if len(line_lst[0]) >= 2:
				dictionary_lst_2.append(line_lst[0][:2])
			elif len(line_lst[0]) == 1:
				dictionary_lst_2.append(line_lst[0][0])

			if len(line_lst[0]) >= 3:
				dictionary_lst_3.append(line_lst[0][:3])
			elif len(line_lst[0]) == 2:
				dictionary_lst_3.append(line_lst[0][:2])
			elif len(line_lst[0]) == 1:
				dictionary_lst_3.append(line_lst[0][0])








def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""

	if len(sub_s) == 2:
		if sub_s in dictionary_lst_2:
			return True
		else:
			return False
	elif len(sub_s) == 3:
		if sub_s in dictionary_lst_3:
			return True
		else:
			return False
	else:
		if sub_s in dictionary_lst:
			return True
		else:
			return False





if __name__ == '__main__':
	main()
