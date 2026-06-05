h={"name":"jai" , 23:44}
print(h)

#nested dictionary

u={23:44,
   "ratings":{8:10 , "jjk":"aot"},
  "subjetcs": {"chem":34 , "phy":67 , "maths":90}}

print(u)
print(u["subjetcs"]["chem"])

#methods

print(h.keys())
print(u.keys())

print(len(u))

u.update({"coutry":"india"})
print(u)