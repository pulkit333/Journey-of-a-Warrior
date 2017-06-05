from pygame.locals import *
import pygame,pygbutton,sys
from random import randint
from random import shuffle
from itertools import chain
armor=-1
level=0
track=0
rain=0
myfont = pygame.font.SysFont("Arial", 30)
myfont1 = pygame.font.SysFont("Arial", 70)
myfont2 = pygame.font.SysFont("Georgia", 28)

def angry_c(a, n, k):
    k=k-1;
    a.sort();
    i=0;
    sm=a[n-1];
    while (i+k)<n:
        d=a[i+k]-a[i];
        if(d<sm):
            sm=d;
        i+=1
    return sm;

def truncline(text, font, maxwidth):
        real=len(text)       
        stext=text           
        l=font.size(text)[0]
        cut=0
        a=0                  
        done=1
        old = None
        while l > maxwidth:
            a=a+1
            n=text.rsplit(None, a)[0]
            if stext == n:
                cut += 1
                stext= n[:-cut]
            else:
                stext = n
            l=font.size(stext)[0]
            real=len(stext)               
            done=0                        
        return real, done, stext             
        
def wrapline(text, font, maxwidth): 
    done=0                      
    wrapped=[]                  
                               
    while not done:             
        nl, done, stext=truncline(text, font, maxwidth) 
        wrapped.append(stext.strip())                  
        text=text[nl:]                                 
    return wrapped
 
 
def wrap_multi_line(text, font, maxwidth):
    """ returns text taking new lines into account.
    """
    lines = chain(*(wrapline(line, font, maxwidth) for line in text.splitlines()))
    return list(lines)

def knapsack(p,w,n,m):
    a = [[0 for x in range(100)] for x in range(100)] 
    for i in range(0,n+1):
        a[0][i]=0
    for j in range(0,m+1):
        a[j][0]=0
    for i in range(1,n+1):
        for j in range (0,m+1):
            if w[i]>j:
                a[i][j]=a[i-1][j]
            else:
                a[i][j]=max(p[i]+a[i-1][j-w[i]],a[i-1][j])
    return a[n][m]

def score(screen,w,v):
    labelw = myfont.render('Weight: '+str(w), 1, (255,0,0))
    labelv= myfont.render('Value: '+str(v), 1, (255,0,0))
    screen.blit(labelw, (1000, 200))
    screen.blit(labelv, (1000, 300))

def dijkstra(graph, initial_node):
    visited = {initial_node: 0}
    current_node = initial_node
    path = {}
    nodes = set(graph.nodes)
    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
 
        if min_node is None:
            break
        nodes.remove(min_node)
        cur_wt = visited[min_node]
        for edge in graph.edges[min_node]:
            wt = cur_wt + graph.distances[(min_node, edge)]
            if edge not in visited or wt < visited[edge]:
                visited[edge] = wt
                path[edge] = min_node
    return visited, path
 
def shortest_path(graph, initial_node, goal_node):
    distances, paths = dijkstra(graph, initial_node)
    route = [goal_node]
    while goal_node != initial_node:
        route.append(paths[goal_node])
        goal_node = paths[goal_node]
 
    route.reverse()
    return route

