class Student:
    def __init__(self, Id , name , lastname ):
        self.id= Id
        self.name =name
        self.lastname = lastname
        

    def __str__(self):
        return self.name + self.lastname + self.id
    def getname (self):
        return self.name
    def getlastname (self):
        return self.lastname
    def getid (self):
        return self.id
q=open("student.txt","r",encoding="utf-8")
students=[]
k=[]
for i in q:
    another= i.split()
    kjr=another[0]
    i=i.strip()
    k.append(kjr)
    s=i.split()
    a=Student(s[0],s[1],s[2])
    students.append(a)
q.close()

class university:
    def __init__(self, number, uniname  ,basepoint ,quato ):
        self.uniname=uniname
        self.number= number
        self.basepoint=basepoint
        self.quato= quato
        

    
    def getuniname(self):
        return self.uniname
    def getnumber (self):
        return self.number
    def getbasepoint(self):
        return self.basepoint
    def getquato(self):
        return self.quato
    
    
   
r= open("university.txt","r",encoding="utf-8")
unitxt=open("new.txt","w",encoding="utf-8")
uni=[]
unilist=[]
for u in r:
    u=u.strip()
    new=u.split(",")
    newone=new[1]
    unilist.append(newone)# lenght alabilme için
    unitxt.write(newone +"\n")
    b=university(new[0],new[1],new[2],new[3])
    uni.append(b)
r.close()
unitxt.close()




#for i in range(len(k)):
    #print(students[i].getid(),students[i].getname(),students[i].getlastname(),uni[i].getuniname(),uni[i].getbasepoint(),uni[i].getquato())


#print(students[0].getname(),students[0].getlastname(),students[0].getid())
#print(students[0])

class datas:  
#book type, number of correct, incorrect and blank answers, number of answers after
#reducing the wrong ones based on the formula given above, score, name of the
    def __init__ (self,booktype,true,false,blank,net,point):
        self.booktype=booktype
        self.true=true
        self.false=false
        self.blank=blank
        self.net=net
        self.point=point

    def getbooktype(self):
        return self.booktype
    def gettrue(self):
        return self.true
    def getfalse(self):
        return self.false
    def getblank(self):
        return self.blank
    def getnet(self):
        return self.net
    def getpoint(self):
        return self.point

data=[]
general=[] #booktype list
answerss=[]# answers list
keys=[]
students_choices=[]#öğrencierin üni tercihlerini sıralar

w=open("answers.txt","r",encoding="utf-8")
for iy in w:
    ar= iy.split()
    wr= ar[1] #booktype
    wt= ar[2] #answers
    xyz= ar[3:] #choices
    
    general.append(wr)
    answerss.append(wt)
    students_choices.append(xyz)
    
w.close()

students_choices2=[]# öğrencierin üni isim tercihlerini sıralar 6 lı liste


for i in students_choices:
    a1=int(i[0])
    a1=a1-1
    a2=int(i[1])
    a2=a2-1
    a3=int(i[2])
    a3=a3-1
    a4=int(i[3])
    a4=a4-1
    a5=int(i[4])
    a5=a5-1
    
    a6=uni[a1].getuniname()# bu bir class oldugu için saymaya sıfırdan başlar bu yüzden a1 vb den 1 çıkardık.
    a7=uni[a2].getuniname()
    a8=uni[a3].getuniname()
    a9=uni[a4].getuniname()
    a10=uni[a5].getuniname()
    a11= a6 + ", " + a7 + ", " + a8 + ", " + a9 +", " + a10
    students_choices2.append([a11]) # her öğrencisin üni tercihlerinin isimlerini yazar önce 1. öğrenci ve ilk 5 tercihi son 2.
      



e=open("key.txt","r",encoding="utf-8")
for i in e:
    keys.append(i)

a=keys[0]    
keys[0]= a[:-1]

ansa= keys[0] #book a key
ansb= keys[1] #book b key
e.close()


trs=[] # doğruların listesi
flss=[] #list of falses
emps=[] # list of blankes
nets=[] # list of net
points=[] #list of points
pointscounter=[] # points in aynısı


