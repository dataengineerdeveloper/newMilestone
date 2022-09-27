 # using count to check number of letter in n
n = 'hello world'
 # >> COUNT >> number of characters appear in variable
print(n.count('l'))
 # FIND >> tells us where is located the word
print(n.find('world')) 
 # to get a negative one , we can simulate a word that doesn't existe in variable
print(n.find('Universe'))   

 # REPLACE > WE CAN USE A SECONDS VARIABLE TO PERFORM THE REPLACE
n_new =  n.replace('world','universe')
print(n_new)


gretting = 'hello'
name = 'luis'
 #1 options
 # message = gretting + ',' + name + ' .Welcome!'
 # 2options >> e indicate the correct format for our string variable
 # message = '{},  {}. Welcome!'.format(gretting,name)
 #3options
message = f'{gretting},  {name}. Welcome!'

print(message) 




 # imagine that we need to see all functions available for a particular variable,  it'll list all functions and if we don't know how does it work
print(help(str))
help(print)

print(help(str.join))
