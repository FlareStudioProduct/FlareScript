import sys
import os
ns=[]
nss=[]
impo=["network","main","windows","createfiles"]
impoboollists=["False","False","False","False"]
b="NODOT"
def introduce(nq):
    nss=nq.split("<")
    if nss[0]=="printf":
        nsss=nss[1].split(">")
        print(nsss[0])
    imp=nq.split(" ")
    if imp[0]=="#import":
        readimport=imp[1]
        for i in range(len(impo)):
            if readimport==impo[i]:
                impoboollists[i]="True"
while True:
    while True:
        n=input(">>>")
        if impoboollists[1]=="True":
            if n=="done()" or n=="done":
                break
            elif n=="exit()" or n=="exit":
                sys.exit(0)
            elif n=="save()" or n=="save":
                if impoboollists[3]=="True":
                    filename=input("name:")
                    if not filename.endswith(".flare"):
                        filename+=".flare"
                    with open(filename,"w",encoding="utf-8") as f:
                        f.write("\n".join(ns))
                    print(f"Already save it in {filename}")
            else:
                ns.append(n)
    for i in range(len(ns)):
        introduce(ns[i])

