from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import pymysql
import simplejson as json

# Create your views here.
def login(request):
    data=""
    con=pymysql.connect("localhost","root","","shoppingdb")
    c=con.cursor()
    if(request.POST):
       
        username=request.POST.get("username")
        password=request.POST.get("password")
       # d="select r_id from login_tab where username='"+str(username)+"' and password='"+str(password)+"'"
        c.execute("select r_id from login_tab where user_name='"+str(username)+"' and l_password='"+str(password)+"'")
        data=c.fetchone()
     
        c.execute("select role from role_tab where r_id='"+str(data[0])+"'")
        data1=c.fetchone()
        #request.session["sname"] =username
        if(str(data1[0])=="admin"):
            return HttpResponseRedirect("adminview")
        elif(str(data1[0])=="supplier"):
            return HttpResponseRedirect("supplierview") 
        elif(str(data1[0])=="consumer"):
            return HttpResponseRedirect("consumerview")   
    return render(request,"login.html",{"data":data})


def maincategoryview(request):
    con=pymysql.connect("localhost","root","","shoppingdb")
    c=con.cursor()
    if(request.POST):
     categoryName=request.POST.get("cname")

     c.execute("insert into maincategory_tab(cat_Name)values('"+categoryName+"')")
     con.commit()
    return render(request,"maincategory.html") 

def subcategoryview(request):
    data=""
    con=pymysql.connect("localhost","root","","shoppingdb")
    c=con.cursor()
    c.execute("select * from maincategory_tab")
    data=c.fetchall()
    if(request.POST):
     subcategoryName=request.POST.get("sname")
     maincategoryid=request.POST.get("maincategory")
     c.execute("insert into subcategory_tab(sub_Name,cat_id)values('"+subcategoryName+"','"+maincategoryid+"')")
     con.commit()

    return render(request,"subcategoryview.html",{"data":data})   



def adminview(request):
    data=""
    data1=""
    con=pymysql.connect("localhost","root","","shoppingdb")
    c=con.cursor()
    
    c.execute("select product_tab.p_id, product_tab.p_name, product_tab.description, product_tab.price,product_tab.is_active,subcategory_tab.sub_Name,supplier_tab.s_name from product_tab inner join subcategory_tab on product_tab.sub_id = subcategory_tab.sub_id INNER JOIN supplier_tab ON product_tab.s_id = supplier_tab.s_id where product_tab.is_active=1") 
    data=c.fetchall()

    c.execute("select product_tab.p_id, product_tab.p_name, product_tab.description, product_tab.price,product_tab.is_active,subcategory_tab.sub_Name,supplier_tab.s_name from product_tab inner join subcategory_tab on product_tab.sub_id = subcategory_tab.sub_id INNER JOIN supplier_tab ON product_tab.s_id = supplier_tab.s_id where product_tab.is_active=0") 
    data1=c.fetchall()
    
    return render(request,"adminview.html",{"data":data,"data1":data1}) 

def approve(request):
     con=pymysql.connect("localhost","root","","shoppingdb")
     c=con.cursor()
     id=request.GET.get("p_id")
     c.execute("UPDATE product_tab SET is_active = 1  WHERE p_id ='"+str(id)+"' ")
     con.commit()
     return HttpResponseRedirect("adminview")


def cart(request):
    data=""
    data1=""
    productid=request.GET.get("p_id")
    print(productid)
    con=pymysql.connect("localhost","root","","shoppingdb")
    c=con.cursor()
    c.execute("select * from product_tab  where p_id ='"+str(productid)+"'")
    data=c.fetchone()
    print(data)
    productname=data[1]
    description=data[2]
    price=data[5]
    
    c.execute("insert into cart_tab(productname,description,price)values('"+str(productname)+"','"+str(description)+"','"+str(price)+"')")
    con.commit()
    c.execute("select * from cart_tab")
    data1=c.fetchall()
    return render(request,"addcart.html",{"data":data,"data1":data1})

def customerview(request):
    data=""
    con=pymysql.connect("localhost","root","","shoppingdb")
    c=con.cursor()
    c.execute("select p.p_id,p.p_name,p.description,p.price,su.sub_name from product_tab p inner join subcategory_tab su on p.sub_id = su.sub_id where p.is_active=1")
    data=c.fetchall()
    return render(request,"customerview.html",{"data":data}) 

def subcatid(request):
    db=pymysql.connect("localhost","root","","shoppingdb")
    ob=db.cursor()
    catid=request.GET.get("dataid")   
    ob.execute("select sub_id,sub_name from subcategory_tab where cat_id='"+str(catid)+"'")
    data1=ob.fetchall()
    return HttpResponse(json.dumps(data1),content_type="application/json")
  
    
def supplierview(request):
   con = pymysql.connect("localhost","root","","shoppingdb")
   c=con.cursor()
   c.execute("select * from maincategory_tab")
   data=c.fetchall()
   print(data)
   if(request.POST):
       MaincategoryId=request.POST.get("catid")
       subcategoryId=request.POST.get("subcatid")
       productname=request.POST.get("Pname")
       price=request.POST.get("price")
       description=request.POST.get("desc")
       c.execute("insert into product_tab( p_name, description, sub_id, s_id, price, is_active)values('"+str(productname)+"','"+str(description)+"','"+str(subcategoryId)+"','"+str(1)+"','"+str(price)+"','"+str(0)+"')")
       con.commit()

   return render(request,"supplierview.html",{"data":data})
