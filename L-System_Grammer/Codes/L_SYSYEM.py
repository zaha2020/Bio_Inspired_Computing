# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 21:41:07 2022

@author: Zaha
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import turtle
import random

class L_system:                         # Making lsystem class and defining some functions
    
    def __init__(self):
        """create an empty list for rules 
            and an empty base axiom
        """
        self.base = ''
        self.rules = []
        
    def Set_Base(self, new_base):       ## Setting a base axiom for L-System
        """
        Args:
            new_base (str)
        """
        self.base = new_base

    def Add_Rule(self, new_rule):       ## Adding a new rule to Rules of L-System
        """
        Args:
            get a rule as a list. first item of list 
            is left side of replacement rule and second item of 
            list is right side of rule
        """
        self.rules.append(new_rule)


    def Generate(self, initial_string):    ## Creating next generation of string
        """
        Returns:
            str: new string after replacements of rules
        """
        new_string= ''
        for character in initial_string:
            found_rule=False
            for rule in self.rules:
                if rule[0]==character:
                    new_string = new_string + rule[1]
                    found=True
                    break
            if found_rule==False:
                new_string = new_string + character
        return new_string
    
    def Build_String(self, n_iteration):     ## Generating string after given iterations
        """
        Returns:
            str: generated string of L-system after specified iterations
        """
        n_string = self.base
        for i in range(n_iteration):
            n_string = self.Generate(n_string)
        return n_string


"-----------------------------------------------------------------------"

class Turtle:      # Making Turtle class and defining some functions

    def __init__(self,  dx = 800, dy = 800):
        
        """
        Args:
            dx: width of screen.
            dy: height of screen
        """
        turtle.setup(width = dx, height = dy )
        
    def Draw_String(self, d_string, distance, angle):  ## Selecting the movement of turtle.
         
        """
        Args:
            d_string (str): given str which we want to draw
            distance : distance for forward
            angle : angle of rotations (degree)
        """
        stack = []
        color_stack = []
        for character in d_string:
            if character =='F':
                turtle.forward(distance)
            elif character == '-':
                turtle.right(angle)
            elif character=='+':
                turtle.left(angle)
            elif character=='[':
                stack.append([turtle.position(), turtle.heading()])
            elif character==']':
                turtle.penup()      
                pop_item = stack.pop()
                turtle.setheading(pop_item[1])
                turtle.goto(pop_item[0])
                turtle.pendown()
            elif character == '<':
                color_stack.append(turtle.color()[0])
            elif character == '>':
                col = color_stack.pop()
                turtle.color(col)
            elif character =='&':
                turtle.pitch(angle)
            elif character =='^':
                turtle.pitch(-angle)
            elif character=='\\':
                turtle.roll(angle)
            elif character=='/':
                turtle.roll(-angle)
            elif character =='g':
                turtle.color((0, 0.5, 0), (0, 0.5, 0))
            elif character=='y':
                turtle.color((0.5,0.25,0),(0.5,0.25,0))
            elif character=='r':
                turtle.color('red')
        turtle.update()
        
    def Hold(self):   ## This func Holds the screen open until the user clicks or types 'q'
        turtle.listen()
        turtle.ht()
        turtle.update()
        turtle.onkey( turtle.bye, 'q' )
        turtle.onscreenclick( lambda x,y: turtle.bye() )
        turtle.mainloop()
        exit()
        

    def Go_to(self, xpos, ypos):     ## Going to a given point without drawing
        turtle.penup()
        turtle.goto(xpos,ypos)
        turtle.pendown()
        
    def color(self, c): ## Setting color of turtle
        turtle.color(c)
   
    def Place(self, xpos, ypos, angle=None):   ## Going to the given point with optional rotation without drawing
        turtle.penup()
        turtle.goto(xpos,ypos)
        if angle!=None:
            turtle.setheading(angle)
        turtle.pendown()
        

"---------------------------------"
def main():
    
    """
    Test the ability of the Turtle to draw trees.
    The program specifies an L-system with base axiom and replacement rules and then
    draws 5 trees in the screen, using 3-5 iterations  of the rule to generate the string.
    """
    
    tree1 = L_system()
    tree2= L_system()
    tree3= L_system()
    tree4= L_system()
    tree5 = L_system()
    
    
    tree1.Set_Base('X')
    tree1.Add_Rule(['X', 'Z+[X+P]--[--<yL>]I[++<yL>]-[XP]++XP'])
    tree1.Add_Rule(['Z', 'FI[+<yL>][-<yL>]FI'])
    tree1.Add_Rule(['I', 'IFI'])
    tree1.Add_Rule(['P', '<r[++F][+F][F][-F][--F]>'])
    "----------------------------------------------------------------------------"
    tree2.Set_Base('F')
    tree2.Add_Rule(['F', ' <yF<g[+F]><yF[-F]>'])
    "---------------------------------------------------------------------------"
    tree3.Set_Base('X')
    tree3.Add_Rule(['X', 'F<g[+X][-X]>FX'])
    tree3.Add_Rule(['F', '<y>F'])
    "---------------------------------------------------------------------------"
    tree4.Set_Base('X')
    tree4.Add_Rule(['X', 'F-<g[[X]+X]+F[+FX]-X>'])
    tree4.Add_Rule(['F', 'FF'])
    "---------------------------------------------------------------------------"
    tree5.Set_Base('F')
    tree5.Add_Rule(['F', ' FF+[<y>+F-F-F]-[<g-F+F+F]>'])
    "----------------------------------------------------------------------------"
    terp = Turtle(800, 850)
    tree=[tree1,tree2,tree3,tree4,tree5]
    
    #' FF-[<y>-F+F+F]+[<g+F-F-F]>']
    
    for i in range(5):
    #x = 800
    #y = 450
    # create a turtle for drawing
    # number of trees
    
            z=[10,40,80,150,220]
            x0 = -800/3 + i*0.75*800/(6) + z[i]
            y0 = -300
            tstring = tree[i].Build_String(  random.randint( 3, 4 ) ) #4
            terp.color( (0.5, 0.4, 0.3 ) )
            terp.Place( x0, y0, random.randint( 89, 95 ) )
            terp.Draw_String(tstring, random.randint( 5, 7 ), random.randint( 18, 30 ) * random.choice( [1, -1] ) )
     
    
    
    terp.hold()
    
if __name__ == "__main__":
     main()
   