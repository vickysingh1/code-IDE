from django.shortcuts import render
from django.http import JsonResponse
import subprocess
import os
from time import sleep
from django.http.response import HttpResponse
import json
import time
import random

# from django.views.decorators.csrf import csrf_exempt
def index(request):
    return render(request,'../templates/firstpage.html')
def details(request):
    j=0
    #print(request.POST)
    text=request.POST.get('l2')
    text1=request.POST.get('l3')
    #print(text)
    inputtext=request.POST.get('l4')
    #print(inputtext)
    file_=open('log.txt','w+')
    # print(text,text1)
    if text1=='Language' or len(text)==0:
        res = {'result':'No output'}
        return JsonResponse(res)

    elif text1=='C':
        j=random.randint(6000000,8000000)
        l=random.randint(6000000,8000000)
        jj=str(j)
        ll=str(l)
        try:
            fh2=open('input_file'+ll,'w+')
            fh2.write(inputtext)
            fh2.close()
            fh=open('C1.c','w+')
            fh.write(text)
            fh.close()
            try:
                subprocess.run('make C1 > output1'+jj+'.txt 2>&1',shell=True,stdout=file_,timeout=2)
                subprocess.run('cat input_file'+ll+' | ./C1 > output'+jj+'.txt 2>&1',shell=True,stdout=file_,timeout=2)
            except:
                res={"result":"warning: timelimit exceeded (wall time): aborting command"}
                os.remove('/home/msi/Desktop/Djangoproject/codingplatform/output1'+jj+'.txt')
                os.remove('/home/msi/Desktop/Djangoproject/codingplatform/output'+jj+'.txt')
                os.remove('/home/msi/Desktop/Djangoproject/codingplatform/input_file'+ll)
                return JsonResponse(res)
            file_.close()
            fh=open('output1'+jj+'.txt','r+')
            k1=fh.read()
            fh.close()
            fh1=open('output'+jj+'.txt','r+')
            k=fh1.read()
            fh1.close()
            os.remove('/home/msi/Desktop/Djangoproject/codingplatform/output1'+jj+'.txt')
            os.remove('/home/msi/Desktop/Djangoproject/codingplatform/output'+jj+'.txt')
            os.remove('/home/msi/Desktop/Djangoproject/codingplatform/input_file'+ll)
            if len(k1)>20:
                res = {'result':k1[20:]}
            else:
                res = {'result':k}
            return JsonResponse(res)
        except:
            res={'result':"No Output"}
            return JsonResponse(res)
            
            
    elif text1=='CPP':
        j=random.randint(4000000,6000000)
        l=random.randint(4000000,6000000)
        jj=str(j)
        ll=str(l)
        try:
            fh2=open('input_file'+ll,'w+')
            fh2.write(inputtext)
            fh2.close()
            fh=open('Cpp1.cpp','w+')
            fh.write(text)
            fh.close()
            try:
                subprocess.run('make Cpp1 > output1'+jj+'.txt 2>&1',shell=True,stdout=file_,timeout=2)
                subprocess.run('cat input_file'+ll+' | ./Cpp1 > output'+jj+'.txt 2>&1',shell=True,stdout=file_,timeout=2)
            except:
                res={"result":"warning: timelimit exceeded (wall time): aborting command"}
                # os.remove('/home/msi/Desktop/Djangoproject/codingplatform/output1'+jj+'.txt')
                # os.remove('/home/msi/Desktop/Djangoproject/codingplatform/output'+jj+'.txt')
                # os.remove('/home/msi/Desktop/Djangoproject/codingplatform/input_file'+ll)
                return JsonResponse(res)
            file_.close()
            fh=open('output1'+jj+'.txt','r+')
            k1=fh.read()
            fh.close()
            fh1=open('output'+jj+'.txt','r+')
            k=fh1.read()
            fh1.close()
            os.remove('/home/msi/Desktop/Djangoproject/codingplatform/output1'+jj+'.txt')
            os.remove('/home/msi/Desktop/Djangoproject/codingplatform/output'+jj+'.txt')
            os.remove('/home/msi/Desktop/Djangoproject/codingplatform/input_file'+ll)
            # print(len(k1))
            if len(k1)>28:
                res = {'result':k1[27:]}
            else:
                res = {'result':k}
            return JsonResponse(res)
        except:
            res={'result':"No Output"}
            return JsonResponse(res)
    elif text1=='Java':
        j=random.randint(1000000,3000000)
        l=random.randint(1000000,3000000)
        jj=str(j)
        ll=str(l)
        try:
            fh2=open('input_file'+ll,'w+')
            fh2.write(inputtext)
            fh2.close()
            fh=open('Java1.java','w+')
            fh.write(text)
            fh.close()
            try:
                subprocess.run('javac Java1.java > output1'+jj+'.txt 2>&1',shell=True,stdout=file_,timeout=2)
                subprocess.run('cat input_file'+ll+' | java Java1 > output'+jj+'.txt 2>&1',shell=True,stdout=file_,timeout=2)
            except:
                res={"result":"warning: timelimit exceeded (wall time): aborting command"}
                # os.remove('/home/msi/Desktop/Djangoproject/codingplatform/output1'+jj+'.txt')
                # os.remove('/home/msi/Desktop/Djangoproject/codingplatform/output'+jj+'.txt')
                # os.remove('/home/msi/Desktop/Djangoproject/codingplatform/input_file'+ll)
                return JsonResponse(res)
            file_.close()
            fh=open('output1'+jj+'.txt','r+')
            k1=fh.read()
            print(k1)
            # fh.truncate(0)
            fh.close()
            fh=open('output'+jj+'.txt','r+')
            k=fh.read()
            print(k)
            # fh.truncate(0)
            fh.close()
            try:
                os.remove('/home/msi/Desktop/Djangoproject/codingplatform/output1'+jj+'.txt')
                os.remove('/home/msi/Desktop/Djangoproject/codingplatform/output'+jj+'.txt')
                os.remove('/home/msi/Desktop/Djangoproject/codingplatform/input_file'+ll)
                # print(len(k1))
                if len(k1)!=0 :
                    res={'result':k1}
                else:
                    res = {'result':k}
            
                return JsonResponse(res)
            except Exception as e:
                print(e)
                res={'result':"No Output"}
                return JsonResponse(res)


        except:
            # os.remove('/home/msi/Desktop/Djangoproject/codingplatform/output'+jj+'.txt')
            # os.remove('/home/msi/Desktop/Djangoproject/codingplatform/input_file'+ll)
            res={'result':'No Output'}
            return JsonResponse(res)


    elif text1=="Python":
        j=random.randint(0,1000000)
        l=random.randint(0,1000000)
        jj=str(j)
        ll=str(l)
        try:

            fh2=open('input_file'+ll,'w+')
            fh2.write(inputtext)
            fh2.close()
            fh=open('p1.py','w+')
            fh.write(text)
            fh.close()
            command = 'cat input_file'+ll+' | python3 p1.py > output'+jj+'.txt 2>&1'
            try:
                subprocess.run(command,stdout=subprocess.PIPE,shell=True,timeout=2)
            except:
                res = {'result':'warning: timelimit exceeded (wall time): aborting command'}
                os.remove('/home/msi/Desktop/Djangoproject/codingplatform/output'+jj+'.txt')
                os.remove('/home/msi/Desktop/Djangoproject/codingplatform/input_file'+ll)
                return HttpResponse(json.dumps(res), content_type="application/json")
            file_.close()
            # time.sleep(4)
            fh=open('output'+jj+'.txt','r+')
            k=fh.read()
            fh.close()
            os.remove('/home/msi/Desktop/Djangoproject/codingplatform/output'+jj+'.txt')
            os.remove('/home/msi/Desktop/Djangoproject/codingplatform/input_file'+ll)

            res = {'result':k}
            return HttpResponse(json.dumps(res), content_type="application/json")
        except:
            res={'result':"No Output"}
            os.remove('/home/msi/Desktop/Djangoproject/codingplatform/output'+jj+'.txt')
            os.remove('/home/msi/Desktop/Djangoproject/codingplatform/input_file'+ll)
            return HttpResponse(json.dumps(res), content_type="application/json")
        
        

def mylang(request):
    lang=request.POST.get('l3')
    print(lang,end="\n")
    if lang=='Java':
        lang1='// Always Use Java1 as a Main Class \npublic class Java1{\n public static void main(String[] args){\n \tSystem.out.println("Code Funk in Java");\n}\n}'
        res={'lang':lang1,'prog':lang}
        return JsonResponse(res)
    elif lang=='Python':
        lang1='print("Code Funk in python")'
        res={'lang':lang1,'prog':lang}
        return JsonResponse(res)
    elif lang=='C':
        lang1='#include<stdio.h> \n int main(){ \n \t printf("Code Funk in C"); \n }'
        res={'lang':lang1,'prog':lang}
        return JsonResponse(res)
    elif lang=='CPP':
        lang1='#include<iostream> \n using namespace std; \n int main(){ \n \t cout<<"Code Funk in Cpp"; \n }'
        res={'lang':lang1,'prog':lang}
        return JsonResponse(res)
    elif lang=='Language':
        lang1=""
        res={'lang':lang1,'prog':lang}
        return JsonResponse(res)
    
    
        