class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}
    def add_node(self, value):
        self.nodes.add(value)
    def add_edge(self, from_node, to_node, distance):
        self._add_edge(from_node, to_node, distance)
        self._add_edge(to_node, from_node, distance)
 
    def _add_edge(self, from_node, to_node, distance):
        self.edges.setdefault(from_node, [])
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance
class Armory():
    def __init__(self):
        global track
        if track==4:
                pygame.mixer.music.load('5.wav')
                pygame.mixer.music.play()
        p=[0,24,19,20,100,66,30,40,90]
        w=[0,12,10,5,20,30,15,17,30]
        n=8
        m=80
        self.name=['Devil Helm','Horn Helm','Katana','Broad Sword','Steel Armor','Light Armor','Sheild Lion','Sheild Dwarf']
        self.weight=0
        self.val=0;
        self.win=0;
        self.loose=0
        self.full=0
        self.q=0
        self.selected=[0,0,0,0,0,0,0,0]
        self.value=knapsack(p,w,n,m)
        self.night=pygame.image.load('st4.jpg')
        self.nightr=pygame.rect.Rect((0,0),self.night.get_size())
        self.armory=pygame.image.load('armory.jpg')
        self.recta=pygame.rect.Rect((0,0),self.armory.get_size())
        self.background=pygame.image.load('scorearea.jpg')
        self.rectb=pygame.rect.Rect((1000,0),self.background.get_size())
        self.image=pygame.image.load('button.png')
        self.rect=pygame.rect.Rect((13,13),self.image.get_size())
        self.image1=pygame.image.load('button.png')
        self.rect1=pygame.rect.Rect((730,265),self.image1.get_size())
        self.image2=pygame.image.load('button.png')
        self.rect2=pygame.rect.Rect((164,536),self.image2.get_size())
        self.image3=pygame.image.load('button.png')
        self.rect3=pygame.rect.Rect((11,411),self.image3.get_size())
        self.image4=pygame.image.load('button.png')
        self.rect4=pygame.rect.Rect((221,269),self.image4.get_size())
        self.image5=pygame.image.load('button.png')
        self.rect5=pygame.rect.Rect((357,39),self.image5.get_size())
        self.image6=pygame.image.load('button.png')
        self.rect6=pygame.rect.Rect((610,59),self.image6.get_size())
        self.image7=pygame.image.load('button.png')
        self.rect7=pygame.rect.Rect((879,545),self.image7.get_size())
        self.labelw = myfont.render('Weight: '+str(self.weight), 1, (255,0,0))
        self.labelv= myfont.render('Value: '+str(self.val), 1, (255,0,0))

        #text
        self.labelcap = myfont.render(('CAPACITY: 80'), 1, (255,0,0))
        
        self.label1 = myfont.render(('wt=12 atr=24'), 1, (255,0,0))
        self.label2= myfont.render(('wt=10 atr=19'), 1, (255,0,0))
        self.label3 = myfont.render(('wt=5 atr=20'), 1, (255,0,0))
        self.label4 = myfont.render(('wt=20 atr=100'), 1, (255,0,0))
        self.label5 = myfont.render(('wt=30 atr=66'), 1, (255,0,0))
        self.label6 = myfont.render(('wt=15 atr=30'), 1, (255,0,0))
        self.label7 = myfont.render(('wt=17 atr=40'), 1, (255,0,0))
        self.label8 = myfont.render(('wt=30 atr=90'), 1, (255,0,0))

        self.labela = myfont.render(str(self.name[0]), 1, (255,0,0))
        self.labelb = myfont.render(str(self.name[1]), 1, (255,0,0))
        self.labelc = myfont.render(str(self.name[2]), 1, (255,0,0))
        self.labeld = myfont.render(str(self.name[3]), 1, (255,0,0))
        self.labele = myfont.render(str(self.name[4]), 1, (255,0,0))
        self.labelf = myfont.render(str(self.name[5]), 1, (255,0,0))
        self.labelg = myfont.render(str(self.name[6]), 1, (255,0,0))
        self.labelh = myfont.render(str(self.name[7]), 1, (255,0,0))

        self.labela1 = myfont.render(str(u"\u2713"), 1, (255,0,0))
        self.labelb1 = myfont.render(str(u"\u2713"), 1, (255,0,0))
        self.labelc1 = myfont.render(str(u"\u2713"), 1, (255,0,0))
        self.labeld1 = myfont.render(str(u"\u2713"), 1, (255,0,0))
        self.labele1 = myfont.render(str(u"\u2713"), 1, (255,0,0))
        self.labelf1 = myfont.render(str(u"\u2713"), 1, (255,0,0))
        self.labelg1 = myfont.render(str(u"\u2713"), 1, (255,0,0))
        self.labelh1 = myfont.render(str(u"\u2713"), 1, (255,0,0))
        
        self.labelFull = myfont2.render("Bag Full!", 1, (255,0,0))
         
        #buttons
        self.buttonOK = pygbutton.PygButton((1000, 1, 50, 50), 'OK',(  255,   0,   0))
        self.buttonN = pygbutton.PygButton((10, 500, 50, 50), 'NEXT',(  255,   0,   0))
        

    def draw(self,screen):
        if(self.q==0):
                screen.blit(self.night,self.nightr)
                self.buttonN.draw(screen)
        else:
                screen.blit(self.armory,self.recta)
                screen.blit(self.background,self.rectb)
                screen.blit(self.image,self.rect)
                screen.blit(self.image1,self.rect1)
                screen.blit(self.image2,self.rect2)
                screen.blit(self.image3,self.rect3)
                screen.blit(self.image4,self.rect4)
                screen.blit(self.image5,self.rect5)
                screen.blit(self.image6,self.rect6)
                screen.blit(self.image7,self.rect7)

                #text
                screen.blit(self.labelcap, (1030, 400))
                
                screen.blit(self.label1, (50, 7))
                screen.blit(self.label2, (658, 223))
                screen.blit(self.label3, (106, 573))
                screen.blit(self.label4, (6, 371))
                screen.blit(self.label5, (186, 310))
                screen.blit(self.label6, (350, 4))
                screen.blit(self.label7, (497, 27))
                screen.blit(self.label8, (701, 553))
                if(self.selected[0]):
                    screen.blit(self.labela1, (1030, 50))
                if(self.selected[1]):
                    screen.blit(self.labelb1, (1030, 80))
                if(self.selected[2]):
                    screen.blit(self.labelc1, (1030, 110))
                if(self.selected[3]):
                    screen.blit(self.labeld1, (1030, 140))
                if(self.selected[4]):
                    screen.blit(self.labele1, (1030, 170))
                if(self.selected[5]):
                    screen.blit(self.labelf1, (1030, 200))
                if(self.selected[6]):
                    screen.blit(self.labelg1, (1030, 230))
                if(self.selected[7]):
                    screen.blit(self.labelh1, (1030, 260))

                screen.blit(self.labela, (1050, 50))
                screen.blit(self.labelb, (1050, 80))
                screen.blit(self.labelc, (1050, 110))
                screen.blit(self.labeld, (1050, 140))
                screen.blit(self.labele, (1050, 170))
                screen.blit(self.labelf, (1050, 200))
                screen.blit(self.labelg, (1050, 230))
                screen.blit(self.labelh, (1050, 260))


                screen.blit(self.labelw, (1030, 300))
                screen.blit(self.labelv, (1030, 340))

                self.buttonOK.draw(screen)
                if(self.full):
                    screen.blit(self.labelFull, (1030, 500))

    def reRender(self):
        self.labelw = myfont.render('Weight: '+str(self.weight), 1, (255,0,0))
        self.labelv= myfont.render('Value: '+str(self.val), 1, (255,0,0))
        

    def update(self,event):
        global armor,level,track
        if 'click' in self.buttonN.handleEvent(event):
                self.q=1
        #score(screen,self.weight,self.value)
        if self.val > 240 and 'click' in self.buttonOK.handleEvent(event):
            armor=1
            track=5
            pygame.mixer.music.stop()
            s=Final()
            level=5;
        if self.val <= 240 and 'click' in self.buttonOK.handleEvent(event):
            armor=0
            track=5
            pygame.mixer.music.stop()
            s=Final()
            level=5;
        
        
        '''self.labelw = myfont.render('Weight: '+str(self.weight), 1, (255,0,0))
        self.labelv= myfont.render('Value: '+str(self.val), 1, (255,0,0))
        screen.blit(self.labelw, (1000, 200))
        screen.blit(self.labelv, (1000, 300))'''
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if self.rect.collidepoint(x, y):
                if(self.weight+12>80):
                    self.full=1;
                else:
                    self.weight+=12
                    self.val+=24
                    self.selected[0]=1;
            if self.rect1.collidepoint(x, y):
                if(self.weight+10>80):
                    self.full=1;
                else:
                    self.weight+=10
                    self.val+=19
                    self.selected[1]=1;
            if self.rect2.collidepoint(x, y):
                if(self.weight+5>80):
                    self.full=1;
                else:
                    self.weight+=5
                    self.val+=20
                    self.selected[2]=1;
            if self.rect3.collidepoint(x, y):
                if(self.weight+20>80):
                    self.full=1;
                else:
                    self.weight+=20
                    self.val+=100
                    self.selected[3]=1;
            if self.rect4.collidepoint(x, y):
                 if(self.weight+30>80):
                    self.full=1;
                 else:
                    self.weight+=30
                    self.val+=66
                    self.selected[4]=1;
            if self.rect5.collidepoint(x, y):
                if(self.weight+15>80):
                    self.full=1;
                else:
                    self.weight+=15
                    self.val+=30
                    self.selected[5]=1;
            if self.rect6.collidepoint(x, y):
                if(self.weight+17>80):
                    self.full=1;
                else:
                    self.weight+=17
                    self.val+=40
                    self.selected[6]=1;
            if self.rect7.collidepoint(x, y):
                if(self.weight+30>80):
                    self.full=1;
                else:
                    self.weight+=30
                    self.val+=90
                    self.selected[7]=1;
                    

