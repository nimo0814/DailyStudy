from selenium import webdriver
user_file=open('user_info.txt', 'r')
lines=user_file.readlines()
user_file.close()

for line in lines:
    username=line.split(',')[0]
    #print(lines)
    password=line.split(',')[1]
    print(username,password)