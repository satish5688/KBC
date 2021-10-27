
import random,time, pyttsx3
from pyttsx3 import engine

engine = pyttsx3.init()

QUE=["Who is the prime minister of india ?","What is the age limit for NDA exam ?","what is the tenure of president ?","who is the father of computer ?","how many states are in india ?","which is the largest state in india by area ?","Which state has biggest economy ?","Which state has biggest sea border ?","Which state founded on the bassic of language firstly ?"," Which is smallest state by area ?","How many article in our constitution ?","Which is last point of india in south ?","How many members in indian parlement ?","What is the rank of india in defence ?"]
op1=["1) Narendra Modi","1) 20 years","1) 6 years","1) Morgun Moly","1) 27","1) Madhyapradesh","1) Maharastra","1) Tamilnadu","1) kerala","1) sikkim","1) 300","1) tamilnadu","1) 300","1) 1"]
op2=["2) Rajnath Sing","2) 18.5 years","2) 5 years","2) Robert Patricia","2) 28","2) Rajsthan","2) Goa","2) Kerala","2) Telangana","2) Goa","2) 350","2) Andaman","2) 400","2) 2"]
op3=["3) Manmohan Sing","3) 17.5 years","3) 4 years","3) Charles Babbage","3) 29","3) Maharastra","3) Delhi","3) Maharashtra","3) Andrapradesh","3) Meghalaya","3) 395","3) Lakshadip","3) 555","3) 3"]
op4=["4) Amit Shah","4) 19.5 years","4) 8 years","4) Darma Saty","4) 30","4) Uttar pradesh","4) Punjab","4) Gujrat","4) Tamilnadu","4) Nagaland","4) 400","4) Indira point",'4) 545',"4) 4"]
ans=[1,4,2,3,2,2,1,4,3,2,3,4,4,4]
while True:
    m=["(1)50-50 Lifeline","(2) Phone of friend","(3) Audience Pole","(4) Flip the Question ","(5) Gochi"]
    mq=0
    w=["you have used this lifelies "]
    fifty,total, flip, call,coin, pole,gochi,o1, o2, o3, o4,repeat=0,0,0,0,0,0,0,0,0,0,0,[]
    while mq<len(QUE):
        q=random.randint(0,13)
        if q in repeat:
            continue
        mq+=1
        print("\033[1m""This is your question on.",mq,"for",coin+10000,"\033[0m")
        repeat.append(q)
        print()
        print("\x1b[31m"f'{mq}]',QUE[q],"\x1b[0m")
        engine.say(QUE[q])
        engine.runAndWait()
        print("\x1b[32m",op1[q])
        engine.say(op1[q])
        engine.runAndWait()
        print("\x1b[32m",op2[q])
        engine.say(op2[q])
        engine.runAndWait()
        print("\x1b[32m",op3[q])
        engine.say(op3[q])
        engine.runAndWait()
        print("\x1b[32m",op4[q])
        engine.say(op4[q])
        engine.runAndWait()
        print("\x1b[33m""5) Use Lifeline .")
        a=int(input("\x1b[34m""enter your option number :""\x1b[0m"))
        if a==5:
            while True:
                if flip or fifty or call or pole or gochi >1:
                    for A in w:
                        print("\x1b[31m",A,"\x1b[0m")
                print("*** you can use this lifelines only ones.")
                for z in m:
                    print("\x1b[35m""   ",z,"\x1b[0m")
                b=int(input(":="))
                n=m.pop(b-1)
                m.insert(b-1," ")
                w.append(n)
                if b==1:
                    fifty+=1
                    if fifty>1:
                        print("\x1b[31m""(1) 50-50 Lifeline ""\x1b[0m")
                        continue
                    else:
                        answers = [op1[q], op2[q], op3[q], op4[q]]
                        realans = answers.pop(ans[q]-1)
                        shuf = [realans, random.choice(answers)]
                        random.shuffle(shuf)
                        print("your 50-50 lifeline is.\n", shuf[0],"\n", shuf[1])
                        a=int(input("\x1b[34m""enter your opption number :""\x1b[0m"))
                        break 
                elif b==2:
                    call+=1
                    if call>1:
                        continue
                    else:
                        print("\033[1m""your friend suggested option no.",ans[q],"\033[0m")
                        a=int(input("\x1b[34m""enter your opption number :""\x1b[0m"))
                        break
                elif b==3:
                    pole+=1
                    if pole>1:
                        print("you have used this so you cant use this again.\nuse something different lifeline.")
                        continue
                    for v in range(100):
                        e=random.randint(1,4)
                        if e==1:
                            o1+=1
                        elif e==2:
                            o2+=1
                        elif e==3:
                            o3+=1
                        elif e==4:
                            o4+=1
                    print("option 1 :",o1,"%")
                    print("option 2 :",o2,"%")
                    print("option 3 :",o3,"%")
                    print("option 4 :",o4,"%")
                    a=int(input("\x1b[34m""enter your option number :""\x1b[0m"))
                    break   
                
                elif b==4:
                    flip+=1
                    if flip>1:
                        continue
                    if flip==1:
                        que2=["Who is the prime minister of israel?","How many contries has veto power ?","which is the smallest nation in world by area ?","when was Himachal pradesh established","where is horn of Africa ?"]
                        Op1=["1) Neftali Benet","1) 6","1) Italy ","1) 1972 ","1) East africa"]
                        Op2=["2) Berjamin netnyhay",'2) 7',"2) vetican city","2) 1971","2) west africa"]
                        Op3=['3) Yasle leaweli','3) 5',"3) mexico ","3) 1975","3) central africa"]
                        Op4=["4) Nareadra medi","4) 8", '4) panama',"4) 1980","4) south africa."]
                        Ans=[1,3,2,2,1]
                        c=random.randint(0,4)
                        print()
                        print("\x1b[31m",que2[c])
                        print("\x1b[32m",Op1[c])
                        print("\x1b[32m",Op2[c])
                        print("\x1b[32m",Op3[c])
                        print("\x1b[32m",Op4[c],"\x1b[0m")
                        d=int(input("\x1b[34m""enter your option nunbere :""\x1b[0m"))
                        if d==Ans[c]:
                            coin+=10000
                            a = ans[q]
                        break             
                elif b==5:
                    if gochi>1:
                            continue
                    else:
                        print("Welcome to gochi lifeline :)")
                        print("Close your eyes for 10 seconds and then type your answer then it will be correct :)")
                        time.sleep(10)
                        a=int(input("Good Luck enter your answer: "))
                        break
        if a==ans[q]:
            coin+=10000
            print("\x1b[36m""Congratulation! your answer is correct.\n you won",coin,"rupees.""\x1b[0m")
            if mq!=len(QUE)-1:
                total+=coin
                print()
        else:
            print("\033[3m""Wooo... your answer is wrong , So you are  out of Game.""\033[3m")
            break
    print("\033[3m""Now your are going out of game \n so totaly you won",total,"rupees from our KBC.""\x1b[0m")
    p=input("Do you want to play again y/n :")
    if p=="y":
        continue
    else:
        break
