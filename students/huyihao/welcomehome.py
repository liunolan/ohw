from mcpi.minecraft import Minecraft
import time
import mcpi

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)

stayed_time=0

mc = Minecraft.create()
pos = mc.player.getTilePos()

for i in range(11):
    for y in range(6):
        mc.setBlock(pos.x,pos.y+y,pos.z+i,1)
        mc.setBlock(pos.x+10,pos.y+y,pos.z+i,1)
        mc.setBlock(pos.x+i,pos.y+y,pos.z,1)
        mc.setBlock(pos.x+i,pos.y+y,pos.z+10,1)
        
for i in range(1):
    for y in range(3):
        mc.setBlock(pos.x+5+i,pos.y+y,pos.z,0)

for i in range(2):
    for y in range(2):
        mc.setBlock(pos.x,pos.y+2+y,pos.z+1+i,20)

for y in range(5):
    for i in range(11-2*y):
        mc.setBlock(pos.x+y,pos.y+6+y,pos.z+y+i,1)
        mc.setBlock(pos.x+10-y,pos.y+6+y,pos.z+y+i,1)
        mc.setBlock(pos.x+y+i,pos.y+6+y,pos.z+y,1)
        mc.setBlock(pos.x+y+i,pos.y+6+y,pos.z+10-y,1)


while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home x=-30 y=-6 z=-40 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    if pos.x==-30 and pos.y==-6 and pos.z==-40:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=30:
            mc.player.setTilePos(-30,10,-40)
            stayed_time=0
    else:
        stayed_time=0
        
     