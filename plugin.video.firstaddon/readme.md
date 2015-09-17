OK LETS READ A PAGE

So you get used to it we will start small, so pick your page you want to read. im going to pick the kodi fourms.

http://forum.kodi.tv/forumdisplay.php?fid=26 

Once on the page right click and view source now this may look hard but this is the code of the website HTML normaly.
click ctrl F and type in the text you are trying to find mine is your first add-on it should now hight light the txt
now the left and right there will be code you want to select the whole line now copy it 

<a href="showthread.php?tid=209948" class=" subject_new" id="tid_209948">Your First Add-On: Hello World!</a></strong> 

now regex has special code to indicate that this is the text you want and to ignore the rest the code is 

EXAMPLES OF REGEX CODE

Read This  --->   (.+?)
Ignore This --->  .+?
read this numbers ---> (\d\d) the \d stands for number so for each \d is one number so (\d\d) would read 2 numbers
a new line ----> \n
before this ---> \b

so look at the code you have copyed

<a href="showthread.php?tid=209948" class=" subject_new" id="tid_209948">Your First Add-On: Hello World!</a></strong>

Now you need to grab the txt that will change but still match what you are trying to grab so

<a href="showthread.php?tid=209948" class=" subject_new" id="tid_209948">Your First Add-On: Hello World!</a></strong>
                            ^^^^^^                  ^^^          ^^^^^^  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  where you see ^ is text that will change on each post so we will start with the name of the post 
  
  "Your First Add-On Hello World"
  
  now like in the regex examples we want to read this so what we do is remove the text "Your First Add-On Hello World"
  and put (.+?) the tell regex that we want this code now you code should look like
  
  <a href="showthread.php?tid=209948" class=" subject_new" id="tid_209948">(.+?)</a></strong>
  
  now the code will fetch the name but as you will see this will only fetch one item becouse 
  
  showthread.php?tid=209948      tid_209948       subject_new
  
  these 3 items can change on each post so to do this i want to add
  
  .+?
  
  this tell regex to ignore this text so lets change it 
    
  FROM  <a href="showthread.php?tid=209948" class=" subject_new" id="tid_209948">(.+?)</a></strong>
  TO    <a href="showthread.php?tid=.+?" class=".+?" id="tid_.+?">(.+?)</a></strong>
  
  Now the reason why i have kept the text showthread.php?tid= is becouse i dont want it to read every link just the posts
  Now you see where it says PUT REGEX CODE you want to copy
  
  <a href="showthread.php?tid=.+?" class=".+?" id="tid_.+?">(.+?)</a></strong>
  
  and paste it in there now we need to tell kodi that we have one item and that we want it to be the name so to do this
  look bellow see where it says GIVE IT A NAME change the text channelid to name all this is a defining the read text nw that   we have given it a name we also need to say add a director each time you read the name so bellow that you should see
  
  addDir('','',10,'')
  
  let me break it down for you 
  
addDir('1','2',3,'4')

1. THE NAME 
2. THE URL
3. THE MODE
4. THE ICON

So with kodi you want to remember this bit of code

%s

This meens put it here basically but how does kodi know what to put there this is dont by adding 

%(name)
  ^--- Put The name Of The Fuction Defined Earlier here    

So now it meens put the text 

<a href="showthread.php?tid=.+?" class=".+?" id="tid_.+?">(.+?)</a></strong>
                                                            ^------- FROM HERE
AND

            addDir('','',10,'')
   PUT IT HERE ----^

but make sure that the %(name)is after the comma so it should look like 
addDir('%s'%(name),'',10,'')

the %s will now put the name there now you can experiment just say you want som text befor the name you can do

addDir('ANY TXT HERE %s OR HERE'%(name),'',,'')

now if you plan on having nothing either side you can do this

addDir(name,'',10,'')

all i have done is removed the '' and put name this tells kodi like the other examples to put the name here now there are
other cool exanples you can use to play with the text these are

CHANGE THE COLOR ----> [COLOR yellow]TXT HERE[/COLOR] SO IN YOUR CODE ----> addDir('[COLOR yellow]%s[/COLOR]'%(name),'',10,'')
BOLD TEXT -----> [B]TXT HERE[/B]   SO IN YOUR CODE ----> addDir('[B]%s[/B]'%(name),'',10,'')