for i in range (len(general)): # range of booktype general means 
    
    if general[i]=="B":
        
        tr=0 # 
        fls=0
        emp=0
        for ak in range(len(ansb)):
            if answerss[i][ak] in ansb[ak]:
                tr= tr+1
            elif answerss[i][ak]=="-":
                emp=emp+1
            else:
                fls=fls+1
            
        trs.append(tr)
        flss.append(fls)
        emps.append(emp)
        arty= flss[i]
        artyz= float(arty/4)
        arky=trs[i]
        ets= arky-artyz
        ets2=ets*15
        nets.append(ets)
        points.append(ets2)
        pointscounter.append(ets2)
        a=str(students_choices2[i]) # str ye çevirdik çünkü sondaki [] işaretlerini silmek için
        b= a[1:-1]
        mp3.append(b)
    
    if general[i]=="A":
        tr=0
        fls=0
        emp=0
        for az in range(len(ansb)):
            if answerss[i][az] in ansa[az]:
                tr= tr+1
            elif answerss[i][az]=="-":
                emp=emp+1
            else:
                fls=fls+1
        
        
        trs.append(tr)
        flss.append(fls)
        emps.append(emp)
        arty= flss[i]
        artyz= float(arty/4)
        arky=trs[i]
        ets= arky-artyz
        ets2=ets*15
        nets.append(ets)
        points.append(ets2)
        pointscounter.append(ets2)
        mp3=[]
        a=str(students_choices2[i])
        b= a[1:-1]
        mp3.append(b)# student choices 6 lı üni isimleri ve listten çıkarılmış hali

for i in range(len(general)):
    
    ax= datas(general[i],trs[i],flss[i],emps[i],nets[i],points[i]) # booktype, trues , falses , blanks,nets,points bunlarla bunları datas classına ekler
    data.append(ax) #a turle name of data for datas class

awe=points[:] #clone of points
acg=points[:] # clone of points

#for i in range(len(general)):
    #print(data[i].getbooktype(),data[i].gettrue(),data[i].getfalse(),data[i].getblank(),data[i].getnet(),data[i].getpoint())

#NOW WE CAN USE ALL CLASSES!!!!"












def Id ():
    n= input("please enter Id:")
    x=list(n)
    for i in range(len(k)):
        if students[i].getid()== n and len(students[i].getid()) == len(x):
            a=students[i].getname()+" "+ students[i].getlastname()
            return a   
    


#print(Id())
def unibase ():

    q = open("university.txt", "r", encoding="utf-8")
    b = []
    c = []
    d = []
    e = []
    d_counter = []
    t = 0
    for i in q:
        a = i.split(",")
        h = a[0] #number of universtiy
        b.append(h) # list of number of university
        g = a[1] #name of uni
        c.append(g) #list of uni names
        j = a[2] # base point of uni
        d.append(j) # list of uni's base points
        d_counter.append(j) # same with d 
        u = int(a[3]) # quato of üni
        e.append(u) # list of uni's quatos



    d.sort() # sort of the uni base points
    d.reverse() #reverse # şu an maxdan mine puanlar sıralandı
    
    gh=[] #indexlerin fazlalıgının olmayan hali
    indexler = [] #d nin d counterdaki yerini verir
    for i in range(len(d)):
        for index in range(len(d)):
            if d[i] == d_counter[index]: # eğer d[i] d_counter[index] e eşitse index numarasını alır 0 1 2 3 gibi
                indexler.append(index) # bunu indenxler listesine ekler
    for i in range(len(indexler)):
        if indexler[i] not in indexler[i+1:]: #eğer i elemanı geri kalan index listesinde yoksa yazar
            ab=indexler[i]
            gh.append(ab) # gh listesine ekler
    
    
    for k in gh:
        print(c[k],float(d_counter[k])) # c uninames o üni ismini çağırır, d conuter da o üninin puanının çağırır 
     
#unibase()  

