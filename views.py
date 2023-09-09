from django.shortcuts import render
from django.shortcuts import redirect

from my_app.models import person
from my_app.models import cyber_attacks
from my_app.models import latest_news
from my_app.models import security_threats
from my_app.models import lawyer
from my_app.models import ngo
from my_app.models import policestation
from my_app.models import helpline
from my_app.models import laws
from my_app.models import help1
from my_app.models import review1
from my_app.models import contact1
from my_app.models import register1
from my_app.models import tips
from my_app.models import alerts
from my_app.models import crimes
from my_app.models import dgpsuraksha
from my_app.models import security_tips
from my_app.models import blog
from my_app.models import vulnerabilities1
from my_app.models import product
from my_app.models import productvuln
from django.conf import settings
from django.core.mail import send_mail
from django.utils.html import strip_tags

# Create your views here.
def contact(request):
    if request.method=='POST':
        if request.POST.get('n') and request.POST.get('ph'):
            post=contact1()
            post.name=request.POST.get('n')
            post.phone=request.POST.get('ph')
            post.email=request.POST.get('em')
            post.subject=request.POST.get('sub')
            post.message=request.POST.get('msg')
            post.save()
            x="Submitted Successfully"
            return render(request,'contact.html',{'x':x})
        else:
            y="Error...!! Not Submitted"
            return render(request,'contact.html',{'y':y})

    else:
        return render(request,"contact.html")

def aboutus(request):
    return render(request,"aboutus.html")

def FAQ(request):
    return render(request,"FAQ.html")

def footer(request):
    return render(request,"footer.html")

def forgetpassword(request):
    if(request.method=='POST'):
        em=request.POST.get('em')
        user=register1.objects.filter(email=em)
        if (len(user)>0):
            pw=user[0].password
            subject="Password"
            message="Welcome to SecuroPlex. Your Password is" +pw
            email_from=settings.EMAIL_HOST_USER
            recipient_list=[em,]
            #print(pw,subject,message,email_from,recipient_list)
            send_mail(subject,message,email_from,recipient_list )
            rest="Your Password sent to your respective Email Account. Please Check"
            return render(request,"forgetpassword.html",{'rest':rest})
        else:
            res="This email id is not registered"
            return render(request,"forgetpassword.html",{'res':res})
    else:
        return render(request,"forgetpassword.html")

def login(request):
    if request.method =='POST':
        formpost=True

        us=request.POST.get('us')
        pw=request.POST.get('pw')
        errormessage=""
        expert=register1.objects.filter(email = us, password = pw)
        print(us,pw)
        k=len(expert)
        if k>0:
            print("Valid Credentials")
            request.session['us']=us
            return render(request,'dashboard.html',{})
        else:
            print("Invalid Credentials")
            errormessage="invalid credentials"
            return render(request,'login.html',{'formpost':formpost})

    else:
        formpost=False
        return render(request,"login.html",{'formpost':formpost})

def register(request):
    if request.method=='POST':
        if request.POST.get('n') and request.POST.get('ph'):
            post=register1()
            post.name=request.POST.get('n')
            post.phone=request.POST.get('ph')
            post.email=request.POST.get('em')
            pwd=request.POST.get('pw')
            cpwd=request.POST.get('cpw')
            em=request.POST.get('em')

            if(pwd == cpwd):
                if register1.objects.filter(email=em).exists():
                    msg="Email Already Exists"
                    return render(request,'register.html',{'msg':msg})

                post.password=request.POST.get('pw')
                post.confirmpassword=request.POST.get('cpw')   
            else:
                z="Password doesn't match"
                return render(request,'register.html',{'z':z})
            post.save()
            x="Submitted Successfully"
            return render(request,'register.html',{'x':x})
        else:
            y="Error...!! Not Submitted"
            return render(request,'register.html',{'y':y})
    else:
        return render(request,"register.html")

def services(request):
    return render(request,"services.html")

