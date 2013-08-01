import sys
from com.l2scoria.gameserver.model.quest import State
from com.l2scoria.gameserver.model.quest import QuestState
from com.l2scoria.gameserver.model.quest.jython import QuestJython as JQuest
from com.l2scoria.gameserver.datatables import SkillTable
from com.l2scoria.util.random import Rnd

qn = "8009_HotSpringsBuffs"

HSMOBS = [21316, 21317, 21321, 21322, 21314, 21319]

class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onAttack (self,npc,player,damage,isPet):
    npcId = npc.getNpcId()
    if npcId in HSMOBS:
      if (Rnd.get(2) == 1):
        if player.getFirstEffect(int(4554)):
          malaria = player.getFirstEffect(int(4554)).getLevel()
          if (Rnd.get(100) < 15):
            if malaria < 10:
              newmalaria = int(malaria + 1)
              npc.setTarget(player)
              npc.doCast(SkillTable.getInstance().getInfo(4554,newmalaria))
        else:
          npc.setTarget(player)
          npc.doCast(SkillTable.getInstance().getInfo(4554,1))
      elif npcId == 21317 or npcId == 21322 :
        if player.getFirstEffect(int(4553)):
          flu = player.getFirstEffect(int(4553)).getLevel()
          if (Rnd.get(100) < 15):
            if flu < 10:
              newflu = int(flu + 1)
              npc.setTarget(player)
              npc.doCast(SkillTable.getInstance().getInfo(4553,newflu))
        else:
          npc.setTarget(player)
          npc.doCast(SkillTable.getInstance().getInfo(4553,1))
      elif npcId == 21319 or npcId == 21316 :
        if player.getFirstEffect(int(4552)):
          holera = player.getFirstEffect(int(4552)).getLevel()
          if (Rnd.get(100) < 30):
            if holera < 10:
              newholera = int(holera + 1)
              npc.setTarget(player)
              npc.doCast(SkillTable.getInstance().getInfo(4552,newholera))
        else:
          npc.setTarget(player)
          npc.doCast(SkillTable.getInstance().getInfo(4552,1))
      else:
        if player.getFirstEffect(int(4551)):
          rheumatism = player.getFirstEffect(int(4551)).getLevel()
          if (Rnd.get(100) < 30):
            if rheumatism < 10:
              newrheumatism = int(rheumatism + 1)
              npc.setTarget(player)
              npc.doCast(SkillTable.getInstance().getInfo(4551,newrheumatism))
        else:
          npc.setTarget(player)
          npc.doCast(SkillTable.getInstance().getInfo(4551,1))
    return 

QUEST       = Quest(8009,qn,"custom")

for i in HSMOBS: 
  QUEST.addAttackId(i)