class TextBoxString():
    def __init__(self, string):
        #string that you will be dealing with
        self.totalString = string
        self.currentString = string[0]
        #how many characters you want shown to the screen
        self.length = 0
        #this means that every four times through your 
        #while loop a new char is displayed
        self.loopNum=0
        self.speed = 5
    def addOn(self):
    #adds one to the loop num and then checks if the loop num equals the speed
        self.loopNum += 1
        if self.loopNum == self.speed:
            self.length += 1
            self.loopNum=0
        self.currentString = self.totalString[0: self.length]
    def showAll(self):
        self.length = len(self.totalString)
        self.currentString = self.totalString[0: self.length]


def cycleSort(array):
  writes = 0
 
  # Loop through the array to find cycles to rotate.
  for cycleStart in range(0, len(array) - 1):
    item = array[cycleStart]
 
    # Find where to put the item.
    pos = cycleStart
    for i in range(cycleStart + 1, len(array)):
      if array[i] < item:
        pos += 1
 
    # If the item is already there, this is not a cycle.
    if pos == cycleStart:
      continue
 
    # Otherwise, put the item there or right after any duplicates.
    while item == array[pos]:
      pos += 1
    array[pos], item = item, array[pos]
    writes += 1
 
    # Rotate the rest of the cycle.
    while pos != cycleStart:
 
      # Find where to put the item.
      pos = cycleStart
      for i in range(cycleStart + 1, len(array)):
        if array[i] < item:
          pos += 1
 
      # Put the item there or right after any duplicates.
      while item == array[pos]:
        pos += 1
      array[pos], item = item, array[pos]
      writes += 1
 
  return writes

class Rocks():
    def __init__(self):
        global track
        if track==2:
                pygame.mixer.music.load('3.wav')
                pygame.mixer.music.play()
        self.img=1
        self.y=[455,394,347,283,212]
        self.moves=cycleSort(self.y)
        self.moves-=1
        shuffle(self.y)
        self.Text = TextBoxString("STAGE -1")
        self.i=0
        self.j=0
        self.r=0
        self.m=0
        self.q=0
        #bg='stage2_1.jpg'
        self.imgz=pygame.image.load('st2.jpg')
        self.rz=pygame.rect.Rect((0,0),self.imgz.get_size())
        self.background=pygame.image.load('scorearea.jpg')
        self.rectm=pygame.rect.Rect((1000,0),self.background.get_size())
        self.imagea=pygame.image.load('stage2_1.jpg')
        self.imageb=pygame.image.load('stage2_2.jpg')
        self.recta=pygame.rect.Rect((0,0),self.imagea.get_size())
        self.rectb=pygame.rect.Rect((0,0),self.imageb.get_size())
        
        self.image0=pygame.image.load('rock.png')
        
        self.image1=pygame.image.load('rock.png')
        
        self.image2=pygame.image.load('rock.png')
        
        self.image3=pygame.image.load('rock.png')
        
        self.image4=pygame.image.load('rock.png')
        self.buttonOK = pygbutton.PygButton((1010, 25, 50, 50), 'OK',(  255,   0,   0))
        self.buttonN = pygbutton.PygButton((1006, 19, 50, 50), 'NEXT',(255,0,0))
        self.buttonN2 = pygbutton.PygButton((1006, 500, 50, 50), 'NEXT',(255,0,0))
        #self.label = myfont.render(str(self.name[0]), 1, (255,0,0))
        
    def draw(self,screen):
        if(self.q==0):
                screen.blit(self.imgz,self.rz)
                self.buttonN.draw(screen)
        else:
                screen.blit(self.background, self.rectm)
                if(self.img==1):
                    screen.blit(self.imagea,self.recta)
                elif(self.img==2):
                    screen.blit(self.imageb,self.rectb)
                self.buttonOK.draw(screen)
                self.buttonN2.draw(screen)
                self.rect0=pygame.rect.Rect((126,self.y[0]),self.image0.get_size())
                self.rect1=pygame.rect.Rect((264,self.y[1]),self.image1.get_size())
                self.rect2=pygame.rect.Rect((408,self.y[2]),self.image2.get_size())
                self.rect3=pygame.rect.Rect((554,self.y[3]),self.image3.get_size())
                self.rect4=pygame.rect.Rect((700,self.y[4]),self.image4.get_size())
                screen.blit(self.image0,self.rect0)
                screen.blit(self.image1,self.rect1)
                screen.blit(self.image2,self.rect2)
                screen.blit(self.image3,self.rect3)
                screen.blit(self.image4,self.rect4)

        

    def update(self,event):
        #print(self.m)
        #print(self.moves)
        global level,track
        if 'click' in self.buttonOK.handleEvent(event) and self.y==[455,394,347,283,212]:
                if self.m<=self.moves:
                        self.img=2;
                else:
                        level=7
        if 'click' in self.buttonN2.handleEvent(event) and self.y==[455,394,347,283,212]:
                if self.m<=self.moves:
                        track=3
                        pygame.mixer.music.stop()
                        s=Angry()
                        level=3
                else:
                        track=7
                        pygame.mixer.music.stop()
                        s=Loose()
                        level=7
        if self.q==0:
                if 'click' in self.buttonN.handleEvent(event):
                    self.q=1
        else:
                
                if event.type == MOUSEBUTTONUP:
                    self.Text.showAll()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if self.r==0:
                        if self.rect0.collidepoint(x, y):
                            self.r=1
                            self.i=0
                        if self.rect1.collidepoint(x, y):
                            self.r=1
                            self.i=1
                        if self.rect2.collidepoint(x, y):
                            self.r=1
                            self.i=2
                        if self.rect3.collidepoint(x, y):
                            self.r=1
                            self.i=3
                        if self.rect4.collidepoint(x, y):
                            self.r=1
                            self.i=4
                    elif self.r==1:
                        if self.rect0.collidepoint(x, y):
                            self.r=2
                            self.j=0
                        if self.rect1.collidepoint(x, y):
                            self.r=2
                            self.j=1
                        if self.rect2.collidepoint(x, y):
                            self.r=2
                            self.j=2
                        if self.rect3.collidepoint(x, y):
                            self.r=2
                            self.j=3
                        if self.rect4.collidepoint(x, y):
                            self.r=2
                            self.j=4
                if self.r==2:
                    self.r=0
                    self.m+=1
                    self.y[self.i] ,self.y[self.j]=self.y[self.j] ,self.y[self.i]