def changepassword(request):
    if not request.session.has_key('us'):
        return redirect('/Login')
    if request.method=='POST':
        reg=register1.objects.get(email=request.session['us'])
        password=request.POST.get('opw')
        newpwd=request.POST.get('npw')
        confirmpwd=request.POST.get('cpw')
        if(newpwd==confirmpwd):
            p=reg.password

            if(password==p):
                reg.password=newpwd
                reg.confirmpassword=confirmpwd
                reg.save()
                rest="Password Changed"
                return render(request,'changepassword.html',{'rest':rest})
            else:
                res="Invalid Current Password"
                return render(request,"changepassword.html",{'res':res})

        else:
            res="Confirm Password and New Password Do Not Match"
            return render(request,"changepassword.html",{'res':res})
    else:
        return render(request,"changepassword.html")
    
def Help(request):
    if not request.session.has_key('us'):
        return redirect('/Login')
    if request.method=='POST':
        if request.POST.get('t') and request.POST.get('msg'):
            post=help1()
            post.title=request.POST.get('t')
            post.message=request.POST.get('msg')
            post.save()
            x="Submitted Successfully"
            return render(request,'help.html',{'x':x})
        else:
            y="Error...!! Not Submitted"
            return render(request,'help.html',{'y':y})

    else:
        return render(request,'help.html')

def review(request):
    if not request.session.has_key('us'):
        return redirect('/Login')
    if request.method=='POST':
        if request.POST.get('t') and request.POST.get('msg'):
            post=review1()
            post.title=request.POST.get('t')
            post.message=request.POST.get('msg')
            post.save()
            x="Submitted Successfully"
            return render(request,'review.html',{'x':x})
        else:
            y="Error...!! Not Submitted"
            return render(request,'review.html',{'y':y})

    else:
        return render(request,'review.html')
    

def main(request):
    return render(request,"main.html")

def index(request):
    return render(request,"index.html")

def base(request):
    return render(request,"base.html")

def dashboard(request):
    return render(request,"dashboard.html")


def allattacks(request):
    x=cyber_attacks.objects.all()
    return render(request,"allattacks.html",{'data':x})

def allnews(request):
    a=latest_news.objects.all()
    t=tips.objects.all()
    return render(request,"allnews.html",{'data':a,'data1':t})

def allthreats(request):
    t=security_threats.objects.all()
    return render(request,"allthreats.html",{'data':t})

def alllawyers(request):
    l=lawyer.objects.all()
    return render(request,"alllawyers.html",{'data':l})

def allngos(request):
    n=ngo.objects.all()
    return render(request,"allngos.html",{'data':n})

def allpolicestations(request):
    p=policestation.objects.all()
    return render(request,"allpolicestations.html",{'data':p})

def allhelplines(request):
    h=helpline.objects.all()
    news=latest_news.objects.all()
    return render(request,"allhelplines.html",{'data':h,'data1':news})

def allacts(request):
    l=laws.objects.all()
    return render(request,"allacts.html",{'data':l})

def detaillawyer(request,id):
    dl=lawyer.objects.get(id=id)
    return render(request,"detaillawyer.html",{'i':dl})

def detailattack(request,id):
    da=cyber_attacks.objects.get(id=id)
    return render(request,"detailattack.html",{'i':da})

def detailnews(request,id):
    dn=latest_news.objects.get(id=id)
    return render(request,"detailnews.html",{'i':dn})

def detailthreat(request,id):
    dt=security_threats.objects.get(id=id)
    return render(request,"detailthreat.html",{'i':dt})

def alltips(request):
    t=tips.objects.all()
    return render(request,"alltips.html",{'data':t})
   
def allcrimes(request):
    c=crimes.objects.all()
    return render(request,"allcrimes.html",{'data':c})

def profile(request):
    if not request.session.has_key('us'):
        return redirect('/Login')
    userdetail=register1.objects.get(email=request.session['us'])
    return render(request,"profile.html",{'user':userdetail})

def logout(request):
    if not request.session.has_key('us'):
        return redirect('/Login')
    del request.session['us']
    return redirect('/Login')

def allalerts(request):
    a=alerts.objects.all()
    return render(request,"allalerts.html",{'data':a})