Now the code should look like

def REGEX(url):
        link = OPEN_URL(url)
        match=re.compile('<a href="showthread.php?tid=.+?" class=".+?" id="tid_.+?">(.+?)</a></strong>').findall(link)
        for name in match:
            addDir('%s'%(name),'',10,'')

if you want to read 2 items from the code lets say you want to know if its a new or old item so if you go back to the first time you copyed the code you will see that after class=" it says subject_new or will be subject_old to do this just change 

class=".+?"

to

class="(.+?)"

just put brackets around .+? 

now like befor we give it a name il give this newold now look at where its position is in your regxex the first (.+?) is or new old so we want to change 

for name in match:

TO

for newold,name in match:

this tells kodi that the first (.+?) is the newold and the second (.+?) Is The name now we want it to show up in the name of or addDir so change

addDir('%s'%(name),'',10,'')

TO

 addDir('%s %s'%(newold,name),'',10,'')

let me break it down for you

 addDir('%s %s'%(newold,name),'',10,'')
          ^  |     ^     ^
          |  |_____|_____|
          |        |
          >------->^

Now The Complete Code Should Look Like 

def REGEX(url):
        link = OPEN_URL(url)
        match=re.compile('<a href="showthread.php?tid=.+?" class="(.+?)" id="tid_.+?">(.+?)</a></strong>').findall(link)
        for newold,name in match:
            addDir('%s %s'%(newold,name),'',10,'')
########################################################### UPDATE ###########################################################################
########################################################### UPDATE ###########################################################################
Now To Scrape Two Items You must add another
match=re.compile('<a href="showthread.php?tid=.+?" class="(.+?)" id="tid_.+?">(.+?)</a></strong>').findall(link)

under the first one and change match for match2
also you need to add a second
                            V---------- CHANGED TO match2
        for newold,name in match2:
            addDir('%s %s'%(newold,name),'',10,'')

and insert this bellow your 

addDir('%s %s'%(newold,name),'',10,'')

and inline with
        
for newold,name in match:

so the complete code is

def REGEX(url):
        link = OPEN_URL(url)
        match=re.compile('<a href="showthread.php?tid=.+?" class="(.+?)" id="tid_.+?">(.+?)</a></strong>').findall(link)
        match2=re.compile('<a href="showthread.php?tid=.+?" class="(.+?)" id="tid_.+?">(.+?)</a></strong>').findall(link)
        for newold,name in match:
            addDir('%s %s'%(newold,name),'',10,'')
        for newold,name in match2:
            addDir('%s %s'%(newold,name),'',10,'')
			
to add just a directorty handy is you want to add a search button just add

addDir('name','url',10,'icon')
at the top like

def REGEX(url):
        addDir('name','url',10,'icon')
        link = OPEN_URL(url)
        match=re.compile('<a href="showthread.php?tid=.+?" class="(.+?)" id="tid_.+?">(.+?)</a></strong>').findall(link)
        match2=re.compile('<a href="showthread.php?tid=.+?" class="(.+?)" id="tid_.+?">(.+?)</a></strong>').findall(link)
        for newold,name in match:
            addDir('%s %s'%(newold,name),'',10,'')
        for newold,name in match2:
            addDir('%s %s'%(newold,name),'',10,'')
			

########################################################### UPDATE ###########################################################################
########################################################### UPDATE ###########################################################################

Common errors can be a result of spaces or indentations python requires 4 spaces between lines here is an example

def REGEX(url):
<--8--->link = OPEN_URL(url)
<--8--->match=re.compile('<a href="showthread.php?tid=.+?" class="(.+?)" id="tid_.+?">(.+?)</a></strong>').findall(link)
<--8--->for newold,name in match:
<--12------>addDir('%s %s'%(newold,name),'',10,'')

the  next error can be due having 2 (.+?) and not giving the names in

for newold,name in match:

the next error is having the names 

for newold,name in match:

and not putting them in your addDir('','',10,'')
 
