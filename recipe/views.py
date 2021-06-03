from django.shortcuts import render,redirect
from recipe import recipeDao
from django.http import HttpResponse
# Create your views here.

def recipe_list(request):
    try:
          page=request.GET['page']
    except Exception as e:
          page="1"
    '''
       if(page==null) page="1"
    '''
    curpage=int(page)
    recipe_data=recipeDao.recipeListData(curpage)
    rd=[]
    for r in recipe_data:
        rr={"no":r[0],"title":r[1],"poster":r[2],"chef":r[3]}
        rd.append(rr)

    temp = request.COOKIES
    cookie_data=[]
    if temp:
        for c in temp:
            if c.startswith('k'):
                value = request.COOKIES.get(c)
                print(value)
                cd=recipeDao.recipe_info(int(value))
                cd2={"no":cd[0],"title":cd[1],"poster":cd[2]}
                cookie_data.append(cd2)

    return render(request,'recipe/recipe_list.html',{"rd":rd,"cd":cookie_data})

def recipe_before(request):
    # 쿠키 저장
    no=request.GET['no']
    response=redirect("/recipe/recipe_detail/?no="+str(no))
    response.set_cookie(f"k{no}",no,60*60*24)
    #  key , value , maxage
    return response

def recipe_detail(request):
    no=request.GET['no']
    #print(temp)
    '''
           if request.COOKIES.get(f"m{no}") is not None: #null (X) , None(O)
            value=request.COOKIES.get(f"m{no}")
            print(value)
    else:
           print("데이터가 없습니다")
    '''

    return render(request,'recipe/recipe_detail.html',{"no":no})






