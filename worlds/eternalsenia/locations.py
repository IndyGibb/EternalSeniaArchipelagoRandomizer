from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import EternalSeniaWorld

# Every location must have a unique integer ID associated with it.
# We will have a lookup from location name to ID here that, in world.py, we will import and bind to the world class.
# Even if a location doesn't exist on specific options, it must be present in this lookup.
LOCATION_NAME_TO_ID = {
    "Entrance Big Armor/Violet Sword Broken": 1,
    "Two Handed Sword Pickup": 2,
    "Violet Armor Broken": 3,
    "Entrance Dragon Defeated": 4,
    "Warrior Armor Chest": 5,
    "Warrior Glove Chest": 6,
    "Warrior Cape Chest": 7,
    "Health Ring Chest": 8,
    "King Slime Defeated": 9,
    "Forest chest #1 Phantom Strike gap": 10,
    "Phantom Strike tutorial": 11,
    "King Evil Flower": 12,
    "Crafting Tutorial": 13,
    "Crafting Tutorial Done": 14,
    "Forest chest #2 Stepping Stones": 15,
    "Forest chest #3 Pink Flower": 16,
    "King Sunny Mushroom": 17,
    "Forest Facebook Admin": 18,
    "King Snake defeated": 19,
    "Forest cut down tree north": 20,
    "Forest cut down tree south": 21,
    "Forest chest #4 outside village": 22,
    "Little Fairy joins party": 23,
    "Forest chest #5 inside Village": 24,
    "Splash Leap Tutorial": 25,
    "Arcane Realm rare accessory chest": 26,
    "Medusa defeated": 27,
    "Forest chest #6 hidden in trees": 28,
    "King Dragon defeated": 29,
    "Forest Jack in the Chest": 30,
    "Forest Slimey Bounty 1": 31,
    "Forest Slimey Bounty 2": 32,
    "Forest Slimey Bounty 3": 33,
    "Forest Slimey Bounty 4": 34,
    "Forest Slimey All Bounties Reward": 35,
    "Forest Legendary Sheep": 36,
    "Fairy Queen defeated": 37,
    "Frontier chest #1 Fairy Gap": 38,
    "Frontier Facebook Admin": 39,
    "Elite Spell Caster": 40,
    "Frontier chest #2 Phantom Gap": 41,
    "Fairy Attack Tutorial": 42,
    "Frontier chest # 3 Destructible Wall": 43,
    "Winged Demon King": 44,
    "Frontier chest Passage of Bravery (#4-7)": 45,
    "Death Defeated": 46,
    "Frontier Wisdom chest #1 (#4-7)": 47,
    "Frontier Wisdom chest #2 (#4-7)": 48,
    "Succubus Celith Defeated": 49,
    "Little Fiary hole in wall chest (#4-7)": 50,
    "King Succubus": 51,
    "Force Realm rare acessory chest": 52,
    "Warlock defeated": 53,
    "Frontier encountered Mageleta": 54,
    "Frontier chest #8 Candle Puzzle": 55,
    "Frontier chest #9 Top of Tower": 56,
    "Sickle Ghost King": 57,
    "Frontier Jack in the Chest": 58,
    "Frontier Slimey Bounty 1": 59,
    "Frontier Slimey Bounty 2": 60,
    "Frontier Slimey Bounty 3": 61,
    "Frontier Slimey Bounty 4": 62,
    "Frontier Slimey All Bounties Reward": 63,
    "Frontier Legendary Sheep": 64,
    "Demon Lord defeated": 65,
    "Eternity Burst tutorial": 66,
    "Cross Pendant broken": 67,
    "Sanctum Facebook Admin": 68,
    "Sanctum Senia's Wardrobe Sword blueprint": 69,
    "Sanctum Senia's Wardrobe Armor blueprint": 70,
    "Sanctum Mageleta's Wardrobe": 71,
    "Sanctum Chapel Chest bottom right": 72,
    "Sanctum Chapel Chest top right": 73,
    "Sanctum Chapel chest top left": 74,
    "Sanctum chapel Piano played": 75,
    "High Sanctum Nun": 76,
    "Sanctum chest #5 past yellow barrier": 77,
    "Sanctum chest #6 Corridor": 78,
    "Dark Angel King": 79,
    "Sanctum Arcane Realm rare acessory chest": 80,
    "Micheal defeated": 81,
    "Sanctum chest #7 Confession 1": 82,
    "Elite Sanctum Knight": 83,
    "Sanctum chest #8 Confession 2": 84,
    "Sanctum chest #9 Holy Chamber": 85,
    "Cross Pendant repaired": 86,
    "Sanctum Jack in the Chest": 87,
    "Sanctum Legendary Sheep": 88,
    "Sanctum Slimey bounty 1": 89,
    "Sanctum Slimey bounty 2": 90,
    "Sanctum Slimey bounty 3": 91,
    "Sanctum Slimey bounty 4": 92,
    "Sanctum Slimey all bounties reward": 93,
    "Connection Test Chest": 94,
}


