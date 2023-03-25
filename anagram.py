def check(str1, str2):
	if(sorted(str1)== sorted(str2)):
		print("The strings are anagrams.")
	else:
		print("The strings aren't anagrams.")
str1 ="listen"
str2 ="silent"
check(str1, str2)
