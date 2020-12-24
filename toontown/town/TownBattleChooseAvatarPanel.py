from toontown.toonbase.ToontownBattleGlobals import *
from toontown.toonbase import ToontownGlobals
from direct.fsm import StateData
from direct.directnotify import DirectNotifyGlobal
from toontown.battle import BattleBase
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from toontown.toonbase import TTLocalizer

class TownBattleChooseAvatarPanel(StateData.StateData):
    """TownBattleChooseAvatarPanel
    This is the panel used for choosing a avatar to attack.
    """
    notify = DirectNotifyGlobal.directNotify.newCategory('ChooseAvatarPanel')

    def __init__(self, doneEvent, toon):
        self.notify.debug("Init choose panel...")
        StateData.StateData.__init__(self, doneEvent)
        # How many avatars in the battle?
        self.numAvatars = 0
        # Which was picked?
        self.chosenAvatar = 0
        # Is this for toons? (or suits?)
        self.toon = toon
        return

    def load(self):
        gui = loader.loadModel("phase_3.5/models/gui/battle_gui")
        self.frame = DirectFrame(
            relief = None,
            image = gui.find("**/BtlPick_TAB"),
            image_color = Vec4(1,0.2,0.2,1),
            )
        self.frame.hide()

        self.statusFrame = DirectFrame(
            parent = self.frame,
            relief = None,
            image = gui.find("**/ToonBtl_Status_BG"),
            image_color = Vec4(0.5,0.9,0.5,1),
            pos = (0.611, 0, 0),
            )
        
        self.textFrame = DirectFrame(
            parent = self.frame,
            relief = None,
            image = gui.find("**/PckMn_Select_Tab"),
            image_color = Vec4(1,1,0,1),
            text = "",
            text_fg = Vec4(0,0,0,1),
            text_pos = (0,-0.025,0),
            text_scale = 0.08,
            pos = (-0.013, 0, 0.013),
            )
        if self.toon:
            self.textFrame['text'] = TTLocalizer.TownBattleChooseAvatarToonTitle
        else:
            self.textFrame['text'] = TTLocalizer.TownBattleChooseAvatarCogTitle
            
        self.avatarButtons = []
        for i in range(4):
            button = DirectButton(
                parent = self.frame,
                relief = None,
                image = (gui.find("**/PckMn_Arrow_Up"),
                         gui.find("**/PckMn_Arrow_Dn"),
                         gui.find("**/PckMn_Arrow_Rlvr")),
                command = self.__handleAvatar,
                extraArgs = [i],
                )
            if self.toon:
                button.setScale(1,1,-1)
                button.setPos(0,0,-0.2)
            else:
                button.setScale(1,1,1)
                button.setPos(0,0,0.2)
            self.avatarButtons.append(button)
        
        self.backButton = DirectButton(
            parent = self.frame,
            relief = None,
            image = (gui.find("**/PckMn_BackBtn"),
                     gui.find("**/PckMn_BackBtn_Dn"),
                     gui.find("**/PckMn_BackBtn_Rlvr")),
            pos = (-0.647, 0, 0.006),
            scale = 1.05,
            text = TTLocalizer.TownBattleChooseAvatarBack,
            text_scale = 0.05,
            text_pos = (0.01,-0.012),
            text_fg = Vec4(0,0,0.8,1),
            command = self.__handleBack,
            )

        gui.removeNode()

        return

    def unload(self):
        """unload(self)
        """
        self.frame.destroy()
        del self.frame
        del self.statusFrame
        del self.textFrame
        del self.avatarButtons
        del self.backButton
        return

    def enter(self, numAvatars, localNum=None, luredIndices=None, trappedIndices=None, track=None):
        # Show the panel
        self.frame.show()
        # Place the buttons
        # Suits that are lured should not be available to select for
        # certain attacks
        invalidTargets = []
        if not self.toon:
            if (len(luredIndices) > 0):
                # You can't place a trap in front of a suit that is already lured
                if (track == BattleBase.TRAP or track == BattleBase.LURE): 
                    invalidTargets += luredIndices
            if (len(trappedIndices) > 0):
                # You can't place a trap in front of a suit that is already trapped
                if (track == BattleBase.TRAP):
                    invalidTargets += trappedIndices
        self.__placeButtons(numAvatars, invalidTargets, localNum)
        # Force chat balloons to the margins while this is up.
        # NametagGlobals.setOnscreenChatForced(1)
        return

    def exit(self):
        # Hide the panel
        self.frame.hide()
        # NametagGlobals.setOnscreenChatForced(0)
        return

    def __handleBack(self):
        doneStatus = {'mode' : 'Back'}
        messenger.send(self.doneEvent, [doneStatus])
        return
    
    def __handleAvatar(self, avatar):
        doneStatus = {'mode' : 'Avatar',
                      'avatar' : avatar}
        messenger.send(self.doneEvent, [doneStatus])
        return

    def adjustCogs(self, numAvatars, luredIndices, trappedIndices, track):
        # Suits that are lured should not be available to select for
        # certain attacks
        invalidTargets = []
        if (len(luredIndices) > 0):
            # You can't place a trap in front of a suit that is already lured
            if (track == BattleBase.TRAP or track == BattleBase.LURE): 
                invalidTargets += luredIndices
        if (len(trappedIndices) > 0):
            # You can't place a trap in front of a suit that is already trapped
            if (track == BattleBase.TRAP):
                invalidTargets += trappedIndices
        self.__placeButtons(numAvatars, invalidTargets, None)
        return

    def adjustToons(self, numToons, localNum):
        self.__placeButtons(numToons, [], localNum)
        return

    def __placeButtons(self, numAvatars, invalidTargets, localNum):
        # Place the buttons. NOTE: Remember, from the toons point of view
        # the avatars are numbered from right to left.
        for i in range(4):
            # Only show the button if this avatar is in the battle
            # and he is not in the invalidTargets list
            if ((numAvatars > i) and (i not in invalidTargets) and (i != localNum)):
                self.avatarButtons[i].show()
            else:
                self.avatarButtons[i].hide()

        # Evenly positions the buttons on the bar
        if numAvatars == 1:
            self.avatarButtons[0].setX(0)
        elif numAvatars == 2:
            self.avatarButtons[0].setX(0.2)
            self.avatarButtons[1].setX(-0.2)
        elif numAvatars == 3:
            self.avatarButtons[0].setX(0.4)
            self.avatarButtons[1].setX(0.0)
            self.avatarButtons[2].setX(-0.4)
        elif numAvatars == 4:
            self.avatarButtons[0].setX(0.6)
            self.avatarButtons[1].setX(0.2)
            self.avatarButtons[2].setX(-0.2)
            self.avatarButtons[3].setX(-0.6)
        else:
            self.notify.error("Invalid number of avatars: %s" % numAvatars)

        return None

    