class Angry():
    def __init__(self):
        global track
        if track==3:
                pygame.mixer.music.load('4.wav')
                pygame.mixer.music.play()
        self.buttonN = pygbutton.PygButton((10, 500, 50, 50), 'NEXT',(255,0,0))
        self.d=0
        self.w=-1
        self.ln=1
        self.lm=0
        self.img=1
        self.q=0
        self.check=[True,False,False,False]
        self.check1=[False,False,False,False,False,False,False,False,False]
        self.tick=[False,False,False,False,False,False,False,False]
        self.items=[]
        self.selected=[0,0,0,0,0,0,0,0]
        for i in range(0,8):
            self.items.append(randint(15,200))
        self.u=angry_c(self.items,8,5)
        print(self.u)
        self.night=pygame.image.load('st3.jpg')
        self.nightr=pygame.rect.Rect((0,0),self.night.get_size())
        self.background=pygame.image.load('scorearea.jpg')
        self.rectm=pygame.rect.Rect((1000,0),self.background.get_size())
        self.imagea=pygame.image.load('vill.jpg')
        self.imagea1=pygame.image.load('vill1.jpg')
        self.imagea2=pygame.image.load('problem.jpg')
        self.imagea3=pygame.image.load('bk.jpg')
        self.imageb=pygame.image.load('stage2_2.jpg')
        self.recta=pygame.rect.Rect((0,0),self.imagea.get_size())
        self.recta1=pygame.rect.Rect((0,0),self.imagea1.get_size())
        self.recta2=pygame.rect.Rect((0,0),self.imagea2.get_size())
        self.recta3=pygame.rect.Rect((0,0),self.imagea3.get_size())
        self.rectb=pygame.rect.Rect((0,0),self.imageb.get_size())

        #sacks
        self.img1=pygame.image.load('sack.png')
        self.img2=pygame.image.load('sack.png')
        self.img3=pygame.image.load('sack.png')
        self.img4=pygame.image.load('sack.png')
        self.img5=pygame.image.load('sack.png')
        self.img6=pygame.image.load('sack.png')
        self.img7=pygame.image.load('sack.png')
        self.img8=pygame.image.load('sack.png')
        self.imgx1=pygame.image.load('sack1.png')
        self.imgx2=pygame.image.load('sack1.png')
        self.imgx3=pygame.image.load('sack1.png')
        self.imgx4=pygame.image.load('sack1.png')
        self.imgx5=pygame.image.load('sack1.png')
        self.imgx6=pygame.image.load('sack1.png')
        self.imgx7=pygame.image.load('sack1.png')
        self.imgx8=pygame.image.load('sack1.png')
        self.r1=pygame.rect.Rect((34 ,423),self.img1.get_size())
        self.r2=pygame.rect.Rect((152 ,264),self.img2.get_size())
        self.r3=pygame.rect.Rect((302 ,421),self.img3.get_size())
        self.r4=pygame.rect.Rect((441 ,269),self.img4.get_size())
        self.r5=pygame.rect.Rect((445 ,57),self.img5.get_size())
        self.r6=pygame.rect.Rect((580 ,428),self.img6.get_size())
        self.r7=pygame.rect.Rect((725 ,272),self.img7.get_size())
        self.r8=pygame.rect.Rect((847 ,434),self.img8.get_size())
        self.rx1=pygame.rect.Rect((34 ,423),self.imgx1.get_size())
        self.rx2=pygame.rect.Rect((152 ,264),self.imgx2.get_size())
        self.rx3=pygame.rect.Rect((302 ,421),self.imgx3.get_size())
        self.rx4=pygame.rect.Rect((441 ,269),self.imgx4.get_size())
        self.rx5=pygame.rect.Rect((445 ,57),self.imgx5.get_size())
        self.rx6=pygame.rect.Rect((580 ,428),self.imgx6.get_size())
        self.rx7=pygame.rect.Rect((725 ,272),self.imgx7.get_size())
        self.rx8=pygame.rect.Rect((847 ,434),self.imgx8.get_size())
        
        self.Text1=TextBoxString("The hero arrives at the village of Feldunim where the people of the mountain valley live.")
        self.Text2=TextBoxString("The village is in bad shape, it looks under populated and torn.")
        self.Text3=TextBoxString("Poverty,pestilance,starvation and strife signs of the coming of dragons, of the start of the dragon king festival.") 
        self.Text4=TextBoxString("Knowning not what was ahead of him the hero enters............")
        self.Text5=TextBoxString("Wise man - Ho!, who goes there")
        self.Text6=TextBoxString("Warrior - A warrior from far lands wise one.")
        self.Text7=TextBoxString("wise man -It is a rare sight to see a warrior as you in these lands, ")
        self.Text8=TextBoxString("what bussiness do you have in a land over run by dragons.")
        self.Text9=TextBoxString("Warrior- wa - I have to do a deed of true valor to be knighted at the round table , can you help me wise one.")
        self.Text10=TextBoxString("Wise man -I can indeed but you have to help me first. The village as you can see faces starvation but ")
        self.Text11=TextBoxString("that is not the problem. We have food to distribute but we have no leader to distribute it in equal rations ")
        self.Text12=TextBoxString("we need a strong leader to be able to do so.If you distribue the food with out any riots then I will give you the knowledge you seek. ")
        self.Text13=TextBoxString("So here are the details of the problem.")
        self.buttonOK1 = pygbutton.PygButton((1000, 500, 50, 50), 'NEXT',(  255,   0,   0))
        self.buttonOK2 = pygbutton.PygButton((1000, 500, 50, 50), 'NEXT',(  255,   0,   0))
        self.buttonOK3 = pygbutton.PygButton((1000, 500, 80, 50), 'SOLVE',(  255,   0,   0))
        self.buttonOK4 = pygbutton.PygButton((1000, 500, 80, 50), 'OK',(  255,   0,   0))


    def draw(self,screen):
        if(self.q==0):
                screen.blit(self.night,self.nightr)
                self.buttonN.draw(screen)
        else:
                screen.blit(self.background, self.rectm)
                if self.img==1:
                        screen.blit(self.imagea,self.recta)
                        self.buttonOK1.draw(screen)
                
                elif self.img==2:
                        screen.blit(self.imagea1,self.recta1)
                        self.check=[False,False,False,False]
                        self.check1[0]=True
                        if self.lm==0:
                                self.lm=1
                        self.ln=0
                        self.buttonOK2.draw(screen)
                elif self.img==3:
                        self.check1=[False,False,False,False,False,False,False,False,False]
                        screen.blit(self.imagea2,self.recta2)
                        self.check=[False,False,False,False]
                        self.buttonOK3.draw(screen)
                elif self.img==4:
                        self.check1=[False,False,False,False,False,False,False,False,False]
                        screen.blit(self.imagea3,self.recta3)
                        self.check=[False,False,False,False]
                        self.buttonOK4.draw(screen)
                text1 = myfont2.render(self.Text1.currentString, 1,(255,255,0))
                text2 = myfont2.render(self.Text2.currentString, 1,(255,255,0))
                text3 = myfont2.render(self.Text3.currentString, 1,(255,255,0))
                text4 = myfont2.render(self.Text4.currentString, 1,(255,255,0))
                text5 = myfont2.render(self.Text5.currentString, 1,(255,0,0))
                text6 = myfont2.render(self.Text6.currentString, 1,(255,0,0))
                text7 = myfont2.render(self.Text7.currentString, 1,(255,0,0))
                text8 = myfont2.render(self.Text8.currentString, 1,(255,0,0))
                text9 = myfont2.render(self.Text9.currentString, 1,(255,0,0))
                text10 = myfont2.render(self.Text10.currentString, 1,(255,0,0))
                text11 = myfont2.render(self.Text11.currentString, 1,(255,0,0))
                text12 = myfont2.render(self.Text12.currentString, 1,(255,0,0))
                text13 = myfont2.render(self.Text13.currentString, 1,(255,0,0))
                
                if(self.check[0]):
                        screen.blit(text1, (0,0))
                        self.Text1.addOn()
                if(self.check[1]):
                        screen.blit(text2, (0,50))
                        self.Text2.addOn()
                if(self.check[2]):
                        screen.blit(text3, (0,100))
                        self.Text3.addOn()
                if(self.check[3]):
                        screen.blit(text4, (0,150))
                        self.Text4.addOn()
                if(self.check1[0]):
                        screen.blit(text5, (0,0))
                        self.Text5.addOn()
                if(self.check1[1]):
                        screen.blit(text6, (0,50))
                        self.Text6.addOn()
                if(self.check1[2]):
                        screen.blit(text7, (0,100))
                        self.Text7.addOn()
                if(self.check1[3]):
                        screen.blit(text8, (0,150))
                        self.Text8.addOn()
                if(self.check1[4]):
                        screen.blit(text9, (0,200))
                        self.Text9.addOn()
                if(self.check1[5]):
                        screen.blit(text10, (0,250))
                        self.Text10.addOn()
                if(self.check1[6]):
                        screen.blit(text11, (0,300))
                        self.Text11.addOn()
                if(self.check1[7]):
                        screen.blit(text12, (0,350))
                        self.Text12.addOn()
                if(self.check1[8]):
                        screen.blit(text13, (0,400))
                        self.Text13.addOn()
                if(self.img==4):
                        if(not self.tick[0]):
                                screen.blit(self.img1,self.r1)
                        else:
                                screen.blit(self.imgx1,self.rx1)
                        if(not self.tick[1]):
                                screen.blit(self.img2,self.r2)
                        else:
                                screen.blit(self.imgx2,self.rx2)
                        if(not self.tick[2]):
                                screen.blit(self.img3,self.r3)
                        else:
                                screen.blit(self.imgx3,self.rx3)
                        if(not self.tick[3]):
                                screen.blit(self.img4,self.r4)
                        else:
                                screen.blit(self.imgx4,self.rx4)
                        if(not self.tick[4]):
                                screen.blit(self.img5,self.r5)
                        else:
                                screen.blit(self.imgx5,self.rx5)
                        if(not self.tick[5]):
                                screen.blit(self.img6,self.r6)
                        else:
                                screen.blit(self.imgx6,self.rx6)
                        if(not self.tick[6]):
                                screen.blit(self.img7,self.r7)
                        else:
                                screen.blit(self.imgx7,self.rx7)
                        if(not self.tick[7]):
                                screen.blit(self.img8,self.r8)
                        else:
                                screen.blit(self.imgx8,self.rx8)

               

                #items text
                self.labela = myfont.render(str(self.items[0]), 1, (255,0,0))
                self.labelb = myfont.render(str(self.items[1]), 1, (255,0,0))
                self.labelc = myfont.render(str(self.items[2]), 1, (255,0,0))
                self.labeld = myfont.render(str(self.items[3]), 1, (255,0,0))
                self.labele = myfont.render(str(self.items[4]), 1, (255,0,0))
                self.labelf = myfont.render(str(self.items[5]), 1, (255,0,0))
                self.labelg = myfont.render(str(self.items[6]), 1, (255,0,0))
                self.labelh = myfont.render(str(self.items[7]), 1, (255,0,0))

                
                if self.img==4:
                        screen.blit(self.labela, (100, 496))
                        screen.blit(self.labelb, (225, 342))
                        screen.blit(self.labelc, (360, 508))
                        screen.blit(self.labeld, (506, 340))
                        screen.blit(self.labele, (518, 146))
                        screen.blit(self.labelf, (640, 512))
                        screen.blit(self.labelg, (795, 342))
                        screen.blit(self.labelh, (917, 511))

    def update(self,event):
        global level,track
        if 'click' in self.buttonN.handleEvent(event):
            self.q=1;
        if 'click' in self.buttonOK1.handleEvent(event) and self.img==1:
            self.img=2;
        elif 'click' in self.buttonOK2.handleEvent(event) and self.img==2:
            self.img=3;
        elif 'click' in self.buttonOK3.handleEvent(event) and self.img==3:
            self.img=4;
        elif 'click' in self.buttonOK4.handleEvent(event) and self.d==5:
            a=[]
            for i in self.selected:
                    if i !=0:
                            a.append(i)
            a.sort()
            if(a[4]-a[0]==self.u):
                    pygame.mixer.music.stop()
                    track=4
                    s=Armory()
                    level=4
            else:
                    pygame.mixer.music.stop()
                    track=7
                    s=Loose()
                    level=7
        if event.type == MOUSEBUTTONDOWN and self.ln==1:
            self.ln=2
            self.check[1]=True
        elif event.type == MOUSEBUTTONDOWN and self.ln==2:
            self.ln=3
            self.check[2]=True
        elif event.type == MOUSEBUTTONDOWN and self.ln==3:
            self.ln=4
            self.check[3]=True
        elif event.type == MOUSEBUTTONDOWN and self.ln==4:
            self.ln=5
        elif event.type == MOUSEBUTTONDOWN and self.lm==1:
            self.lm=2
            self.check1[1]=True
        elif event.type == MOUSEBUTTONDOWN and self.lm==2:
            self.lm=3
            self.check1[2]=True
        elif event.type == MOUSEBUTTONDOWN and self.lm==3:
            self.lm=4
            self.check1[3]=True
        elif event.type == MOUSEBUTTONDOWN and self.lm==4:
            self.lm=5
            self.check1[4]=True
        elif event.type == MOUSEBUTTONDOWN and self.lm==5:
            self.lm=6
            self.check1[5]=True
        elif event.type == MOUSEBUTTONDOWN and self.lm==6:
            self.lm=7
            self.check1[6]=True
        elif event.type == MOUSEBUTTONDOWN and self.lm==7:
            self.lm=8
            self.check1[7]=True
        elif event.type == MOUSEBUTTONDOWN and self.lm==8:
            self.lm=9
            self.check1[8]=True


        #sack update
        if self.img==4:
                if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        if self.r1.collidepoint(x, y):
                                if(not self.tick[0]):
                                        self.tick[0]=True
                                        self.d+=1
                                        self.selected[0]+=self.items[0]
                                else:
                                        self.d-=1
                                        self.tick[0]=False
                                        self.selected[0]=0
                        if self.r2.collidepoint(x, y):
                                if(not self.tick[1]):
                                        self.tick[1]=True
                                        self.d+=1
                                        self.selected[1]+=self.items[1]
                                else:
                                        self.d-=1
                                        self.tick[1]=False
                                        self.selected[1]=0
                        if self.r3.collidepoint(x, y):
                                if(not self.tick[2]):
                                        self.tick[2]=True
                                        self.d+=1
                                        self.selected[2]+=self.items[2]
                                else:
                                        self.d-=1
                                        self.tick[2]=False
                                        self.selected[2]=0
                        if self.r4.collidepoint(x, y):
                                if(not self.tick[3]):
                                        self.tick[3]=True
                                        self.selected[3]+=self.items[3]
                                        self.d+=1
                                else:
                                        self.d-=1
                                        self.tick[3]=False
                                        self.selected[3]=0
                        if self.r5.collidepoint(x, y):
                                if(not self.tick[4]):
                                        self.tick[4]=True
                                        self.d+=1
                                        self.selected[4]+=self.items[4]
                                else:
                                        self.d-=1
                                        self.tick[4]=False
                                        self.selected[4]=0
                        if self.r6.collidepoint(x, y):
                                if(not self.tick[5]):
                                        self.tick[5]=True
                                        self.d+=1
                                        self.selected[5]+=self.items[5]
                                else:
                                        self.d-=1
                                        self.tick[5]=False
                                        self.selected[5]=0
                        if self.r7.collidepoint(x, y):
                                if(not self.tick[6]):
                                        self.tick[6]=True
                                        self.d+=1
                                        self.selected[6]+=self.items[6]
                                else:
                                        self.d-=1
                                        self.tick[6]=False
                                        self.selected[6]=0
                        if self.r8.collidepoint(x, y):
                                if(not self.tick[7]):
                                        self.tick[7]=True
                                        self.d+=1
                                        self.selected[7]+=self.items[7]
                                else:
                                        self.d-=1
                                        self.tick[7]=False
                                        self.selected[7]=0
                    
        
       
        
