from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import EternalSeniaWorld

# A region is a container for locations ("checks"), which connects to other regions via "Entrance" objects.
# Many games will model their Regions after physical in-game places, but you can also have more abstract regions.
# For a location to be in logic, its containing region must be reachable.
# The Entrances connecting regions can have rules - more on that in rules.py.
# This makes regions especially useful for traversal logic ("Can the player reach this part of the map?")

# Every location must be inside a region, and you must have at least one region.
# This is why we create regions first, and then later we create the locations (in locations.py).


def create_and_connect_regions(world: EternalSeniaWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: EternalSeniaWorld) -> None:
    # Creating a region is as simple as calling the constructor of the Region class.
    tower_entrance = Region("Tower Entrance", world.player, world.multiworld)
    fairy_forest = Region("Fairy Forest", world.player, world.multiworld)
    demon_frontier = Region("Demon Frontier", world.player, world.multiworld)
    fallen_sanctum = Region("Fallen Sanctum", world.player, world.multiworld)
    holy_chamber = Region("Holy Chamber", world.player, world.multiworld)

    # Let's put all these regions in a list.
    regions = [tower_entrance, fairy_forest, demon_frontier, fallen_sanctum, holy_chamber]

    # Some regions may only exist if the player enables certain options.
    # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    # TODO:
    if world.options.hammer:
        top_middle_room = Region("Top Middle Room", world.player, world.multiworld)
        regions.append(top_middle_room)

    # We now need to add these regions to multiworld.regions so that AP knows about their existence.
    world.multiworld.regions += regions


# TODO: Add in region connections
def connect_regions(world: EternalSeniaWorld) -> None:
    # We have regions now, but still need to connect them to each other.
    # But wait, we no longer have access to the region variables we created in create_all_regions()!
    # Luckily, once you've submitted your regions to multiworld.regions,
    # you can get them at any time using world.get_region(...).
    tower_entrance = world.get_region("Tower Entrance")
    fairy_forest = world.get_region("Fairy Forest")
    demon_frontier = world.get_region("Demon Frontier")
    fallen_sanctum = world.get_region("Fallen Sanctum")
    holy_chamber = world.get_region("Holy Chamber")

    # Okay, now we can get connecting. For this, we need to create Entrances.
    # Entrances are inherently one-way, but crucially, AP assumes you can always return to the origin region.
    # One way to create an Entrance is by calling the Entrance constructor.
    tower_entrance_to_fairy_forest = Entrance(world.player, "Tower Entrance to Fairy Forest", parent=tower_entrance)
    tower_entrance.exits.append(tower_entrance_to_fairy_forest)

    # You can then connect the Entrance to the target region.
    tower_entrance_to_fairy_forest.connect(fairy_forest)

    # An even easier way is to use the region.connect helper.
    tower_entrance.connect(
        demon_frontier,
        "Tower Entrance to Demon Frontier",
    )
    tower_entrance.connect(
        fallen_sanctum,
        "Tower Entrance to Fallen Sanctum",
    )
    tower_entrance.connect(
        holy_chamber,
        "Tower Entrance to Holy Chamber",
    )

    # The region.connect helper even allows adding a rule immediately.
    # We'll talk more about rule creation in the set_all_rules() function in rules.py.

    # Some Entrances may only exist if the player enables certain options.
    # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    # In this case, we previously created an extra "Top Middle Room" region that we now need to connect to Overworld.
    # if world.options.hammer:
    #    top_middle_room = world.get_region("Top Middle Room")
    #    overworld.connect(top_middle_room, "Overworld to Top Middle Room")
