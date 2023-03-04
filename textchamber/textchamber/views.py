#this file by (mk)





from django.http import  HttpResponse

from django.shortcuts import render


def index(request):
    params = {"game": 'mk'}

    return render(request , "index.html",params)
    # return HttpResponse("""<h1> HOME </h1><br><br><a href ='https://mangadex.org'> wow nerd manga </a>
    #                     <br><a href='https://mail.google.com/mail/u/1/#inbox'> mail dekh </a>
    #                     <br> <a href='http://127.0.0.1:8000/news'> news</a> 
    #                     <br> <a href='http://127.0.0.1:8000/about'> about</a>




def news(request):
    data = open("/Users/mayankolhan/PycharmProjects/textUtil/textchamber/textchamber/two.txt")
    content = data.read()
    return HttpResponse(content + """<br><a href=http://127.0.0.1:8000> home<=</a>""")



def analyze(request):
    text = request.POST.get("string", "default")
    remove_punc = request.POST.get("remove_punc" , "off")
    space_cnt = request.POST.get("space_cnt" , 'off')
    caps = request.POST.get("caps" , 'off')
    remove_nl = request.POST.get("remove_nl" , 'off')
    remove_sp = request.POST.get("remove_sp" , 'off')
    char_cnt = request.POST.get("char_cnt" , 'off')



    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    analyzed = ''
    num_spaces= 0
    cnt=0
    if (remove_punc == 'off'):
        analyzed = text
    if (remove_punc == "on"):
        for i in text:
            if i  not in punctuations:
                analyzed+=i
   


        params = {"purpose" : "remove punctuations" , "analyzed_text" : analyzed}

        text = analyzed
        #return render(request,"analyze.html", params)
    if(caps== 'on'):

        analyzed = ''

        for i in text:
            analyzed += i.upper()

        params = {"purpose": "capitalize", "analyzed_text": analyzed
                     }
        text=analyzed
       # return render(request, "analyze.html", params)

    if (remove_nl == 'on'):

        analyzed = ''

        for i in text:
            if(i != '\n' and i!="\r"):
                analyzed += i

        params = {"purpose": "removed new lines", "analyzed_text": analyzed,
                 }
        text = analyzed
        # return render(request, "analyze.html", params)
    if ( space_cnt == 'on'):



        for i in text:
            if(i == ' '):
                num_spaces+=1


        params = {"purpose": "removed new lines", "analyzed_text": analyzed,
                  'number_of_spaces': num_spaces
                 }
        text = analyzed
       # return render(request, "analyze.html", params)

    if ( remove_sp == 'on'):


        analyzed=''
        for index,char in enumerate(text):
            if( text[index] == ' ' and text[index+1] == ' '):
                pass
            else:
                analyzed+=char




        params = {"purpose": "removed extra spaces", "analyzed_text": analyzed,

                 }
        text = analyzed
        #return render(request, "analyze.html", params)

    if (char_cnt  == 'on'):



        for i in text:
            cnt+=1

        params = {"purpose": "counted characters", "analyzed_text": analyzed ,"character_count":cnt
                  }

       # return render(request, "analyze.html", params)

    params = {"purpose": "counted characters", "analyzed_text": analyzed,
              "number_of_spaces" : num_spaces

              }
    return render(request, "analyze.html",params)

def about(request):

    return render(request , "about.html")
def contact(request):

    return render(request , "contactus.html")

