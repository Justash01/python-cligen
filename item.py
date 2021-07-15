from typing import Collection
from pathlib import Path
import json
import os
identifier = input("Identifier:")
displayName = input("Display Name:")
cooldownDur = float(input("Cooldown Duration:"))

itemID = identifier.split(":", 2)
mainPath = 'output'
folder = itemID[1]
path = os.path.join(mainPath, folder)
Path(path).mkdir(parents=True, exist_ok=True)

itemFileName = '{0}.json'.format(itemID[1])
item = os.path.join(path, itemFileName)

f = open(item, "a")
itemJSON = {
    "format_version": "1.16.100",
    "minecraft:item": {
        "description": {
            "identifier": "{}".format(identifier),
            "category": "items"
        },
        "components": {
            "minecraft:icon": {
                "texture": "{}.texture".format(itemID[1])
            },
            "minecraft:display_name": {
                "value": "{0}.{1}".format(itemID[0], itemID[1])
            },
            "minecraft:max_stack_size": 1,
            "minecraft:use_duration": 999999999,
            "minecraft:stacked_by_data": True,
            "minecraft:hand_equipped": True,
            "minecraft:creative_category": {
                "parent": "itemGroup.name.tools"
            },
            "minecraft:food": {
                "can_always_eat": True
            },
            "minecraft:cooldown": {
                "category": "{}".format(itemID[0]),
                "duration": cooldownDur
            },
            "minecraft:render_offsets": {
                "main_hand": {
                    "first_person": {
                        "scale": [
                            0,
                            0,
                            0
                        ]
                    },
                    "third_person": {
                        "scale": [
                            0,
                            0,
                            0
                        ]
                    }
                }
            }
        }
    }
}
f.write(json.dumps(itemJSON, indent=2))
f.close()
print('Item files were successfully created.')

textPath = 'output'
textFile = 'en_US.lang'
textPathFul = os.path.join(path, textFile)
f = open(textPathFul, "a")
f.write('{0}.{1}={2}\n'.format(itemID[0], itemID[1], displayName))
f.close()
