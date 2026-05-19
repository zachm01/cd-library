import os
import sys
import json

discs = []

for disc in os.listdir("discs"):
    try:
        with open(f"discs/{disc}", "r", encoding="utf8") as f:
            discs.append(json.load(f))
    except Exception as exc:
        print(f"Failed to load {disc}")
        print(exc)
        

def get_next_id():
    """
    Returns the next available integer ID
    """
    highest_id = -1;
    for disc_obj in discs:
        if disc_obj['id'] > highest_id:
            highest_id = disc_obj['id']
    return highest_id + 1

def get_every_artist():
    """
    Returns a sorted list containing every artist (soloist, conductor, composer, orchestra, etc.)
    that appears in the database
    """
    artists = set()
    
    for disc in discs:
        for artist in disc.get("all artists"):
            artists.add(artist)
    
    return sorted(list(artists))

def remove_file_field(field_name):
    """
    Removes `field` from every entry in the database
    This is an irreversible action
    """
    for disc_obj in discs:
        disc_obj.remove(field_name)
    for d, disc_obj in os.listdir("discs"), discs:
        with open(f"discs/{d}", "w", encoding="utf8") as f:
            json.dump(disc_obj, f)
            

def add_file_field(field_name: str):
    """
    Adds `field` to every entry in the database
    """
    for disc_obj in discs:
        disc_obj.update({ field_name: ""})
    for d, disc_obj in os.listdir("discs"), discs:
        with open(f"discs/{d}", "w", encoding="utf8") as f:
            json.dump(disc_obj, f)

def add_piece_field(field_name: str):
    """
    Adds `field` to every piece in every entry in the database
    """
    for disc_obj in discs:
        # for every disc in an entry
        for d in disc_obj['discs']:
            # for every piece on a disc
            for p in d['pieces']:
                p.update({field_name: ""})
                
    for i in range(len(discs)):
        fpaths = os.listdir("discs")
        with open(f"discs/{fpaths[i]}", "w", encoding="utf8") as f:
            json.dump(discs[i], f)
            
def print_help_message():
    print(
        """Please provide one of the following options:
  -aff \"field\"    Add the supplied field name mapping to an empty string to every file
  -apf \"field\"    Add the supplied field name mapping to an empty string to every piece in every file
  -rff \"field\"    Remove the supplied field name from every file
  -gea            Get a list of all artists in the library
  -geax path?     Get a list of all artists in the library and export as a JSON file
  -gni            Retrieve the highest index of a file in the library + 1
  -h              Display this message""")

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print_help_message()
        sys.exit()
    arguments = sys.argv[1:] if len(sys.argv) > 1 else list()
    
    match arguments[0]:
        case "-aff": # Add File Field
            try:
                add_file_field(arguments[1])
                print(f"Added the field {arguments[1]} to {len(discs)} files")
            except IndexError as _:
                print("Please provide a field to add to every file")
        case "-apf": # Add Piece Field
            try:
                add_file_field(arguments[1])
                num_pieces = sum([len(disc_obj["pieces"]) for disc_obj in discs])
                print(f"Added the field {arguments[1]} to {num_pieces} pieces accross {len(discs)} files")
            except IndexError as _:
                print("Please provide a field to add to every piece of every file")
        case "-rff": # Remove File Field
            try:
                remove_file_field(arguments[1])
                print(f"Irreversibly removed the field {arguments[1]} from {len(discs)} files")
            except IndexError as _:
                print("Please provide a field to remove from every file")
        case "-gea": # Get Every Artist
            artists = get_every_artist()
            for a in artists: print(a)
        case "-geax": # Get Every Artist and eXport
            artists = get_every_artist()
            obj = { "artists": artists }
            json_str = json.dumps(obj, indent = 4)
            with open(
                "all_artists.json" if len(arguments) <= 1 else arguments[1],
                "w"
            ) as f:
                f.write(json_str)
        case "-gni": # Get Next Id
            print(f"Next ID: {get_next_id()}")
        case "-h":
            print_help_message()