from . import CatalogItem
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.toon import ToonDNA
import random
from direct.showbase import PythonUtil
from direct.gui.DirectGui import *
from pandac.PandaModules import *

CTArticle = 0
CTString = 1
CTBasePrice = 2

ABoysShirt = 0
AGirlsShirt = 1
AShirt = 2
ABoysShorts = 3
AGirlsShorts = 4
AGirlsSkirt = 5
AShorts = 6


# These index numbers are written to the database.  Don't mess with them.
ClothingTypes = {
    # Basic boy's shirts (also available from Make-A-Toon)
    101 : (ABoysShirt, 'bss1', 40),
    102 : (ABoysShirt, 'bss2', 40),
    103 : (ABoysShirt, 'bss3', 40),
    105 : (ABoysShirt, 'bss4', 40),
    104 : (ABoysShirt, 'bss5', 40),
    106 : (ABoysShirt, 'bss6', 40),
    107 : (ABoysShirt, 'bss7', 40),
    108 : (ABoysShirt, 'bss8', 40),
    109 : (ABoysShirt, 'bss9', 40),
    111 : (ABoysShirt, 'bss11', 40),
    115 : (ABoysShirt, 'bss15', 40),
    # Catalog exclusive shirts are a bit pricier
    116 : (ABoysShirt, 'c_ss1', 80),   # Series 1
    117 : (ABoysShirt, 'c_ss2', 80),   # Series 1
    118 : (ABoysShirt, 'c_bss1', 80),  # Series 1
    119 : (ABoysShirt, 'c_bss2', 80),  # Series 1
    
    120 : (ABoysShirt, 'c_ss3', 80),   # Series 2
    121 : (ABoysShirt, 'c_bss3', 80),  # Series 2
    122 : (ABoysShirt, 'c_bss4', 80),  # Series 2

    123 : (ABoysShirt, 'c_ss4', 120),   # Series 3
    124 : (ABoysShirt, 'c_ss5', 120),   # Series 3
 
    125 : (AShirt, 'c_ss6', 120),   # Series 4
    126 : (AShirt, 'c_ss7', 120),   # Series 4
    127 : (AShirt, 'c_ss8', 120),   # Series 4
    128 : (AShirt, 'c_ss9', 120),   # Series 4
    129 : (AShirt, 'c_ss10', 120),   # Series 4
    130 : (AShirt, 'c_ss11', 120),   # Series 4
    
    131 : (ABoysShirt, 'c_ss12', 160),   # Series 7
    
    # Basic girl's shirts (also available from Make-A-Toon)
    201 : (AGirlsShirt, 'gss1', 40),
    202 : (AGirlsShirt, 'gss2', 40),
    203 : (AGirlsShirt, 'gss3', 40),
    205 : (AGirlsShirt, 'gss4', 40),
    204 : (AGirlsShirt, 'gss5', 40),
    206 : (AGirlsShirt, 'gss6', 40),
    207 : (AGirlsShirt, 'gss7', 40),
    208 : (AGirlsShirt, 'gss8', 40),
    209 : (AGirlsShirt, 'gss9', 40),
    211 : (AGirlsShirt, 'gss11', 40),
    215 : (AGirlsShirt, 'gss15', 40),
    
    # Catalog exclusive shirts are a bit pricier
    216 : (AGirlsShirt, 'c_ss1', 80),  # Series 1
    217 : (AGirlsShirt, 'c_ss2', 80),  # Series 1
    218 : (AGirlsShirt, 'c_gss1', 80), # Series 1
    219 : (AGirlsShirt, 'c_gss2', 80), # Series 1
    220 : (AGirlsShirt, 'c_ss3', 80),  # Series 2
    221 : (AGirlsShirt, 'c_gss3', 80), # Series 2
    222 : (AGirlsShirt, 'c_gss4', 80), # Series 2
    223 : (AGirlsShirt, 'c_gss5', 80), # UNUSED
    224 : (AGirlsShirt, 'c_ss4', 120), # Series 3
    225 : (AGirlsShirt, 'c_ss13', 160), # Series 7

    # Basic shorts for boys (available from Make-A-Toon)
    301 : (ABoysShorts, 'bbs1', 50),
    302 : (ABoysShorts, 'bbs2', 50),
    303 : (ABoysShorts, 'bbs3', 50),
    304 : (ABoysShorts, 'bbs4', 50),
    305 : (ABoysShorts, 'bbs5', 50),
    308 : (ABoysShorts, 'bbs8', 50),
    # Catalog exclusive shorts
    310 : (ABoysShorts, 'c_bs1', 120), # Series 3
    311 : (ABoysShorts, 'c_bs2', 120), # Series 3
    312 : (ABoysShorts, 'c_bs3', 120), # Series 4
    313 : (ABoysShorts, 'c_bs4', 120), # Series 4
    314 : (ABoysShorts, 'c_bs5', 160), # Series 7

    # Basic shorts/skirts for girls (available from Make-A-Toon)
    401 : (AGirlsSkirt, 'gsk1', 50),
    403 : (AGirlsSkirt, 'gsk3', 50),
    404 : (AGirlsSkirt, 'gsk4', 50),
    405 : (AGirlsSkirt, 'gsk5', 50),
    407 : (AGirlsSkirt, 'gsk7', 50),
    # Catalog exclusive skirts are a bit pricier
    408 : (AGirlsSkirt, 'c_gsk1', 100),
    409 : (AGirlsSkirt, 'c_gsk2', 100),
    410 : (AGirlsSkirt, 'c_gsk3', 100),
    411 : (AGirlsSkirt, 'c_gsk4', 120),
    412 : (AGirlsSkirt, 'c_gsk5', 120), # Series 4
    413 : (AGirlsSkirt, 'c_gsk6', 120), # Series 4
    414 : (AGirlsSkirt, 'c_gsk7', 160), # Series 7
    # Shorts
    451 : (AGirlsShorts, 'gsh1', 50),
    452 : (AGirlsShorts, 'gsh2', 50),
    453 : (AGirlsShorts, 'gsh3', 50),

    # Halloween-themed clothes.
    1001 : (AShirt, 'hw_ss1', 200),
    1002 : (AShirt, 'hw_ss2', 200),
    #disney why did you number these this way -facepalm-
    1112: (AShirt, 'hw_ss5', 200),
    1113: (AShirt, 'hw_ss6', 300),
    1114: (AShirt, 'hw_ss7', 200),
    1115: (AShirt, 'hw_ss8', 200),
    1116: (AShirt, 'hw_ss9', 300),
    1117: (ABoysShorts, 'hw_bs1', 200),
    1118: (ABoysShorts, 'hw_bs2', 300),
    1119: (ABoysShorts, 'hw_bs5', 200),
    1120: (ABoysShorts, 'hw_bs6', 200),
    1121: (ABoysShorts, 'hw_bs7', 300),
    1122: (AGirlsShorts, 'hw_gs1', 200),
    1123: (AGirlsShorts, 'hw_gs2', 300),
    1124: (AGirlsShorts, 'hw_gs5', 200),
    1125: (AGirlsShorts, 'hw_gs6', 200),
    1126: (AGirlsShorts, 'hw_gs7', 300),
    1127: (AGirlsSkirt, 'hw_gsk1', 300),
    # Winter Holiday clothes.
    1100 : (AShirt, 'wh_ss1', 200),
    1101 : (AShirt, 'wh_ss2', 200),
    1102 : (AShirt, 'wh_ss3', 200),
    1103 : (AShirt, 'wh_ss4', 200),
    1104 : (ABoysShorts, 'wh_bs1', 200),
    1105 : (ABoysShorts, 'wh_bs2', 200),
    1106 : (ABoysShorts, 'wh_bs3', 200),
    1107 : (ABoysShorts, 'wh_bs4', 200),
    1108 : (AGirlsSkirt, 'wh_gsk1', 200),
    1109 : (AGirlsSkirt, 'wh_gsk2', 200),
    1110 : (AGirlsSkirt, 'wh_gsk3', 200),
    1111 : (AGirlsSkirt, 'wh_gsk4', 200),

    # Valentines clothes.
    1200 : (AGirlsShirt, 'vd_ss1', 200),
    1201 : (AShirt, 'vd_ss2', 200),
    1202 : (ABoysShirt, 'vd_ss3', 200),
    1203 : (AGirlsShirt, 'vd_ss4', 200),
    1204 : (AGirlsSkirt, 'vd_gs1', 200),
    1205 : (ABoysShorts, 'vd_bs1', 200),
    1206 : (AShirt, 'vd_ss5', 200),
    1207 : (AShirt, 'vd_ss6', 200),
    1208 : (ABoysShorts, 'vd_bs2', 200),
    1209 : (ABoysShorts, 'vd_bs3', 200),
    1210 : (AGirlsSkirt, 'vd_gs2', 200),
    1211 : (AGirlsSkirt, 'vd_gs3', 200),
    1212 : (AShirt, 'vd_ss7', 200),
    # St. Patricks Day clothes
    1300 : (AShirt, 'sd_ss1', 200),
    1301 : (AShirt, 'sd_ss2', 225),
    1302 : (AGirlsShorts, 'sd_gs1', 200),
    1303 : (ABoysShorts, 'sd_bs1', 200),
    # T-Shirt Contest Shirts
    1400 : (AShirt, 'tc_ss1', 200),
    1401 : (AShirt, 'tc_ss2', 200),
    1402 : (AShirt, 'tc_ss3', 200),
    1403 : (AShirt, 'tc_ss4', 200),
    1404 : (AShirt, 'tc_ss5', 200),
    1405 : (AShirt, 'tc_ss6', 200),
    1406 : (AShirt, 'tc_ss7', 200),
    # July 4th clothes
    1500 : (AShirt, 'j4_ss1', 200),
    1501 : (AShirt, 'j4_ss2', 200),
    1502 : (ABoysShorts, 'j4_bs1', 200),
    1503 : (AGirlsSkirt, 'j4_gs1', 200),
    # Loyalty Gag Pajamas
    1600 : (AShirt, 'pj_ss1', 500),
    1601 : (AShirt, 'pj_ss2', 500),
    1602 : (AShirt, 'pj_ss3', 500),
    1603 : (ABoysShorts, 'pj_bs1', 500),
    1604 : (ABoysShorts, 'pj_bs2', 500),
    1605 : (ABoysShorts, 'pj_bs3', 500),
    1606 : (AGirlsShorts, 'pj_gs1', 500),
    1607 : (AGirlsShorts, 'pj_gs2', 500),
    1608 : (AGirlsShorts, 'pj_gs3', 500),
    # Special Award Clothes
    1700 : (AShirt, 'sa_ss1', 200),
    1701 : (AShirt, 'sa_ss2', 200),
    1702 : (AShirt, 'sa_ss3', 200),
    1703 : (AShirt, 'sa_ss4', 200),
    1704 : (AShirt, 'sa_ss5', 200),
    1705 : (AShirt, 'sa_ss6', 200),
    1706 : (AShirt, 'sa_ss7', 200),
    1707 : (AShirt, 'sa_ss8', 200),
    1708 : (AShirt, 'sa_ss9', 200),
    1709 : (AShirt, 'sa_ss10', 200),
    1710 : (AShirt, 'sa_ss11', 200),
    
    1711 : (ABoysShorts, 'sa_bs1', 200),
    1712 : (ABoysShorts, 'sa_bs2', 200),
    1713 : (ABoysShorts, 'sa_bs3', 200),
    1714 : (ABoysShorts, 'sa_bs4', 200),
    1715 : (ABoysShorts, 'sa_bs5', 200),
    
    1716 : (AGirlsSkirt, 'sa_gs1', 200),
    1717 : (AGirlsSkirt, 'sa_gs2', 200),
    1718 : (AGirlsSkirt, 'sa_gs3', 200),
    1719 : (AGirlsSkirt, 'sa_gs4', 200),
    1720 : (AGirlsSkirt, 'sa_gs5', 200),
    
    1721 : (AShirt, 'sa_ss12', 200),
    1722 : (AShirt, 'sa_ss13', 200),
    1723 : (AShirt, 'sa_ss14', 250),
    1724 : (AShirt, 'sa_ss15', 250),
    1725 : (AShirt, 'sa_ss16', 200),
    1726 : (AShirt, 'sa_ss17', 200),
    1727 : (AShirt, 'sa_ss18', 200),
    1728 : (AShirt, 'sa_ss19', 200),
    1729 : (AShirt, 'sa_ss20', 200),
    1730 : (AShirt, 'sa_ss21', 200),
    1731 : (AShirt, 'sa_ss22', 200),
    1732 : (AShirt, 'sa_ss23', 200),
    
    1733 : (ABoysShorts, 'sa_bs6', 200),
    1734 : (ABoysShorts, 'sa_bs7', 250),
    1735 : (ABoysShorts, 'sa_bs8', 250),
    1736 : (ABoysShorts, 'sa_bs9', 200),
    1737 : (ABoysShorts, 'sa_bs10', 200),
    
    1738 : (AGirlsSkirt, 'sa_gs6', 200),
    1739 : (AGirlsSkirt, 'sa_gs7', 250),
    1740 : (AGirlsSkirt, 'sa_gs8', 250),
    1741 : (AGirlsSkirt, 'sa_gs9', 200),
    1742 : (AGirlsSkirt, 'sa_gs10', 200),
    
    1743 : (AShirt, 'sa_ss24', 250),
    1744 : (AShirt, 'sa_ss25', 250),
    1745 : (ABoysShorts, 'sa_bs11', 250),
    1746 : (ABoysShorts, 'sa_bs12', 250),
    1747 : (AGirlsSkirt, 'sa_gs11', 250),
    1748 : (AGirlsSkirt, 'sa_gs12', 250),
    
    # I'm setting the cost of any Code Redemption clothing item to an obvious
    # 5000 jellybeans. They should never be offered for sale in the catalog. 
    # They should only be available through the code redemption system.
    1749 : (AShirt, 'sil_1', 1),      # Silly Mailbox Shirt
    1750 : (AShirt, 'sil_2', 1),      # Silly Trash Can Shirt
    1751 : (AShirt, 'sil_3', 1),         # Loony Labs Shirt
    1752 : (AShirt, 'sil_4', 5000),      # Silly Hydrant Shirt
    1753 : (AShirt, 'sil_5', 5000),      # Sillymeter Whistle Shirt
    1754 : (AShirt, 'sil_6', 1),      # Silly Cogbuster Shirt
    1755 : (ABoysShorts, 'sil_bs1', 1),     # Silly Cogbuster Shorts
    1756 : (AGirlsShorts, 'sil_gs1', 1),    # Silly Cogbuster Shorts
    1757 : (AShirt, 'sil_7', 20),      # Victory Party Shirt 1
    1758 : (AShirt, 'sil_8', 20),      # Victory Party Shirt 2
    
    1762 : (AShirt, 'sa_ss26', 200),
    1763: (AShirt, 'sb_1', 20),
    1764: (AShirt, 'sa_ss27', 5000),
    1765: (AShirt, 'sa_ss28', 5000),
    1766: (ABoysShorts, 'sa_bs13', 5000),
    1767: (AGirlsShorts, 'sa_gs13', 5000),
    1768: (AShirt, 'jb_1', 20),
    1769: (AShirt, 'jb_2', 20),
    1770: (AShirt, 'hw_ss3', 250),
    1771: (AShirt, 'hw_ss4', 250),
    1772: (ABoysShorts, 'hw_bs3', 250),
    1773: (AGirlsShorts, 'hw_gs3', 250),
    1774: (ABoysShorts, 'hw_bs4', 250),
    1775: (AGirlsShorts, 'hw_gs4', 250),
    1776: (AShirt, 'ugcms', 15000),
    1777: (AShirt, 'lb_1', 20),
    1778: (AShirt, 'sa_ss29', 5000),
    1779: (AShirt, 'sa_ss30', 5000),
    1780: (ABoysShorts, 'sa_bs14', 5000),
    1781: (AGirlsShorts, 'sa_gs14', 5000),
    1782: (AShirt, 'sa_ss31', 5000),
    1783: (ABoysShorts, 'sa_bs15', 5000),
    1784: (AGirlsSkirt, 'sa_gs15', 5000),
    1785: (AShirt, 'sa_ss32', 5000),
    1786: (AShirt, 'sa_ss33', 5000),
    1787: (AShirt, 'sa_ss34', 5000),
    1788: (AShirt, 'sa_ss35', 5000),
    1789: (AShirt, 'sa_ss36', 5000),
    1790: (AShirt, 'sa_ss37', 5000),
    1791: (ABoysShorts, 'sa_bs16', 5000),
    1792: (ABoysShorts, 'sa_bs17', 5000),
    1793: (AGirlsSkirt, 'sa_gs16', 5000),
    1794: (AGirlsSkirt, 'sa_gs17', 5000),
    1795: (AShirt, 'sa_ss38', 5000),
    1796: (AShirt, 'sa_ss39', 5000),
    1797: (ABoysShorts, 'sa_bs18', 5000),
    1798: (AGirlsSkirt, 'sa_gs18', 5000),
    1799: (AShirt, 'sa_ss40', 5000),
    1800: (AShirt, 'sa_ss41', 5000),
    1801: (AShirt, 'sa_ss42', 250),
    1802: (AGirlsShirt, 'sa_ss43', 250),
    1803: (AShirt, 'sa_ss44', 5000),
    1804: (AShirt, 'sa_ss45', 5000),
    1805: (AShirt, 'sa_ss46', 5000),
    1806: (AShirt, 'sa_ss47', 5000),
    1807: (AShirt, 'sa_ss48', 5000),
    1808: (AShirt, 'sa_ss49', 5000),
    1809: (AShirt, 'sa_ss50', 5000),
    1810: (AShirt, 'sa_ss51', 5000),
    1811: (AShirt, 'sa_ss52', 5000),
    1812: (AShirt, 'sa_ss53', 5000),
    1813: (AShirt, 'sa_ss54', 5000),
    1814: (ABoysShorts, 'sa_bs19', 5000),
    1815: (ABoysShorts, 'sa_bs20', 5000),
    1816: (ABoysShorts, 'sa_bs21', 5000),
    1817: (AGirlsSkirt, 'sa_gs19', 5000),
    1818: (AGirlsSkirt, 'sa_gs20', 5000),
    1819: (AGirlsSkirt, 'sa_gs21', 5000),
    1820: (AShirt, 'sa_ss55', 5000)
    }