def fullscan(request):
    if request.method=='POST':
        target=request.POST.get('url')
        
        print(target)
        
        # importing the scokets module
        import socket

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # getting the ip address using gethostbyname
        # function
        t_IP = socket.gethostbyname(target)
        print("Starting scan on host: ", t_IP)
        
        result=[]
       
        for i in range(1,65535):
            l=[]
            try:
                s.connect((t_IP, i))
                l.append(i,'port open')
                
                
            except:
                l.append([i,'port Closed'])
               
            result.append(l)
    
        return render(request,'fullscanresult.html',{'result':result})
    else:
        return render(request,'fullscan.html')

def quickscan(request):
    if request.method=='POST':
        target=request.POST.get('url')
        
        print(target)
        
        # importing the scokets module
        import socket

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # getting the ip address using gethostbyname
        # function
        t_IP = socket.gethostbyname(target)
        print("Starting scan on host: ", t_IP)
        port=[20,21,23,25,53,443,110,135,137,138,139,1433,1434]
        result=[]
        for i in port:
            l=[]
            try:
                s.connect((t_IP, i))
                l.append(i,'port open')
                
                
            except:
                l.append([i,'port Closed'])
               
            result.append(l)

        return render(request,'quickscanresult.html',{'result':result})
    else:
        return render(request,"quickscan.html")

def rangescan(request):
    if request.method=='POST':
        target=request.POST.get('url')
        fport=int(request.POST.get('from'))
        tport=int(request.POST.get('to'))
        print(target)
        print(fport)
        print(tport)
        import sys
        import socket
        from datetime import datetime
        msg=""
        result1=[]
        try:

            #will scan ports between (1 to 65,535)
            for port in range(fport,tport):
                l=[]
                s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result=s.connect_ex((target,port))
                if(result==0):
                    l.append([port,'port Open'])
                    msg="Port {} is open".format(port)
                else:
                    l.append([port,'port Closed'])
                    msg="Port {} is close".format(port)  
                result1.append(l)
            s.close()

        except KeyboardInterrupt:
            msg="Exiting Program !!!!"
            sys.exit()

        except socket.gaierror:
            msg="Host name could not be resolved !!!!"
            sys.exit()
        except socket.error:
            msg="Server not responding !!!!"
            sys.exit()
        return render(request,"rangescanresult.html",{'result1':result1})
    else:
        return render(request,"rangescan.html")

def phishingdetection(request):
    import os
    import pandas as pd
    import numpy as np

    import keras
    from keras.preprocessing.sequence import pad_sequences
    from keras.models import load_model

    from models.phishing import simple_bilstm

    PHISHING_DATA_DIR_PATH = "./data/phishing_url"
    PHISHING_CACHE_DIR_PATH = "./cache/phishing_url"

    model_file_path = os.path.join(PHISHING_CACHE_DIR_PATH, "simple_bilstm.h5")
    def read_data():
        blacklist = os.path.join(PHISHING_DATA_DIR_PATH, 'phishing_database.csv')
        whitelist = os.path.join(PHISHING_DATA_DIR_PATH, 'whitelist.txt')

        urls = {}

        blacklist = pd.read_csv(blacklist)

    # Assign 0 for non-malicious and 1 as malicious for supervised learning.
        for url in blacklist['url']:
            urls[url] = 1

        with open(whitelist, 'r') as f:
            lines = f.read().splitlines()
            for url in lines:
                urls[url] = 0

        return urls

    urls = read_data()
    samples = []
    labels = []
    for k, v in urls.items():
        samples.append(k)
        labels.append(v)
    #print(k, v)

    print("label == 1: ", labels.count(1))
    print("label == 0: ", labels.count(0))

    max_chars, maxlen, num_chars, embedding_vector_length, sequences = simple_bilstm.build_tokenizer(
        samples)

    data = pad_sequences(sequences, maxlen=maxlen)

    labels = np.asarray(labels)
    print('Shape of data tensor:', data.shape)
    print('Shape of label tensor:', labels.shape)
    # Divide data between training, cross-validation, and test data.
    training_samples = int(len(samples) * 0.95)
    validation_samples = int(len(labels) * 0.05)
    print("training_samples: ", training_samples)
    print("validation_samples: ", validation_samples)

    indices = np.arange(data.shape[0])
    np.random.shuffle(indices)
    data = data[indices]
    labels = labels[indices]

