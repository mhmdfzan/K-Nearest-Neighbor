import csv;
import numpy as np;
import statistics as stat
import math;
import random;

def validasi(a,b,c,d,e,f,g,h,i,j):
    return math.sqrt((a-f)**2+(b-g)**2+(c-h)**2+(d-i)**2+(e-j)**2);

def rumusK(i):
    return ((4*i)+1);

def TestUji(data1,data2,k):
    i=0;
    final = []
    while (i<200):
        uji = []
        j=0;
        while(j<800):
            total = validasi(data2[i][1],data2[i][2],data2[i][3],data2[i][4],data2[i][5],data1[j][1],data1[j][2],data1[j][3],data1[j][4],data1[j][5])
            hasil = {
                "no" : int(data1[j][0]),
                "score" : total
            }
            uji.append(hasil);
            j+=1;
        uji.sort(key=lambda x: x['score']);
        l=0; a=0; b=0; c=0; d=0; t=0;
        while True:
            if(l==k):
                break
            else:
                x = int(data1[uji[l]['no']-1][6])
                if(x==0):
                    a=a+1
                elif(x==1):
                    b=b+1
                elif(x==2):
                    c=c+1
                elif(x==3):
                    d = d+1
                l+=1       
        if(a>b and a>c and a>d):
            final.append(0)
            print(i,0);
        elif(b>a and b>c and b>d):
            final.append(1)
            print(i,1);
        elif(c>a and c>b and c>d):
            final.append(2)
            print(i,2);
        elif(d>a and d>b and d>c):
            final.append(3)
            print(i,3);
        else:
            final.append(random.randint(0,3))
        i+=1;
    w = np.asarray(final)
    w.tofile('TebakanTugas3.csv',sep='\n')
        
        
def cariNilaiK(data1,data2):
    KAkhir = 0;
    hasilAkhir=0;
    q=0;
    while (q<4):
        persen=0;
        x=0;
        y=199;
        z=0;
        k=rumusK(q);
        while (z<=3):
            i=x;
            v=0;
            while (i<=y):
                test = []
                j=0
                if (x==0):
                    j = j+200;
                while (j<800):
                    if (j==x and y==799):
                        break;
                    elif (j==x and y!=799):
                        j=j+200;
                        total = validasi(data1[i][1],data1[i][2],data1[i][3],data1[i][4],data1[i][5],data1[j][1],data1[j][2],data1[j][3],data1[j][4],data1[j][5])
                        hasil = {
                            "no" : int(data1[j][0]-1),
                            "score" : total
                        }
                        test.append(hasil);
                        j+=1;
                    else:
                        total = validasi(data1[i][1],data1[i][2],data1[i][3],data1[i][4],data1[i][5],data1[j][1],data1[j][2],data1[j][3],data1[j][4],data1[j][5])
                        hasil = {
                            "no" : int(data1[j][0]-1),
                            "score" : total   
                        }
                        test.append(hasil);
                        j+=1;
                        
                test.sort(key=lambda x: x['score']);
                l=0; a=0; b=0; c=0; d=0; t=0;
                while True:
                    if(l==k):
                        break
                    else:
                        w = int(data1[test[l]['no']][6])
                        if(w==0):
                            a=a+1
                        elif(w==1):
                            b=b+1
                        elif(w==2):
                            c=c+1
                        elif(w==3):
                            d=d+1
                        l+=1  
                if (a>b and a>c and a>d):
                    t=0;
                elif (b>a and b>c and b>d):
                    t=1;
                elif (c>a and c>b and c>d):
                    t=2
                elif (d>a and d>b and d>c):
                    t=3;

                if (int(data1[i][6]) == t):
                    v=v+1;
                i+=1;
            persen= persen + (v/200*100);
            z+=1;
            x=x+200;
            y=y+200;

        hasilK = (persen/4);
        if (hasilK>hasilAkhir):
            hasilAkhir=hasilK;
            KAkhir=k;
        print("K =",k,":",hasilK,"%") 
        q+=1;
    print("K yang terpilih adalah", KAkhir)
    return KAkhir, hasilAkhir        

def main():
    data1 = np.genfromtxt("DataTrain_Tugas3_AI.csv",delimiter=",",skip_header=True)
    data2 = np.genfromtxt("DataTest_Tugas3_AI.csv",delimiter=",",skip_header=True)

    K, hasilAkhir = cariNilaiK(data1,data2);
    TestUji(data1,data2,K);
    
   
main();
