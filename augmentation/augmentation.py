from PIL import Image
from random import randint
import colorsys

def Crop(im, xmin, ymin, xmax, ymax):
    largeur,hauteur=im.size
    x1 = randint(0,xmin-5)
    y1 = randint(0, ymin-5)
    x2 = randint(xmax+5,largeur-1)
    y2 = randint(ymax+5,hauteur-1)
    larg2 = x2+1-x1
    haut2 = y2+1-y1
    im2 = Image.new( mode = "RGB", size = (larg2, haut2), color = (0, 0, 0))
    for x in range(larg2):
        for y in range(haut2):
            im2.putpixel((x,y), im.getpixel((x1+x,y1+y)))
    return im2, xmin-x1, ymin-y1, xmax-x1, ymax-y1

def FlouGaussien(im):
    largeur,hauteur=im.size
    im2 = Image.new( mode = "RGB", size = (largeur, hauteur), color = (0, 0, 0))
    for x in range(largeur):
        for y in range(hauteur):
            pixo=im.getpixel((x,y))
            r = 4*pixo[0]
            g = 4*pixo[1]
            b = 4*pixo[2]
            p=4
            if x!=0:
                pix=im.getpixel((x-1,y))
                r+=pix[0]
                g+=pix[1]
                b+=pix[2]
                p+=1
            if x!=(largeur-1):
                pix=im.getpixel((x+1,y))
                r+=pix[0]
                g+=pix[1]
                b+=pix[2]
                p+=1
            if y!=0:
                pix=im.getpixel((x,y-1))
                r+=pix[0]
                g+=pix[1]
                b+=pix[2]
                p+=1
            if y!=(hauteur-1):
                pix=im.getpixel((x,y+1))
                r+=pix[0]
                g+=pix[1]
                b+=pix[2]
                p+=1
            Npix = (r//p,g//p,b//p)
            im2.putpixel((x,y),Npix)
    return im2

def DistorsionCouleur(im):
    largeur,hauteur=im.size
    for x in range(largeur):
        for y in range(hauteur):
            pi = im.getpixel((x,y))
            pix = colorsys.rgb_to_hsv(float(pi[0])/255.0,float(pi[1])/255.0,float(pi[2])/255.0)
            h = min(pix[0]+0.05,1.0)
            s = max(pix[1]-0.1,0.0)
            v = min(pix[2]+0.15,1.0)
            t=colorsys.hsv_to_rgb(h,s,v)
            r=int(t[0]*255)
            g=int(t[1]*255)
            b=int(t[2]*255)
            pix2=(r,g,b)
            im.putpixel((x,y),pix2)
    return im

def Rotation(im):
    largeur,hauteur=im.size
    angle = randint(355,365)%360
    im2 = im.rotate(angle)
    return im2

im = Image.open("C:\\Users\\Marc\\Documents\\projet-p5\\couverture bd.png")
largeur,hauteur=im.size
for x in range(largeur):
    for y in range(hauteur):
        if im.getpixel((x,y))[0]>180:
            im.putpixel((x,y),(255,255,255))
im.save("C:\\Users\\Marc\\Documents\\projet-p5\\nouvelleCouvertureBD.png")