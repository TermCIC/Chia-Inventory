import random
from library.character import *
from library.item_list import *

def assign_attribute(stats):
    if stats.weapon in Knife_list:
        stats.slash = 1
        stats.pierce = 1
    if stats.weapon in Sword_list:
        stats.slash = 2
        stats.bash = 1
    if stats.weapon in Short_Axe_list:
        stats.slash = 2
        stats.bash = 1
    if stats.weapon in Wood_Club_list:
        stats.bash = 2
    if stats.weapon in Short_Bow_list:
        stats.pierce = 2
    if stats.weapon in Catapult_list:
        stats.bash = 1
    if stats.weapon in Enhanced_Tree_Root_list:
        stats.pierce = 1
    if stats.weapon in Khopesh_list:
        stats.slash = 1
        stats.bash = 1
        stats.pierce = 1
    if stats.weapon in Red_Nuclei_Weapon_list:
        stats.str = stats.str + random.randint(1, 5)
    if stats.weapon in Orange_Nuclei_Weapon_list:
        stats.con = stats.con + random.randint(1, 5)
    if stats.weapon in Green_Nuclei_Weapon_list:
        stats.dex = stats.dex + random.randint(1, 5)
    if stats.weapon in Purple_Nuclei_Weapon_list:
        stats.wis = stats.wis + random.randint(1, 5)
    if stats.weapon in Shadow_Sword:
        stats.slash = 5
        stats.pierce = 1
        stats.magic = 3
    if stats.shield in Bark_Shield_list:
        stats.defense = 1
    if stats.mount in Deer_list:
        stats.dex = stats.dex + random.randint(1, 5)
    if stats.mount in Majestic_Deer_list:
        stats.str = stats.str + random.randint(1, 5)
    if stats.ring == "Nuclei Ring 01":
        stats.str = stats.str + random.randint(1, 5)
    if stats.ring == "Nuclei Ring 02":
        stats.dex = stats.dex + random.randint(1, 5)
    if stats.ring == "Nuclei Ring 03":
        stats.int = stats.int + random.randint(1, 5)
    if stats.ring == "Nuclei Ring 04":
        stats.con = stats.con + random.randint(1, 5)
    if stats.ring == "Nuclei Ring 05":
        stats.wis = stats.wis + random.randint(1, 5)
    if stats.herb in Brave_Seedling_list:
        stats.health = stats.health + random.randint(1, 5)
    if stats.herb in Powerful_Brave_Seedling_list:
        stats.health = stats.health + random.randint(1, 5)
    if stats.familiar in Chia_Slime_list:
        stats.str = stats.str + random.randint(1, 5) - random.randint(1, 5)
        stats.dex = stats.dex + random.randint(1, 5) - random.randint(1, 5)
        stats.int = stats.int + random.randint(1, 5) - random.randint(1, 5)
        stats.wis = stats.wis + random.randint(1, 5) - random.randint(1, 5)
        stats.cha = stats.cha + random.randint(1, 5) - random.randint(1, 5)
        stats.luc = stats.luc + random.randint(1, 5) - random.randint(1, 5)
    if stats.familiar in Healing_Chia_Slime_list:
        stats.health = stats.health + random.randint(1, 5)
    if stats.familiar in Identify_Chia_Slime_list:
        stats.int = stats.int + random.randint(1, 5)
    if stats.familiar in Snail_List:
        stats.dex = stats.dex - random.randint(1, 5)
        stats.luc = stats.luc + random.randint(1, 5)
    if stats.herb in Super_Powerful_Brave_Seedling_list:
        stats.con = stats.con + random.randint(1, 5)
    if stats.familiar in Hard_Snail_list:
        stats.con = stats.con + random.randint(1, 5)

    return stats
