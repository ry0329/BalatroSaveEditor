import re
import json

def main():
    lua_str = '''j_joker=            {order = 1,  unlocked = true,   start_alerted = true, discovered = true,  blueprint_compat = true, perishable_compat = true, eternal_compat = true, rarity = 1, cost = 2, name = "Joker", pos = {x=0,y=0}, set = "Joker", effect = "Mult", cost_mult = 1.0, config = {mult = 4}},
    j_greedy_joker=     {order = 2,  unlocked = true,   discovered = false, blueprint_compat = true, perishable_compat = true, eternal_compat = true, rarity = 1, cost = 5, name = "Greedy Joker", pos = {x=6,y=1}, set = "Joker", effect = "Suit Mult", cost_mult = 1.0, config = {extra = {s_mult = 3, suit = 'Diamonds'}}},
    j_lusty_joker=      {order = 3,  unlocked = true,   discovered = false, blueprint_compat = true, perishable_compat = true, eternal_compat = true, rarity = 1, cost = 5, name = "Lusty Joker", pos = {x=7,y=1}, set = "Joker", effect = "Suit Mult", cost_mult = 1.0, config = {extra = {s_mult = 3, suit = 'Hearts'}}},
            '''
    
    lua_to_json(lua_str)

def lua_to_json(lua_str):
    # Replace Lua key-value pairs with JSON key-value pairs
    json_str = re.sub(r'\b(\w+)\s*=\s*', r'"\1": ', lua_str)
    print(json_str)

    json_str = json_str.replace("{", "{ ").replace("}", " }")
    print(json_str)

    json_str = re.sub(r'(\w+):', r'"\1":', json_str)
    print(json_str)


if __name__ == "__main__":
    main()