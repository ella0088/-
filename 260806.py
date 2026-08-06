##number=1
##multi=1
##
##while multi<5000:
##    multi*=number
##    if multi>=5000:
##        break
##    number+=1
##print(f'number : {number}\nmulti : {multi}')




##num=0
##
##while num<50:
##    num+=1
##    if num%3==0 or num%5==0:
##        continue
##    print(num,end=" ")




##num1=int(input("숫자1 : "))
##num2=int(input("숫자2 : "))
##
##if num1<num2:
##    while True:
##        num1+=1
##        number=num1**2
##        if num1==num2:
##            break
##        print(number, end=' ')
##
##if num1>num2:
##    while True:
##        num2+=1
##        number=num2**2
##        if num1==num2:
##            break
##        print(number, end=' ')




##txt=input("문장을 입력해주세요 : ")
##count=-1
##
##while count<len(txt):
##    if count%2==1:
##        count+=1
##        continue
##    print(txt[count],end='■')
##    count+=1

#random 문제 
##import random
##
##count=0
##while count<20:
##    print(random.randint(3,11),end=' ')
##    count +=1

##import random
##
##count=0
##while count<7:
##    print(random.randrange(2,100+1,5))
##    count +=1


##import random
##
##answer=random.randint(1,100)
##
##while True:
##    num=int(input("1~100 사이 숫자를 입력해 주세요 : "))
##    if num==answer:
##        print("정답입니다.")
##        break
##    elif num>answer:
##        print("더 낮은 숫자가 정답입니다.")
##    elif num<answer:
##        print("더 높은 숫자가 정답입니다.")



##import random
##
##answer=random.randint(1,1000)
##count=0
##while True:
##    num=int(input("1~1000 사이 숫자를 입력해 주세요 : "))
##    count+=1
##    if num==answer:
##        print(f"정답입니다.\n현재 입력 횟수 {count}")
##        break
##    elif num>answer:
##        print("더 낮은 숫자가 정답입니다.")
##    elif num<answer:
##        print("더 높은 숫자가 정답입니다.")


##while True:
##    import random
##    N=str(random.randint(100,999))
##    
##    num100=N[0]
##    
##    num10=N[1]
##    
##    num1=N[2]
##
##    if num100!=num10 and num100!=num1 and num10!=num1:
##        break
##print(N)
    



##import random
##
##
##N=0
##num100=0
##num10=0
##num1=0
##
##while True:
##    num=random.randint(100,999)
##    N=str(num)
##    num100=N[0]
##    num10=N[1]
##    num1=N[2]
##
##    if num100!=num10 and num100!=num1 and num10!=num1:
##        break
##
##while True:
##    strike=0
##    ball=0
##    answer=input("세자리 숫자를 입력해주세요 : ")
##    ans=answer
##
##    ans100=ans[0]
##    ans10=ans[1]
##    ans1=ans[2]
##
##    if num100==ans100:
##        strike+=1
##    elif ans100 in N:
##        ball+=1
##
##    if num10==ans10:
##        strike+=1
##    elif ans10 in N:
##        ball+=1
##
##    if num1==ans1:
##        strike+=1
##    elif ans1 in N:
##        ball+=1
##
##    if strike==3:
##        print(strike,'strike,',ball,'ball')
##        print('정답!')
##        break
##    print(strike,'strike,',ball,'ball')









##for i in range(5,100+1,5):
##    print(i,end=" ")




##num=0
##for i in range(3,99+1,3):
##    num+=i
##
##print('3의 배수의 합 :',num)


#for문 문제3
start=int(input("시작값 입력 : "))
end=int(input("끝값 입력 : "))

for i in range(start,end+1):
    
          



















    
