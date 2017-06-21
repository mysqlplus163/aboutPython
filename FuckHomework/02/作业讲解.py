# 使用while循环输出1 2 3 4 5 6     8 9 10
# count=1
# while count < 11:
#     if count == 7:
#         count+=1
#         continue
#     print(count)
#     count+=1

#
# count=1
# while count < 11:
#     if count != 7:
#         print(count)
#     count+=1


#求1-100的所有数的和

# count=1
# res=0
# while count <= 100:
#     res+=count
#     count+=1
# print(res)
#
# res=0
# for i in range(1,101):
#     res+=i
# print(res)

#
# count=1
# while count <= 100:
#     if count % 2 == 0:
#         print(count)
#     count+=1

# count=1
# res=0
# while count <= 4:
#     if count % 2 ==0:
#         res-=count
#     else:
#         res+=count
#     count+=1
#
# print(res)



# count=1
# while count <= 3:
#     u=input('u>>: ')
#     p=input('p>>: ')
#     if u == 'egon' and p == '123':
#         print('login ok')
#         break
#     count+=1



count=0

while True:
    if count == 3:
        print('try too many times')
        break
    u=input('u>>: ')
    p=input('p>>: ')
    if u == 'egon' and p == '123':
        print('login ok')
        break
    count+=1