'''
x = data
y = labels
'''
    x = data[:training_samples]
    y = labels[:training_samples]
    x_test = data[training_samples: training_samples + validation_samples]
    y_test = labels[training_samples: training_samples + validation_samples]
    callbacks_list = [
    keras.callbacks.ModelCheckpoint(
        filepath=model_file_path,
        monitor='val_loss',
        save_best_only=True
    ),
    keras.callbacks.EarlyStopping(
        monitor='val_loss',
        min_delta=0,
        patience=2,
        mode='auto',
        baseline=None,
    )
]

    model = simple_bilstm.build_model(
        num_chars, embedding_vector_length, maxlen)

# Train.
    model.fit(x, y,
            epochs=10,
            batch_size=32,
            callbacks=callbacks_list,
            validation_split=0.20,
            shuffle=True
            )

    # Evaluate model on test data.
    model = load_model(model_file_path)
    score, acc = model.evaluate(x_test, y_test, verbose=1, batch_size=1024)

    print("Model Accuracy: {:0.2f}%".format(acc * 100))
    from sklearn.metrics import classification_report
    pred = model.predict_classes(x_test)
    print(classification_report(y_test, pred, digits=5))
        except KeyboardInterrupt:
            msg="Exiting Program !!!!"
            print("\n Exiting Program !!!!")
            sys.exit()

        except socket.gaierror:
            msg="Host name could not be resolved !!!!"
            sys.exit()
        except socket.error:
            msg="Server not responding !!!!"
            sys.exit()
        #return render(request,"portscanresult.html",{'msg':msg, 'rest':rest})
        return render(request,"phishingresult.html",{'target': target, 'msg':msg, 'rest':rest})
        else:
            return render(request,"phishingdetection.html")



def portscan(request):
      if request.method=='POST':
        target=request.POST.get('url')
        port=int(request.POST.get('portno'))
        print(target)
        print(port)
        import sys
        import socket
        from datetime import datetime
        msg="" 
        try:
    
        #will scan ports between (1 to 65,535)

            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result=s.connect_ex((target,port))
            if(result==0):
                msg="Port {} is open".format(port)
            
            else:
                msg="Port {} is close".format(port)
        
            s.close()
            if(request.method=='POST'):
                userdetail=register1.objects.get(email=request.session['us'])
                em=userdetail.email
                subject="Port Scan Result"
                message="Welcome to SecuroPlex. Your Scanning Result is: " + msg
                email_from=settings.EMAIL_HOST_USER
                recipient_list=[em,]
                #print(pw,subject,message,email_from,recipient_list)
                send_mail(subject,message,email_from,recipient_list )
                rest="Your Scanning Result sent to your respective Email Account. Please Check"
                
                #return render(request,"portscanresult.html",{'rest':rest})
            #else:
            #res="This email id is not registered"
            #return render(request,"forgetpassword.html",{'res':res})
   # else:
        #return render(request,"forgetpassword.html")

        except KeyboardInterrupt:
            msg="Exiting Program !!!!"
            print("\n Exiting Program !!!!")
            sys.exit()

        except socket.gaierror:
            msg="Host name could not be resolved !!!!"
            sys.exit()
        except socket.error:
            msg="Server not responding !!!!"
            sys.exit()
        #return render(request,"portscanresult.html",{'msg':msg, 'rest':rest})
        return render(request,"portscanresult.html",{'target': target, 'port': port,'msg':msg, 'rest':rest})
      else:
            return render(request,"portscan.html")