class Map():
    def __init__(self):
        global track
        if track==1:
                pygame.mixer.music.load('2.wav')
                pygame.mixer.music.play()
        self.dj=[]
        self.ar=[]
        for i in range(0,12):
            self.ar.append(randint(1,10))
        global myfont
        self.win=0
        self.loose=0
        self.q=0
        self.t=0
        #djkstra runner
        g = Graph()
        g.nodes = set(range(1, 9))
        g.add_edge(1,2,self.ar[0]);
        g.add_edge(2,3,self.ar[1]);
        g.add_edge(3,4,self.ar[2]);
        g.add_edge(4,9,self.ar[3]);
        g.add_edge(9,8,self.ar[4]);
        g.add_edge(8,7,self.ar[5]);
        g.add_edge(7,6,self.ar[6]);
        g.add_edge(6,1,self.ar[7]);
        g.add_edge(6,5,self.ar[8]);
        g.add_edge(5,2,self.ar[9]);
        g.add_edge(5,9,self.ar[10]);
        g.add_edge(5,3,self.ar[11]);
        self.m=shortest_path(g, 1, 9)

        self.img=pygame.image.load('st1.jpg')
        self.r=pygame.rect.Rect((0,0),self.img.get_size())
        self.image=pygame.image.load('map.jpg')
        self.rect=pygame.rect.Rect((0,0),self.image.get_size())
        self.background=pygame.image.load('scorearea.jpg')
        self.rectb=pygame.rect.Rect((1000,0),self.background.get_size())
        
        
        self.button1 = pygbutton.PygButton((339, 123, 20, 20), 'A')
        self.button2 = pygbutton.PygButton((284, 194, 20, 20), 'B')
        self.button3 = pygbutton.PygButton((198, 278, 20, 20), 'C')
        self.button4 = pygbutton.PygButton((255, 357, 20, 20), 'D')
        self.button5 = pygbutton.PygButton((393, 235, 20, 20), 'E')
        self.button6 = pygbutton.PygButton((565, 164, 20, 20), 'F')
        self.button7 = pygbutton.PygButton((668, 286, 20, 20), 'G')
        self.button8 = pygbutton.PygButton((496, 326, 20, 20), 'H')
        self.button9 = pygbutton.PygButton((421, 447, 20, 20), 'I')
        #ok and restart button
        self.buttonN = pygbutton.PygButton((1006, 19, 50, 50), 'NEXT',(255,0,0))
        self.buttonOK = pygbutton.PygButton((1100, 25, 50, 50), 'OK',(255,0,0))
        self.buttonR = pygbutton.PygButton((1010, 323, 50, 50), 'RESET',(255,0,0))
        self.buttonH = pygbutton.PygButton((1010, 500, 50, 50), 'HELP',(255,0,0))
        #text
        self.label1 = myfont.render(str(self.ar[0]), 1, (255,0,0))
        self.label2= myfont.render(str(self.ar[1]), 1, (255,0,0))
        self.label3 = myfont.render(str(self.ar[2]), 1, (255,0,0))
        self.label4 = myfont.render(str(self.ar[3]), 1, (255,0,0))
        self.label5 = myfont.render(str(self.ar[4]), 1, (255,0,0))
        self.label6 = myfont.render(str(self.ar[5]), 1, (255,0,0))
        self.label7 = myfont.render(str(self.ar[6]), 1, (255,0,0))
        self.label8 = myfont.render(str(self.ar[7]), 1, (255,0,0))
        self.label9 = myfont.render(str(self.ar[8]), 1, (255,0,0))
        self.label10 = myfont.render(str(self.ar[9]), 1, (255,0,0))
        self.label11 = myfont.render(str(self.ar[10]), 1, (255,0,0))
        self.label12 = myfont.render(str(self.ar[11]), 1, (255,0,0))
        self.labelh = myfont.render(str(self.m), 1, (255,0,0))
        self.labelpath = myfont.render('Move A to I', 1, (255,0,0))

        
    def draw(self,screen):
        
        if(self.q==0):
                screen.blit(self.img,self.r)
                self.buttonN.draw(screen)
        else:
                screen.fill( (0,0,0) )
                screen.blit(self.image,self.rect)
                screen.blit(self.background, self.rectb)
                self.button1.draw(screen)
                self.button2.draw(screen)
                self.button3.draw(screen)
                self.button4.draw(screen)
                self.button5.draw(screen)
                self.button6.draw(screen)
                self.button7.draw(screen)
                self.button8.draw(screen)
                self.button9.draw(screen)
                self.buttonOK.draw(screen)
                self.buttonR.draw(screen)
                self.buttonH.draw(screen)

        #text
                screen.blit(self.labelpath, (1010, 150))
                
                screen.blit(self.label1, (208, 106))
                screen.blit(self.label2, (141, 187))
                screen.blit(self.label3, (235, 314))
                screen.blit(self.label4, (355, 411))
                screen.blit(self.label5, (506, 417))
                screen.blit(self.label6, (620, 341))
                screen.blit(self.label7, (583, 243))
                screen.blit(self.label8, (462, 108))
                screen.blit(self.label9, (487, 227))
                screen.blit(self.label10, (356, 194))
                screen.blit(self.label11, (404, 329))
                screen.blit(self.label12, (291, 250))
                if(self.t==1):
                        screen.blit(self.labelh, (1010, 250))
        

    def update(self,event):
        global level,track
        if 'click' in self.buttonN.handleEvent(event):
            self.q=1
        elif 'click' in self.buttonH.handleEvent(event):
            self.t=1
        elif self.m==self.dj and 'click' in self.buttonOK.handleEvent(event):
            track=2
            pygame.mixer.music.stop()
            s=Rocks()
            level=2
        elif self.m!=self.dj and 'click' in self.buttonOK.handleEvent(event):
            track=7
            pygame.mixer.music.stop()
            s=Loose()    
            level=7
        else:
                if 'click' in self.buttonR.handleEvent(event):
                    del self.dj[:]
                if 'click' in self.button1.handleEvent(event):
                    self.dj.append(1)
                if 'click' in self.button2.handleEvent(event):
                    self.dj.append(2)
                if 'click' in self.button3.handleEvent(event):
                    self.dj.append(3)
                if 'click' in self.button4.handleEvent(event):
                    self.dj.append(4)
                if 'click' in self.button5.handleEvent(event):
                    self.dj.append(5)
                if 'click' in self.button6.handleEvent(event):
                    self.dj.append(6)
                if 'click' in self.button7.handleEvent(event):
                    self.dj.append(7)
                if 'click' in self.button8.handleEvent(event):
                    self.dj.append(8)
                if 'click' in self.button9.handleEvent(event):
                    self.dj.append(9)


