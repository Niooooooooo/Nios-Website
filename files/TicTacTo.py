G = " "
symbol = "x"
grid = [[G,G,G],                                        
        [G,G,G],
        [G,G,G]]
coords_table = ["0,0","1,0","2,0","0,1","1,1","2,1","0,2","1,2","2,2"]        
        
print()
print("----------")
for i in range(3):
  print(G+G+G)
print("----------")

while True:
    
 ans = ""

 #Input Coords
 field = int(input("Feld:"))
 coords = coords_table[field-1].split(",")
 x = int(coords[0])
 y = int(coords[1])
 grid[x][y] = symbol 

 #Print grid
 print()
 print("----------")
 for i in range(3):
   for j in range(3):
     ans = ans+grid[j][i]
   print(ans)
   ans = ""  
 print("----------")
 
 #Symbol Switch
 if symbol == "x":
   symbol = "o"
 else:
   symbol = "x"

 #Horizontal Check     
 for row in range(3):  
   win_xh = 0 
   win_oh = 0                                                                                                  
   for col in range(3):                                                                                           
     if grid[col][row] == "x":                                                                                      
       win_xh += 1
     else:
       win_xh = 0  
     if win_xh == 3:
       break   
     if grid[col][row] == "o":                                                                                     
       win_oh += 1
     else:
       win_oh = 0  
     if win_oh == 3:
       break   
   if win_xh == 3:
     break                                                                            
   if win_oh == 3:
     break   
  
 #Vertical Check
 for col in range(3):  
   win_xv = 0 
   win_ov = 0                                                                                                  
   for row in range(3):                                                                                         
     if grid[col][row] == "x":                        
       win_xv += 1                                                                    
     else:
       win_xv = 0  
     if win_xv == 3:
       break   
     if grid[col][row] == "o":                                                                                     
       win_ov += 1
     else:
       win_ov = 0  
     if win_ov == 3:
       break
   if win_xv == 3:
     break   
   if win_ov == 3:
     break  

 #Check Diagonal                   
 if (grid[0][0] == "x") and (grid[1][1] == "x") and (grid [2][2] == "x"):
   print("x Won!")
   break
 if (grid[2][0] == "x") and (grid[1][1] == "x") and (grid [0][2] == "x"):
   print("x Won!")
   break

 if (grid[0][0] == "o") and (grid[1][1] == "o") and (grid [2][2] == "o"):
   print("o Won!")
   break
 if (grid[2][0] == "o") and (grid[1][1] == "o") and (grid [0][2] == "o"):
   print("o Win!")
   break

 #Print Winner
 if win_xh == 3:
   print("x Won!")
   break
 if win_xv == 3:
   print("x Won!")
   break
     
 if win_oh == 3:
   print("o Won!")
   break
 if win_ov == 3:
   print("o Won!")
   break 