def departmentsbonus():
    r=open("university.txt","r",encoding="utf-8")
    unitxt=open("new.txt","w",encoding="utf-8") # istediğimiz dataları bu txt ye yazacak
    
    for u in r:
        u=u.strip() # fazlalıkları siler n gibi
        new=u.split(",")
        newone=new[1]+"," # her eleman arasına virgül koyar
        unitxt.write(newone +"\n")
    r.close()
    unitxt.close()
    edit2=[]
    newr=open("new.txt","r",encoding="utf-8") # new txt ye yazılanlar çağırır
    
   
        
    edit=[]

    for i in newr:
        splits=i.split() #boşluklara göre split eder
        for y in range (len(splits)):
            if splits[y]=="University": # eğer bu kelimeye eşitse
                ar=splits[y+1:] # o kelimeden sonrasını alır
                edit.append(ar) # edit listesine ekler
    #print(edit)
    bonus=[]
    for i in range(len(edit)):
        if edit[i] not in edit[i+1:]: # eğer birden çok department varsa silmek için
            for i in edit[i]: #
                print(i,end=" ") 
            print() # her elemandan sonra alt satıra geçmesi için
            

        
#departmentsbonus()


def result ():
    data=[]
    general=[] #booktype list
    answerss=[]# answers list
    keys=[]

    w=open("answers.txt","r",encoding="utf-8")
    qe=open("result.txt","w",encoding="utf-8")
    for iy in w:
        ar= iy.split()
        wr= ar[1] #booktype
        wt= ar[2] #answers
        general.append(wr)
        answerss.append(wt)
        
    

    e=open("key.txt","r",encoding="utf-8")
    for i in e:
        keys.append(i)

    a=keys[0]    
    keys[0]= a[:-1] #sondaki n leri silmek için

    ansa= keys[0] #book a key
    ansb= keys[1] #book b key
    e.close()


    trs=[] # doğruların listesi
    flss=[] #list of falses
    emps=[] # list of blankes
    nets=[] # list of net
    points=[] #list of points
    mp4=[] #student choice2nin listten çıkarılmış hali
    for i in range (len(general)):
        
        if general[i]=="B":
            
            tr=0
            fls=0
            emp=0
            for ak in range(len(ansb)):
                if answerss[i][ak] in ansb[ak]:
                    tr= tr+1
                elif answerss[i][ak]=="-":
                    emp=emp+1
                else:
                    fls=fls+1
                
            trs.append(tr)
            flss.append(fls)
            emps.append(emp)
            arty= flss[i]
            artyz= float(arty/4)
            
            arky=trs[i]
            ets= float(arky-artyz)
            ets2=ets*15
            nets.append(ets)
            points.append(ets2)
            a=str(students_choices2[i])
            b= a[1:-1]
            
            mp4.append(b)
            
            dataline = str(students[i].getid()) +", " + str(students[i].getname())+", " +str(students[i].getlastname())+", "+ str(general[i])+", " +str(trs[i])+", " +str(flss[i])+", "+ str(emps[i])+", "+str(nets[i])+", "+str(points[i])+", "+str( mp4[i])
            qe.write(dataline + "\n")
        if general[i]=="A":
            tr=0
            fls=0
            emp=0
            for az in range(len(ansb)):
                if answerss[i][az] in ansa[az]:
                    tr= tr+1
                elif answerss[i][az]=="-":
                    emp=emp+1
                else:
                    fls=fls+1
                
            
            
            trs.append(tr)
            flss.append(fls)
            emps.append(emp)
            arty= flss[i]
            artyz= float(arty/4)
            arky=trs[i]
            ets= arky-artyz
            ets2=float(ets*15)
            nets.append(ets)
            points.append(ets2)
            a=str(students_choices2[i])
            b= a[1:-1]
            
            mp4.append(b)
               
            dataline= str(students[i].getid()) +", " + str(students[i].getname())+", " +str(students[i].getlastname())+", "+ str(general[i])+", " +str(trs[i])+", " +str(flss[i])+", "+ str(emps[i])+", "+str(nets[i])+", "+str(points[i])+", "+str( mp4[i])
            qe.write(dataline + "\n")

    w.close()
    qe.close()
   