def editprofile(request):
    if not request.session.has_key('us'):
        return redirect('/Login')
    userdetail=register1.objects.get(email=request.session['us'])
    if request.method == 'POST':
        detail = register1.objects.get(email=request.session['us'])
        detail.name= request.POST.get('name')
        
        detail.phone= request.POST.get('phone')
        detail.city= request.POST.get('city')
        detail.state= request.POST.get('state')
        detail.dob=request.POST.get('dob')
        detail.gender=request.POST.get('gender')

        detail.save()
        data=register1.objects.get(email=request.session['us'])
        #return render(request,'profile.html',{'us':data})
        return redirect('/Profile',{'us':data})

    else:
        return render(request,"editprofile.html",{'us':userdetail})

def filescan(request):
    if request.method=='POST':
        print("posted")
        f = request.FILES['sentFile'] # here you get the files needed
        handle_uploaded_file(f,f.name)
        import os
        import time
        import json
        import virustotal3.core

        #API_KEY = os.environ['d6e8ddc0f68b12f65e414433c94e36bf26892c600e68727f13dbf68947242ad1']
        API_KEY='d6e8ddc0f68b12f65e414433c94e36bf26892c600e68727f13dbf68947242ad1'
        vt = virustotal3.core.Files('d6e8ddc0f68b12f65e414433c94e36bf26892c600e68727f13dbf68947242ad1')

        response = vt.upload(f.name)
        analysis_id = response['data']['id']
        print('Analysis ID: {}'.format(analysis_id))
        results = virustotal3.core.get_analysis(API_KEY, analysis_id)
        status = results['data']['attributes']['status']

        print('Waiting for results...')
        while 'completed' not in status:
            results = virustotal3.core.get_analysis(API_KEY, analysis_id)
            status = results['data']['attributes']['status']
            print('Current status: {}'.format(status))
            time.sleep(10)

        results = virustotal3.core.get_analysis(API_KEY, analysis_id)
        res=json.dumps(results, indent=4, sort_keys=True)
        print(json.dumps(results, indent=4, sort_keys=True))
        res=json.dumps(results, indent=4, sort_keys=True)
        print(json.dumps(results, indent=4, sort_keys=True))
        print(results['data']['attributes']['results'])
        k=results['data']['attributes']['results']
        import pandas as pd
        l=[]
        for x in k:
                print(x,k[x]['category'])
                l.append([x,k[x]['category']])
        return render(request, 'filescanresult.html',{'res':l})
    else:
        print("hekko")
        return render(request, 'filescan.html',{})