# Each Location instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Location class and override the "game" field.
class EternalSeniaLocation(Location):
    game = "Eternal Senia"


# Let's make one more helper method before we begin actually creating locations.
# Later on in the code, we'll want specific subsections of LOCATION_NAME_TO_ID.
# To reduce the chance of copy-paste errors writing something like {"Chest": LOCATION_NAME_TO_ID["Chest"]},
# let's make a helper method that takes a list of location names and returns them as a dict with their IDs.
# Note: There is a minor typing quirk here. Some functions want location addresses to be an "int | None",
# so while our function here only ever returns dict[str, int], we annotate it as dict[str, int | None].
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: EternalSeniaWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: EternalSeniaWorld) -> None:
    # Finally, we need to put the Locations ("checks") into their regions.
    # Once again, before we do anything, we can grab our regions we created by using world.get_region()
    tower_entrance = world.get_region("Tower Entrance")
    fairy_forest = world.get_region("Fairy Forest")
    demon_frontier = world.get_region("Demon Frontier")
    fallen_sanctum = world.get_region("Fallen Sanctum")
    holy_chamber = world.get_region("Holy Chamber")

    # One way to create locations is by just creating them directly via their constructor.
    # TODO: Remove once locations are done
    """bottom_left_chest = APQuestLocation(
        world.player, "Bottom Left Chest", world.location_name_to_id["Bottom Left Chest"], overworld
    )"""

    # You can then add them to the region.
    # TODO: Remove once locations are done
    # overworld.locations.append(bottom_left_chest)

    # A simpler way to do this is by using the region.add_locations helper.
    # For this, you need to have a dict of location names to their IDs (i.e. a subset of location_name_to_id)
    # Aha! So that's why we made that "get_location_names_with_ids" helper method earlier.
    # You also need to pass your overridden Location class.
    tower_entrance_locations = get_location_names_with_ids(
        [
            "Entrance Big Armor/Violet Sword Broken",
            "Two Handed Sword Pickup",
            "Violet Armor Broken",
            "Entrance Dragon Defeated",
            "Warrior Armor Chest",
            "Warrior Glove Chest",
            "Warrior Cape Chest",
            "Health Ring Chest",
            "King Slime Defeated",
        ]
    )
    tower_entrance.add_locations(tower_entrance_locations, EternalSeniaLocation)

    fairy_forest_locations = get_location_names_with_ids(
        [
            "Forest chest #1 Phantom Strike gap",
            "Phantom Strike tutorial",
            "King Evil Flower",
            "Crafting Tutorial",
            "Crafting Tutorial Done",
            "Forest chest #2 Stepping Stones",
            "Forest chest #3 Pink Flower",
            "King Sunny Mushroom",
            "Forest Facebook Admin",
            "King Snake defeated",
            "Forest cut down tree north",
            "Forest cut down tree south",
            "Forest chest #4 outside village",
            "Little Fairy joins party",
            "Forest chest #5 inside Village",
            "Splash Leap Tutorial",
            "Arcane Realm rare accessory chest",
            "Medusa defeated",
            "Forest chest #6 hidden in trees",
            "King Dragon defeated",
            "Forest Jack in the Chest",
            "Forest Slimey Bounty 1",
            "Forest Slimey Bounty 2",
            "Forest Slimey Bounty 3",
            "Forest Slimey Bounty 4",
            "Forest Slimey All Bounties Reward",
            "Forest Legendary Sheep",
            "Fairy Queen defeated",
        ]
    )
    fairy_forest.add_locations(fairy_forest_locations, EternalSeniaLocation)

    demon_frontier_locations = get_location_names_with_ids(
        [
            "Frontier chest #1 Fairy Gap",
            "Frontier Facebook Admin",
            "Elite Spell Caster",
            "Frontier chest #2 Phantom Gap",
            "Fairy Attack Tutorial",
            "Frontier chest # 3 Destructible Wall",
            "Winged Demon King",
            "Frontier chest Passage of Bravery (#4-7)",
            "Death Defeated",
            "Frontier Wisdom chest #1 (#4-7)",
            "Frontier Wisdom chest #2 (#4-7)",
            "Succubus Celith Defeated",
            "Little Fiary hole in wall chest (#4-7)",
            "King Succubus",
            "Force Realm rare acessory chest",
            "Warlock defeated",
            "Frontier encountered Mageleta",
            "Frontier chest #8 Candle Puzzle",
            "Frontier chest #9 Top of Tower",
            "Sickle Ghost King",
            "Frontier Jack in the Chest",
            "Frontier Slimey Bounty 1",
            "Frontier Slimey Bounty 2",
            "Frontier Slimey Bounty 3",
            "Frontier Slimey Bounty 4",
            "Frontier Slimey All Bounties Reward",
            "Frontier Legendary Sheep",
            "Demon Lord defeated",
            "Eternity Burst tutorial",
            "Cross Pendant broken",
        ]
    )
    demon_frontier.add_locations(demon_frontier_locations, EternalSeniaLocation)

    # Locations may be in different regions depending on the player's options.
    # In our case, the hammer option puts the Top Middle Chest into its own room called Top Middle Room.
    fallen_sanctum_locations = get_location_names_with_ids(
        [
            "Sanctum Facebook Admin",
            "Sanctum Senia's Wardrobe Sword blueprint",
            "Sanctum Senia's Wardrobe Armor blueprint",
            "Sanctum Mageleta's Wardrobe",
            "Sanctum Chapel Chest bottom right",
            "Sanctum Chapel Chest top right",
            "Sanctum Chapel chest top left",
            "Sanctum chapel Piano played",
            "High Sanctum Nun",
            "Sanctum chest #5 past yellow barrier",
            "Sanctum chest #6 Corridor",
            "Dark Angel King",
            "Sanctum Arcane Realm rare acessory chest",
            "Micheal defeated",
            "Sanctum chest #7 Confession 1",
            "Elite Sanctum Knight",
            "Sanctum chest #8 Confession 2",
            "Sanctum chest #9 Holy Chamber",
            "Cross Pendant repaired",
            "Sanctum Jack in the Chest",
            "Sanctum Legendary Sheep",
            "Sanctum Slimey bounty 1",
            "Sanctum Slimey bounty 2",
            "Sanctum Slimey bounty 3",
            "Sanctum Slimey bounty 4",
            "Sanctum Slimey all bounties reward",
            "Connection Test Chest",
        ]
    )
    """if world.options.hammer:
        top_middle_room = world.get_region("Top Middle Room")
        top_middle_room.add_locations(top_middle_room_locations, APQuestLocation)
    else:"""

    fallen_sanctum.add_locations(fallen_sanctum_locations, EternalSeniaLocation)