#result()



def studentmax():
    indexs=[]
    news2=[]
    awe.sort()
    awe.reverse()
    for i in range(len(awe)):
        for y in range(len(awe)):
            if awe[i]==pointscounter[y]:
                indexs.append(y)
    for i in range(len(indexs)):
        if indexs[i] not in indexs[i+1:]:
            aym=indexs[i]
            news2.append(aym)
    for y in news2:
        print(students[y].getid(),students[y].getname(),students[y].getlastname(),points[y])
    

#studentmax()


def xyz():
    if choice==1:
        nes=[]# list of names and surnames
        short= Id()
        
        
        for i in range(len(general)):
            nes.append(students[i].getname()+" "+students[i].getlastname())

        if short in nes:
            print(short)
        else:
            print("Not found")


#xyz()


def yerleştirme():
    indexs=[]
    news2=[]
    q = open("university.txt", "r", encoding="utf-8")
    b = []#uninumber
    c = []#uniname
    d = []#basepoint
    e = []#capacity
    d_counter = []
    t = 0
    for i in q:
        a = i.split(",")
        h = a[0] #number of universtiy
        b.append(h) # list of number of university
        g = a[1] #name of uni
        c.append(g) #list of uni names
        j = a[2] # base point of uni
        d.append(j) # list of uni's base points
        d_counter.append(j) # same with d 
        u = int(a[3]) # quato of üni
        e.append(u) # list of uni's quatos



    d.sort() # sort of the uni base points
    d.reverse() #reverse
    
    
    gh=[] #indexlerin fazlalıgını siler
    indexler = [] #d nin d counterdaki yerini verir
    for i in range(len(d)):
        for index in range(len(d)):
            if d[i] == d_counter[index]: 
                indexler.append(index)
    for i in range(len(indexler)):
        if indexler[i] not in indexler[i+1:]: #eğer i elemanı geri kalan index listesinde yoksa yazar
            ab=indexler[i]
            gh.append(ab)

    uninumber=[]#uninumber sırlaanmış
    unibasepoint=[] #unibasepointsırlaanmış
    uniname=[] #uniname sıralanmış
    capacity=[] # sıralanmış
    studentname=[] #sıralanmış
    studentnumber=[]
    score=[]
    choices1=[] # öğrenci tercihleri sıralandı max studenta göre
    
    for k in gh:
       uniname.append(c[k])
       unibasepoint.append(float(d_counter[k]))
       capacity.append(e[k])
       uninumber.append(b[k])
       
    acg.sort()#clone of points
    acg.reverse()
    for i in range(len(acg)):
        for y in range(len(acg)):
            if acg[i]==pointscounter[y]:
                indexs.append(y)
    for i in range(len(indexs)):
        if indexs[i] not in indexs[i+1:]:
            aym=indexs[i]
            news2.append(aym)
    for y in news2:
        studentname.append(students[y].getname()+" "+students[y].getlastname())
        score.append(points[y])
        choices1.append(students_choices[y])
        studentnumber.append(students[y].getid())
    #print(uninumber,uniname,unibasepoint)
    #print(unibasepoint)
    #print(capacity)
    #for i in range(len(studentname)):
    #print(studentname[i],score[i])
    #print(score)
    #print(choices1)
    
    option1=[]
    option2=[]
    option3=[]
    option4=[]
    option5=[]
    Mezunlar=[]
    
    for i in range(len(choices1)):
        a=choices1[i]
        b4=int(choices1[i][0])
        b5=b4-1
        c2=int(choices1[i][1])
        c1=c2-1
        d2=int(choices1[i][2])
        d1=d2-1
        e2=int(choices1[i][3])
        e1=e2-1
        f2=int(choices1[i][4])
        f1=f2-1
        if score[i] >= float(uni[b5].getbasepoint()) and e[b5]>0:
            at=uni[b5].getuniname()
            ak=str(studentnumber[i])+" " +str(studentname[i]+ " " +str(score[i]))
            e[b5]=e[b5]-1
            option1.append(at)
            option1.append(ak)
            
        elif score[i] >= float(uni[c1].getbasepoint()) and e[c1]>0:
            atk2=uni[c1].getuniname()
            atk3=str(studentnumber[i])+" " +str(studentname[i]+ " " +str(score[i]))
            e[c1]=e[c1]-1
            option2.append(atk2)
            option2.append(atk3)
       
            
        elif score[i] >= float(uni[d1].getbasepoint()) and e[d1]>0:
            atk4=uni[d1].getuniname()
            atk5=str(studentnumber[i])+" " +str(studentname[i]+ " " +str(score[i]))
            e[d1]=e[d1]-1
            option3.append(atk4)
            option3.append(atk5)

        elif score[i] >= float(uni[e1].getbasepoint()) and e[e1]>0:
            atk6=uni[e1].getuniname()
            atk7=str(studentnumber[i])+" " +str(studentname[i]+ " " +str(score[i]))
            e[e1]=e[e1]-1
            option4.append(atk6)
            option4.append(atk7)
        elif score[i] >= float(uni[f1].getbasepoint()) and e[f1]>0:
            atk8=uni[f1].getuniname()
            atk9=str(studentnumber[i])+" " +str(studentname[i]+ " " +str(score[i]))
            e[f1]=e[f1]-1
            option5.append(atk8)
            option5.append(atk9)
        else:
            Mezunlar.append(str(studentnumber[i])+" " +str(studentname[i]+ " " +str(score[i])))

    
    
    #print(c) #uniname
    
    option6 = option1 + option2 + option3 + option4 + option5
    ax=0
    
    while ax<len(uniname):
       op=0
       print(c[ax])
       print("-"*len(c[ax]),end="")
       print()
       for i in range(len(option6)):
            if c[ax] in option6[i]:
                op=op+1
                print(op,")",option6[i+1])
            
       print() 
       ax=ax+1
    