class Final():
        def __init__(self):
                global track
                if track==5:
                        pygame.mixer.music.load('6.wav')
                        pygame.mixer.music.play()
                self.healthw=100
                self.healthd=100
                self.image=pygame.image.load('final.jpg')
                self.rect=pygame.rect.Rect((0,0),self.image.get_size())
                self.img1=pygame.image.load('fires.png')
                self.r1=pygame.rect.Rect((910,208),self.img1.get_size())
                self.img2=pygame.image.load('sworda.png')
                self.r2=pygame.rect.Rect((250,361),self.img2.get_size())
                self.buttonOK = pygbutton.PygButton((520, 69, 75, 50), 'ATTACK',(255,0,0))
                self.warrior=0
                
        
        def draw(self,screen):
                global armor
                screen.blit(self.image,self.rect)
                self.buttonOK.draw(screen)

                self.labelw = myfont.render(str(self.healthw), 1, (255,0,0))
                self.labeld= myfont.render(str(self.healthd), 1, (255,0,0))
                screen.blit(self.labelw, (292, 52))
                screen.blit(self.labeld, (996, 52))
                if(self.warrior==1):
                        screen.blit(self.img2,self.r2)
                        self.r2.x+=5
                        screen.blit(self.img1,self.r1)
                        self.r1.x-=5
                        self.r1.y+=1
                if(self.r1.x<0):
                        
                        if(armor==1):
                                self.healthw-=30
                                self.healthd-=40
                        else:
                                self.healthd-=30
                                self.healthw-=40
                        
                        #pygame.time.delay(100)
                        self.warrior=0
                        self.r1.x=910
                        self.r1.y=208
                        self.r2.x=250
        def update(self,event):
                global level,track
                if 'click' in self.buttonOK.handleEvent(event) and self.warrior==0:
                        self.warrior=1
                if self.healthw<0:
                        self.healthw=0
                if self.healthd<0:
                        self.healthd=0
                if self.healthw==0:
                        pygame.mixer.music.stop()
                        track=7
                        s=Loose()
                        level=7
                if self.healthd==0:
                        pygame.mixer.music.stop()
                        track=6
                        s=Win()
                        level=6