# TODO: Add optional locations
"""
    # Locations may exist only if the player enables certain options.
    # In our case, the extra_starting_chest option adds the Bottom Left Extra Chest location.
    if world.options.extra_starting_chest:
        # Once again, it is important to stress that even though the Bottom Left Extra Chest location doesn't always
        # exist, it must still always be present in the world's location_name_to_id.
        # Whether the location actually exists in the seed is purely determined by whether we create and add it here.
        bottom_left_extra_chest = get_location_names_with_ids(["Bottom Left Extra Chest"])
        overworld.add_locations(bottom_left_extra_chest, APQuestLocation)
"""

# TODO: Add any events
"""
def create_events(world: APQuestWorld) -> None:
    # Sometimes, the player may perform in-game actions that allow them to progress which are not related to Items.
    # In our case, the player must press a button in the top left room to open the final boss door.
    # AP has something for this purpose: "Event locations" and "Event items".
    # An event location is no different than a regular location, except it has the address "None".
    # It is treated during generation like any other location, but then it is discarded.
    # This location cannot be "sent" and its item cannot be "received", but the item can be used in logic rules.
    # Since we are creating more locations and adding them to regions, we need to grab those regions again first.
    top_left_room = world.get_region("Top Left Room")
    final_boss_room = world.get_region("Final Boss Room")

    # One way to create an event is simply to use one of the normal methods of creating a location.
    button_in_top_left_room = APQuestLocation(world.player, "Top Left Room Button", None, top_left_room)
    top_left_room.locations.append(button_in_top_left_room)

    # We then need to put an event item onto the location.
    # An event item is an item whose code is "None" (same as the event location's address),
    # and whose classification is "progression". Item creation will be discussed more in items.py.
    # Note: Usually, items are created in world.create_items(), which for us happens in items.py.
    # However, when the location of an item is known ahead of time (as is the case with an event location/item pair),
    # it is common practice to create the item when creating the location.
    # Since locations also have to be finalized after world.create_regions(), which runs before world.create_items(),
    # we'll create both the event location and the event item in our locations.py code.
    button_item = items.APQuestItem("Top Left Room Button Pressed", ItemClassification.progression, None, world.player)
    button_in_top_left_room.place_locked_item(button_item)

    # A way simpler way to do create an event location/item pair is by using the region.create_event helper.
    # Luckily, we have another event we want to create: The Victory event.
    # We will use this event to track whether the player can win the game.
    # The Victory event is a completely optional abstraction - This will be discussed more in set_rules().
    final_boss_room.add_event(
        "Final Boss Defeated", "Victory", location_type=APQuestLocation, item_type=items.APQuestItem
    )

    # If you create all your regions and locations line-by-line like this,
    # the length of your create_regions might get out of hand.
    # Many worlds use more data-driven approaches using dataclasses or NamedTuples.
    # However, it is worth understanding how the actual creation of regions and locations works,
    # That way, we're not just mindlessly copy-pasting! :)
    """