#yerleştirme()

def mezun():
    indexs=[]
    news2=[]
    q = open("university.txt", "r", encoding="utf-8")
    b = []#uninumber
    c = []#uniname
    d = []#basepoint
    e = []#capacity
    d_counter = []
    t = 0
    for i in q:
        a = i.split(",")
        h = a[0] #number of universtiy
        b.append(h) # list of number of university
        g = a[1] #name of uni
        c.append(g) #list of uni names
        j = a[2] # base point of uni
        d.append(j) # list of uni's base points
        d_counter.append(j) # same with d 
        u = int(a[3]) # quato of üni
        e.append(u) # list of uni's quatos



    d.sort() # sort of the uni base points
    d.reverse() #reverse
    
    
    gh=[] #indexlerin fazlalıgını siler
    indexler = [] #d nin d counterdaki yerini verir
    for i in range(len(d)):
        for index in range(len(d)):
            if d[i] == d_counter[index]: 
                indexler.append(index)
    for i in range(len(indexler)):
        if indexler[i] not in indexler[i+1:]: #eğer i elemanı geri kalan index listesinde yoksa yazar
            ab=indexler[i]
            gh.append(ab)

    uninumber=[]#uninumber sırlaanmış
    unibasepoint=[] #unibasepointsırlaanmış
    uniname=[] #uniname sıralanmış
    capacity=[] # sıralanmış
    studentname=[] #sıralanmış
    studentnumber=[]
    score=[]
    choices1=[] # öğrenci tercihleri sıralandı max studenta göre
    
    for k in gh:
       uniname.append(c[k])
       unibasepoint.append(float(d_counter[k]))
       capacity.append(e[k])
       uninumber.append(b[k])
       
    acg.sort()#clone of points
    acg.reverse()
    for i in range(len(acg)):
        for y in range(len(acg)):
            if acg[i]==pointscounter[y]:
                indexs.append(y)
    for i in range(len(indexs)):
        if indexs[i] not in indexs[i+1:]:
            aym=indexs[i]
            news2.append(aym)
    for y in news2:
        studentname.append(students[y].getname()+" "+students[y].getlastname())
        score.append(points[y])
        choices1.append(students_choices[y])
        studentnumber.append(students[y].getid())
    #print(uninumber,uniname,unibasepoint)
    #print(unibasepoint)
    #print(capacity)
    #for i in range(len(studentname)):
    #print(studentname[i],score[i])
    #print(score)
    #print(choices1)
    
    option1=[]
    option2=[]
    option3=[]
    option4=[]
    option5=[]
    Mezunlar=[]
    
    for i in range(len(choices1)):
        a=choices1[i]
        b4=int(choices1[i][0])
        b5=b4-1
        c2=int(choices1[i][1])
        c1=c2-1
        d2=int(choices1[i][2])
        d1=d2-1
        e2=int(choices1[i][3])
        e1=e2-1
        f2=int(choices1[i][4])
        f1=f2-1
        if score[i] >= float(uni[b5].getbasepoint()) and e[b5]>0:
            at=uni[b5].getuniname()
            ak=str(studentnumber[i])+" " +str(studentname[i]+ " " +str(score[i]))
            e[b5]=e[b5]-1
            option1.append(at)
            option1.append(ak)
            
        elif score[i] >= float(uni[c1].getbasepoint()) and e[c1]>0:
            atk2=uni[c1].getuniname()
            atk3=str(studentnumber[i])+" " +str(studentname[i]+ " " +str(score[i]))
            e[c1]=e[c1]-1
            option2.append(atk2)
            option2.append(atk3)
       
            
        elif score[i] >= float(uni[d1].getbasepoint()) and e[d1]>0:
            atk4=uni[d1].getuniname()
            atk5=str(studentnumber[i])+" " +str(studentname[i]+ " " +str(score[i]))
            e[d1]=e[d1]-1
            option3.append(atk4)
            option3.append(atk5)

        elif score[i] >= float(uni[e1].getbasepoint()) and e[e1]>0:
            atk6=uni[e1].getuniname()
            atk7=str(studentnumber[i])+" " +str(studentname[i]+ " " +str(score[i]))
            e[e1]=e[e1]-1
            option4.append(atk6)
            option4.append(atk7)
        elif score[i] >= float(uni[f1].getbasepoint()) and e[f1]>0:
            atk8=uni[f1].getuniname()
            atk9=str(studentnumber[i])+" " +str(studentname[i]+ " " +str(score[i]))
            e[f1]=e[f1]-1
            option5.append(atk8)
            option5.append(atk9)
        else:
            Mezunlar.append(str(studentnumber[i])+" " +str(studentname[i]+ " " +str(score[i])))

    
    
    #print(c) #uniname
    
    option6 = option1 + option2 + option3 + option4 + option5
    ax=0
    
    print("Mezuna Kalanlar")
    print("-"*len("Mezuna Kalanlar"))
    print()
    oi=0
    for i in Mezunlar:
        print(i)
        oi=oi+1
    print()
    print("Total = ",oi)
    print("-"*len("Mezuna Kalanlar"))

#mezun()



menu=True
while menu:
    for i in range(40):
        print("-",end=" ")
    print()
    print("(1)Search for a student with a given id and display his/her name and last name.")
    print("(2)List the university/universities and departments with a maximum base points.")
    print("(3)Create a file named results.txt for each student")
    print("(4)List the student information (id, name, last name) sorted by their score.")
    print("(5)List the students placed in every university/department")
    print("(6)List the students who were not be able to placed anywhere. ")
    print("(7)List all the departments.")
    for i in range(40):
        print("-",end=" ")
    print()

    choice=input("Please enter your choice 1-7:")
    choice=int(choice)
    if choice==1:
        xyz()
        print()
    if choice==2:
        unibase()
        print()
    if choice==3:
        result()
        print("saved result.txt")
        print()
    if choice==4:
        studentmax()
        print()
    if choice==5:
        yerleştirme()
    if choice==6:
        mezun()
    if choice==7:
        departmentsbonus()
        print()

    questionuser=input("Do you want to continue (y)es or (n)o:")
    if questionuser=="y":
        menu=True
    elif questionuser=="n":
        menu=False
    else:
        print("please enter y or n")
    
        
input()    









    
    
    