class Credits():
        
        def __init__(self):
                global level,track
                if track==8:
                        pygame.mixer.music.load('9.wav')
                        pygame.mixer.music.play(-1)
                self.image=pygame.image.load('Pulkit Pics.jpg')
                self.rect=pygame.rect.Rect((0,0),self.image.get_size())
                
        def draw(self,screen):
                screen.blit(self.image,self.rect)
               
        def update(self,event):
                global level,track
                if event.type==pygame.KEYDOWN:
                        key = pygame.key.get_pressed()
                        if key[pygame.K_SPACE]:
                                pygame.mixer.music.stop()
                                track=0
                                s=Opening()
                                level=0
                        
class Opening():
        def __init__(self):
                global track
                if(track==0):
                        pygame.mixer.music.load('1.wav')
                        pygame.mixer.music.play()
                self.image=pygame.image.load('Title.jpg')
                self.rect=pygame.rect.Rect((0,0),self.image.get_size())
                self.image1=pygame.image.load('story.jpg')
                self.rect1=pygame.rect.Rect((0,0),self.image1.get_size())
                self.buttons = pygbutton.PygButton((19, 541, 70, 70), 'NEXT',(255,0,0))
                self.buttonm = pygbutton.PygButton((88, 27, 20, 20), '',(255,0,0))
                self.buttonc = pygbutton.PygButton((1006, 19, 20, 20), '',(255,0,0))

        def draw(self,screen):
                global rain
                if rain==0:
                        screen.blit(self.image,self.rect)
                        self.buttonm.draw(screen)
                        self.buttonc.draw(screen)
                if rain==1:
                        screen.blit(self.image1,self.rect1)
                        self.buttons.draw(screen)
                

        def update(self,event):
                global level,track,rain
                if 'click' in self.buttonm.handleEvent(event):
                        rain=1
                if 'click' in self.buttons.handleEvent(event):
                        track=1
                        pygame.mixer.music.stop()
                        s=Map()
                        level=1
                if 'click' in self.buttonc.handleEvent(event):
                        track=8
                        pygame.mixer.music.stop()
                        s=Credits()
                        level=8