# A list of clothes that are loyalty items, needed by award manager
LoyaltyClothingItems = ()

class CatalogClothingItem(CatalogItem.CatalogItem):
    """CatalogClothingItem

    This corresponds to an item of clothing, either a shirt or a
    bottom (shorts or skirt).  The clothingType indexes into the
    above map, which returns the appropriate clothing string for
    either a girl or a boy toon.

    """
    
    def makeNewItem(self, clothingType, colorIndex, special=False):
        self.clothingType = clothingType
        self.colorIndex = colorIndex
        #self.loyaltyDays = loyaltyDays
        self.special = special
        CatalogItem.CatalogItem.makeNewItem(self)

    def storedInCloset(self):
        # Returns true if this kind of item takes up space in the
        # avatar's closet, false otherwise.
        return 1

    def notOfferedTo(self, avatar):
        # Boys can only buy boy clothing, and girls can only buy girl
        # clothing.  Sorry.
        article = ClothingTypes[self.clothingType][CTArticle]

        if article == AShirt or article == AShorts:
            # This article is androgynous.
            return 0
            
        forBoys = (article == ABoysShirt or article == ABoysShorts)
        if avatar.getStyle().getGender() == 'm':
            return not forBoys
        else:
            return forBoys
            
    def forBoysOnly(self):
        article = ClothingTypes[self.clothingType][CTArticle]
        if (article == ABoysShirt or article == ABoysShorts):
            return 1
        else:
            return 0
            
    def forGirlsOnly(self):
        article = ClothingTypes[self.clothingType][CTArticle]
        if (article == AGirlsShirt or article == AGirlsSkirt or article == AGirlsShorts):
            return 1
        else:
            return 0
        

    def getPurchaseLimit(self):
        # Returns the maximum number of this particular item an avatar
        # may purchase.  This is either 0, 1, or some larger number; 0
        # stands for infinity.
        return 1

    def reachedPurchaseLimit(self, avatar):
        # Returns true if the item cannot be bought because the avatar
        # has already bought his limit on this item.

        if avatar.onOrder.count(self) != 0:
            # It's on the way.
            return 1
            
        if avatar.onGiftOrder.count(self) != 0:
            # someone has given it to you
            return 1

        if avatar.mailboxContents.count(self) != 0:
            # It's waiting in the mailbox.
            return 1

        if self in avatar.awardMailboxContents or self in avatar.onAwardOrder:
            # check award queue and award mailbox too
            return 1
        
        str = ClothingTypes[self.clothingType][CTString]

        dna = avatar.getStyle()
        if self.isShirt():
            # Check if the avatar is already wearing this shirt.
            defn = ToonDNA.ShirtStyles[str]
            if (dna.topTex == defn[0] and
                dna.topTexColor == defn[2][self.colorIndex][0] and
                dna.sleeveTex == defn[1] and
                dna.sleeveTexColor == defn[2][self.colorIndex][1]):
                return 1

            # Check if the shirt is in the avatar's closet.
            l = avatar.clothesTopsList
            for i in range(0, len(l), 4):
                if (l[i] == defn[0] and
                    l[i + 1] == defn[2][self.colorIndex][0] and
                    l[i + 2] == defn[1] and
                    l[i + 3] == defn[2][self.colorIndex][1]):
                    return 1
        else:
            # Check if the avatar is already wearing these shorts/skirt.
            defn = ToonDNA.BottomStyles[str]
            if (dna.botTex == defn[0] and
                dna.botTexColor == defn[1][self.colorIndex]):
                return 1

            # Check if the shorts/skirt is in the avatar's closet.
            l = avatar.clothesBottomsList
            for i in range(0, len(l), 2):
                if (l[i] == defn[0] and
                    l[i + 1] == defn[1][self.colorIndex]):
                    return 1

        # Not found anywhere; go ahead and buy it.
        return 0
            

    def getTypeName(self):
        # e.g. "shirt", "shorts", etc.
        #article = ClothingTypes[self.clothingType][CTArticle]
        #return TTLocalizer.ClothingArticleNames[article]

        # Until we have descriptive names per-item below, just return
        # "Clothing" here.
        return TTLocalizer.ClothingTypeName

    def getName(self):
        typeName = TTLocalizer.ClothingTypeNames.get(self.clothingType, 0)
        # check for a specific item name
        if typeName:
            return typeName
        # otherwise use a generic name
        else:
            article = ClothingTypes[self.clothingType][CTArticle]
            return TTLocalizer.ClothingArticleNames[article]

    def recordPurchase(self, avatar, optional):
        # Updates the appropriate field on the avatar to indicate the
        # purchase (or delivery).  This makes the item available to
        # use by the avatar.  This method is only called on the AI side.

        if avatar.isClosetFull():
            return ToontownGlobals.P_NoRoomForItem

        str = ClothingTypes[self.clothingType][CTString]

        # Save the avatar's current clothes in his closet.
        dna = avatar.getStyle()
        if self.isShirt():
            added = avatar.addToClothesTopsList(dna.topTex, dna.topTexColor, 
                                                dna.sleeveTex, dna.sleeveTexColor)
            if added:
                avatar.b_setClothesTopsList(avatar.getClothesTopsList())
                self.notify.info('Avatar %s put shirt %d,%d,%d,%d in closet.' % (avatar.doId,
                                                                                 dna.topTex, dna.topTexColor, 
                                                                                 dna.sleeveTex, dna.sleeveTexColor))
            else:
                self.notify.warning('Avatar %s %s lost current shirt; closet full.' % (avatar.doId, dna.asTuple()))

            defn = ToonDNA.ShirtStyles[str]
            dna.topTex = defn[0]
            dna.topTexColor = defn[2][self.colorIndex][0]
            dna.sleeveTex = defn[1]
            dna.sleeveTexColor = defn[2][self.colorIndex][1]

        else:
            added = avatar.addToClothesBottomsList(dna.botTex, dna.botTexColor)
            if added:
                avatar.b_setClothesBottomsList(avatar.getClothesBottomsList())
                self.notify.info('Avatar %s put bottoms %d,%d in closet.' % (avatar.doId,
                                                                             dna.botTex, dna.botTexColor))
            else:
                self.notify.warning('Avatar %s %s lost current bottoms; closet full.' % (avatar.doId, dna.asTuple()))

            defn = ToonDNA.BottomStyles[str]
            dna.botTex = defn[0]
            dna.botTexColor = defn[1][self.colorIndex]

        # Store the new clothes on the avatar.
        avatar.b_setDNAString(dna.makeNetString())
        # need to call this to make sure generateToonClothes is called on client
        avatar.d_catalogGenClothes()
        return ToontownGlobals.P_ItemAvailable

    def getDeliveryTime(self):
        # Returns the elapsed time in minutes from purchase to
        # delivery for this particular item.
        return 60  # 1 hour.

    def getPicture(self, avatar):
        # Returns a (DirectWidget, Interval) pair to draw and animate a
        # little representation of the item, or (None, None) if the
        # item has no representation.  This method is only called on
        # the client.

        # Don't import this at the top of the file, since this code
        # must run on the AI.
        from toontown.toon import Toon

        #assert (not self.hasPicture)
        self.hasPicture=True

        # Make an ToonDNA suitable for showing this clothing.
        # First, we start with a copy of the avatar's dna.
        dna = ToonDNA.ToonDNA(type = 't', dna = avatar.style)

        # Now we apply the properties from this clothing.
        str = ClothingTypes[self.clothingType][CTString]

        if self.isShirt():
            # It's a shirt.
            defn = ToonDNA.ShirtStyles[str]
            dna.topTex = defn[0]
            dna.topTexColor = defn[2][self.colorIndex][0]
            dna.sleeveTex = defn[1]
            dna.sleeveTexColor = defn[2][self.colorIndex][1]
            pieceNames = ('**/1000/**/torso-top', '**/1000/**/sleeves')
        else:
            # It's a skirt or shorts.
            defn = ToonDNA.BottomStyles[str]
            dna.botTex = defn[0]
            dna.botTexColor = defn[1][self.colorIndex]
            pieceNames = ('**/1000/**/torso-bot',)

        # Create a toon wearing the clothing, then pull out the
        # appropriate clothes and throw the rest away.
        toon = Toon.Toon()
        toon.setDNA(dna)
        
        model = NodePath('clothing')

        for name in pieceNames:
            for piece in toon.findAllMatches(name):
                piece.wrtReparentTo(model)
        
        model.setH(180)

        toon.delete()
        
        
        return self.makeFrameModel(model)

    def requestPurchase(self, phone, callback):
        # Orders the item via the indicated telephone.  Some items
        # will pop up a dialog querying the user for more information
        # before placing the order; other items will order
        # immediately.

        # In either case, the function will return immediately before
        # the transaction is finished, but the given callback will be
        # called later with two parameters: the return code (one of
        # the P_* symbols defined in ToontownGlobals.py), followed by the
        # item itself.

        # This method is only called on the client.
        from toontown.toontowngui import TTDialog
        avatar = base.localAvatar

        clothesOnOrder = 0
        for item in avatar.onOrder + avatar.mailboxContents:
            if item.storedInCloset():
                clothesOnOrder += 1
        
        if avatar.isClosetFull(clothesOnOrder):
            # If the avatar's closet is full, pop up a dialog warning
            # the user, and give him a chance to bail out.
            self.requestPurchaseCleanup()
            buttonCallback = PythonUtil.Functor(
                self.__handleFullPurchaseDialog, phone, callback)
            self.dialog = TTDialog.TTDialog(
                style = TTDialog.YesNo,
                text = TTLocalizer.CatalogPurchaseClosetFull,
                text_wordwrap = 15,
                command = buttonCallback,
                )
            self.dialog.show()

        else:
            # The avatar's closet isn't full; just buy it.
            CatalogItem.CatalogItem.requestPurchase(self, phone, callback)

    def requestPurchaseCleanup(self):
        if hasattr(self, "dialog"):
            self.dialog.cleanup()
            del self.dialog

    def __handleFullPurchaseDialog(self, phone, callback, buttonValue):
        from toontown.toontowngui import TTDialog
        self.requestPurchaseCleanup()
        if buttonValue == DGG.DIALOG_OK:
            # Go ahead and purchase it.
            CatalogItem.CatalogItem.requestPurchase(self, phone, callback)
        else:
            # Don't purchase it.
            callback(ToontownGlobals.P_UserCancelled, self)

    def getAcceptItemErrorText(self, retcode):
        # Returns a string describing the error that occurred on
        # attempting to accept the item from the mailbox.  The input
        # parameter is the retcode returned by recordPurchase() or by
        # mailbox.acceptItem().
        if retcode == ToontownGlobals.P_ItemAvailable:
            if self.isShirt():
                return TTLocalizer.CatalogAcceptShirt
            elif self.isSkirt():
                return TTLocalizer.CatalogAcceptSkirt
            else:
                return TTLocalizer.CatalogAcceptShorts
        elif retcode == ToontownGlobals.P_NoRoomForItem:
            return TTLocalizer.CatalogAcceptClosetFull
        return CatalogItem.CatalogItem.getAcceptItemErrorText(self, retcode)
    

    def getColorChoices(self):
        # Returns the list from ToonDNA that defines the clothing
        # item and its color options.
        str = ClothingTypes[self.clothingType][CTString]

        if self.isShirt():
            # It's a shirt.
            return ToonDNA.ShirtStyles[str][2]
        else:
            # It's a skirt or shorts.
            return ToonDNA.BottomStyles[str][1]

    def isShirt(self):
        # Returns true if the article is a shirt, false if it is a
        # pair of shorts or a skirt.
        article = ClothingTypes[self.clothingType][CTArticle]
        return article < ABoysShorts

    def isSkirt(self):
        # Returns true if the article is a skirt, false if it is a
        # pair of shorts or a shirt.
        article = ClothingTypes[self.clothingType][CTArticle]
        return article == AGirlsSkirt

    def output(self, store = ~0):
        return "CatalogClothingItem(%s, %s%s)" % (
            self.clothingType, self.colorIndex,
            self.formatOptionalData(store))

    def getFilename(self):
        str = ClothingTypes[self.clothingType][CTString]
        if self.isShirt():
            # It's a shirt.
            defn = ToonDNA.ShirtStyles[str]
            topTex = defn[0]
            return ToonDNA.Shirts[topTex]
        else:
            # It's a skirt or shorts.
            defn = ToonDNA.BottomStyles[str]
            botTex = defn[0]
            article = ClothingTypes[self.clothingType][CTArticle]
            if article == ABoysShorts:
                return ToonDNA.BoyShorts[botTex]
            else:
                return ToonDNA.GirlBottoms[botTex][0]

    def getColor(self):
        str = ClothingTypes[self.clothingType][CTString]
        if self.isShirt():
            # It's a shirt.
            defn = ToonDNA.ShirtStyles[str]
            topTexColor = defn[2][self.colorIndex][0]
            return ToonDNA.ClothesColors[topTexColor]
        else:
            # It's a skirt or shorts.
            defn = ToonDNA.BottomStyles[str]
            botTexColor = defn[1][self.colorIndex]
            return ToonDNA.ClothesColors[botTexColor]


    def compareTo(self, other):
        if self.clothingType != other.clothingType:
            return self.clothingType - other.clothingType
        return self.colorIndex - other.colorIndex

    def getHashContents(self):
        return (self.clothingType, self.colorIndex)

    def getBasePrice(self):
        return ClothingTypes[self.clothingType][CTBasePrice]

    def decodeDatagram(self, di, versionNumber, store):
        CatalogItem.CatalogItem.decodeDatagram(self, di, versionNumber, store)
        self.clothingType = di.getUint16()
        self.colorIndex = di.getUint8()
        self.special = di.getBool()
        #if versionNumber >= 6:
            #self.loyaltyDays = di.getUint16()
        #else:
            #RAU this seeems safe, as an old user would never have the new loyalty items
            #self.loyaltyDays = 0

        # Now validate the indices by assigning into a variable,
        # color, which we don't care about other than to prove the
        # clothingType and colorIndex map to a valid definition.  If
        # they don't, the following will raise an exception.
        str = ClothingTypes[self.clothingType][CTString]
        if self.isShirt():
            color = ToonDNA.ShirtStyles[str][2][self.colorIndex]
        else:
            color = ToonDNA.BottomStyles[str][1][self.colorIndex]
        
    def encodeDatagram(self, dg, store):
        CatalogItem.CatalogItem.encodeDatagram(self, dg, store)
        dg.addUint16(self.clothingType)
        dg.addUint8(self.colorIndex)
        dg.addBool(self.special)
        #dg.addUint16(self.loyaltyDays)
        
    def isGift(self):
        return 1

def getAllClothes(*clothingTypes):
    # This function returns a list of all possible
    # CatalogClothingItems (that is, all color variants) for the
    # indicated type index(es).

    _list = []
    for clothingType in clothingTypes:
        base = CatalogClothingItem(clothingType, 0)

        _list.append(base)
        for n in range(1, len(base.getColorChoices())):
            _list.append(CatalogClothingItem(clothingType, n))

    return _list
    