def handle_uploaded_file(f,name):
    destination = open(name, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()

def filescanresult(request):
    return render(request,"filescanresult.html")

def alldgpsuraksha(request):
    dg=dgpsuraksha.objects.all()
    return render(request,"alldgpsuraksha.html",{'data':dg})

def allsecurity_tips(request):
    st=security_tips.objects.all()
    return render(request,"allsecurity_tips.html",{'data':st})

def security_tools(request):
    return render(request,"security_tools.html")

def vulnerability(request):
    if request.method=='POST': 
        keyword = request.POST.get('keyword')
        print(keyword.capitalize())
        #ilter(hostname__contains='.amgr.')
        keyword=keyword.capitalize()
        from my_app.models import product
        
        p = product.objects.filter(name=keyword)
        print(p[0])
        
        if(len(p)>0):
             pv=productvuln.objects.filter(name=p[0])
             print(pv)
             return render(request,"vulnerabilitysearch.html",{'pv':pv,'keyword':keyword})
        else:
            msg="This product doesnot exist try a new one!"
            return render(request,"vulnerability.html",{'msg':msg})
        
        
    else:
        msg=''
        return render(request,"vulnerability.html",{'msg':msg})

def detailalert(request,id):
    da=alerts.objects.get(id=id)
    return render(request,"detailalert.html",{'i':da})

def detailcrimes(request,id):
    dc=crimes.objects.get(id=id)
    return render(request,"detailcrimes.html",{'i':dc})

def newsletter(request):
    
    if request.method=='POST':
        typ=request.POST.get('type')
        print(typ)
        if request.POST.get('email'): 
            post=newsletter()
            post.email=request.POST.get('email')
            post.save()
            x="Submitted Successfully"
            return render(request,'index.html',{'x':x})
        else:
            y="Error...!! Not Submitted"
            return render(request,'index.html',{'y':y})

    else:
        return render(request,'index.html')

def allblogs(request):
    b=blog.objects.all()
    return render(request,"allblogs.html",{'data':b})

def detailblog(request,id):
    db=blog.objects.get(id=id)
    return render(request,"detailblog.html",{'i':db})

def vulnerabilitysearch(request):
    v=productvuln.objects.all()
    return render(request,"vulnerabilitysearch.html",{'data':v})

def detailvulnerability(request,id):
    print("id",id)
    dv=vulnerabilities1.objects.get(vid=id)
    return render(request,"detailvulnerability.html",{'i':dv})

def portscanresult(request):
    return render(request,"portscanresult.html")

def phishingresult(request):
    return render(request,"phishingresult.html")

def quickscanresult(request):
    return render(request,"quickscanresult.html")

def rangescanresult(request):
    return render(request,"rangescanresult.html")

def fullscanresult(request):
    return render(request,"fullscanresult.html")

def whoisscanning(request):
    if request.method=='POST':
        #from Whois import whois
        target=request.POST.get('url')
        print(target)
        import whois
        w = whois.whois(target)
        reg=w["registrar"]
        print('reg',reg)
        org=w["organization"]
        print('org',org)
        reg_url=w["registrar_url"]
        print('reg_url',reg_url)
        reg_iana=w["registrar_iana"]
        print('reg_iana',reg_iana)
        update=w["updated_date"]
        print('update',update)
        creation=w["creation_date"]
        print('creation',creation)
        exp_date=w["expiration_date"]
        print('exp_date',exp_date)
        server=w["name_servers"] 
        print('server',server)
        state=w["state"]
        print('state',state)
        email=w["emails"]
        print('email',email)
        status=w["status"]
        print('status',status)
        country=w["country"]
        print('country',country)
        dnssec=w["dnssec"]
        print('dnssec',dnssec)
        return render(request,'whoisscanningresult.html',{'reg':reg,'org':org,'reg_url':reg_url,'reg_iana':reg_iana,'update':update,'creation':creation,'exp_date':exp_date,'server':server,'state':state,'status':status,'email':email,'country':country,'dnssec':dnssec})
    else:
        return render(request,'whoisscanning.html')  

def whoisscanningresult(request):
    return render(request,"whoisscanningresult.html")

def domainscan(request):
    if request.method =='POST':
        import requests
        website=request.POST.get('website')
        website="hdfc.com"
        url = 'https://www.virustotal.com/vtapi/v2/url/scan'
        params = {'apikey': 'd6e8ddc0f68b12f65e414433c94e36bf26892c600e68727f13dbf68947242ad1', 'url':website}
        response = requests.post(url, data=params)
        #print(response.json())
        import pandas as pd
        #print(response.json())
        s=response.json()
        #print(s.get("scan_id"))
        k=s.get("scan_id")
        import requests
        url = 'https://www.virustotal.com/vtapi/v2/url/report'
        params = {'apikey': 'd6e8ddc0f68b12f65e414433c94e36bf26892c600e68727f13dbf68947242ad1', 'resource':k}
        response = requests.get(url, params=params)
        import pandas as pd
        #print(response.json())
        r=response.json()
        df = pd.DataFrame(response.json())
        df = df.reset_index()
        k1=['Sophos','StopBadware','Lumu','Netcraft','NotMining','AutoShun','Cyan']
        df.columns
        df.rename(columns = {'index':'antivirus'}, inplace = True) 
        df =df[(df.antivirus !='Sophos') & (df.antivirus !='Netcraft') & (df.antivirus !='StopBadware') & (df.antivirus !='Lumu') & (df.antivirus !='NotMining') & (df.antivirus !='AutoShun') & (df.antivirus !='Cyan')   ]
        l=[]
        for j,i in zip(df.iloc[:,11],df.iloc[:,0]):
            k=[]
            for x in j :
                print(j[x])
                k.append(j[x])
            k.append(i)
            l.append(k)
        return render(request,"domainresult.html",{'l':l})
    else:
         return render(request,'domainscan.html',{})

def domainresult(request):
    return render(request,"domainresult.html")