class Win():
        def __init__(self):
                global track
                if track==6:
                        pygame.mixer.music.load('7.wav')
                        pygame.mixer.music.play()
                self.image=pygame.image.load('win.jpg')
                self.rect=pygame.rect.Rect((0,0),self.image.get_size())
                self.buttonc = pygbutton.PygButton((10, 500, 75, 75), 'RESTART',(255,0,0))
        def draw(self,screen):
                screen.blit(self.image,self.rect)
                self.buttonc.draw(screen)

        def update(self,event):
                global level,track,rain
                if 'click' in self.buttonc.handleEvent(event):
                        track=0
                        pygame.mixer.music.stop()
                        s=Opening()
                        rain=0
                        level=0
                        
class Loose():
        def __init__(self):
                global track
                if track==7:
                        pygame.mixer.music.load('8.wav')
                        pygame.mixer.music.play()
                self.image=pygame.image.load('loose.jpg')
                self.rect=pygame.rect.Rect((0,0),self.image.get_size())
                self.buttonc = pygbutton.PygButton((10, 500, 75, 75), 'RESTART',(255,0,0))

        def draw(self,screen):
                screen.blit(self.image,self.rect)
                self.buttonc.draw(screen)
        def update(self,event):
                global level,rain,track
                if 'click' in self.buttonc.handleEvent(event):
                        track=0
                        pygame.mixer.music.stop()
                        s=Opening()
                        rain=0
                        level=0
                        
class Game(object):
    def main(self,screen):
        
        global level
        level=0
        
        self.opening=Opening()
        clock=pygame.time.Clock()
        while 1:
            clock.tick(100)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if(level==0):
                        self.credits=Credits()
                        self.map=Map()
                        self.armory=Armory()
                        self.rocks=Rocks()
                        self.angry=Angry()
                        self.final=Final()
                        self.win=Win()
                        self.loose=Loose()
                        self.opening.update(event)
                elif(level==1):
                        self.map.update(event)
                elif(level==2):
                        self.rocks.update(event)
                elif(level==3):
                        self.angry.update(event)
                elif(level==4):
                        self.armory.update(event)
                        self.armory.reRender()
                elif(level==5):
                        self.final.update(event)
                elif(level==6):
                        self.win.update(event)
                elif(level==7):
                        self.loose.update(event)
                elif(level==8):
                        self.credits.update(event)
                #self.rocks.update(event)
                #self.angry.update(event)
                #self.armory.update(event)
                #self.final.update(event)
                
            #screen.blit(background,(1000,0))
            if(level==0):
                    screen.fill( (0,0,0) )
                    self.opening.draw(screen)
            
            elif(level==1):
                    screen.fill( (0,0,0) )
                    self.map.draw(screen)
            elif(level==2):
                    screen.fill( (0,0,0) )
                    self.rocks.draw(screen)
            elif(level==3):
                    screen.fill( (0,0,0) )
                    self.angry.draw(screen)
            elif(level==4):
                    screen.fill( (0,0,0) )
                    self.armory.draw(screen)
            elif(level==5):
                    screen.fill( (0,0,0) )
                    self.final.draw(screen)
            elif(level==6):
                    screen.fill( (0,0,0) )
                    self.win.draw(screen)
            elif(level==7):
                    screen.fill( (0,0,0) )
                    self.loose.draw(screen)
            elif(level==8):
                    screen.fill( (0,0,0) )
                    self.credits.draw(screen)
            #screen.blit(background,(1000,0))
            pygame.display.flip()
            #self.sword.update()

if __name__=='__main__':
    pygame.init()
    pygame.mixer.init()
    screen=pygame.display.set_mode((1200,600),FULLSCREEN)
    Game().main(screen)
            
