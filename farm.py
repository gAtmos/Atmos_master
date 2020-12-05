# %%
from trello import TrelloClient
from trello.trellolist import List as TrelloList

API = {
   'key': 'f32d2c2b280e3e332d19e1e4a531131b',
   'token': '83522f3c43b03d9eaddc2e939299776ff3a90ad0ac0308c5937cfe9e6b1b6b94',
}

FARM_BOARD_ID = 'jQk67bqb'

DEFAULT_CHECKLIST_TITLE = "cycle"
DEFAULT_CHECKLIST_STEPS = ("seeding", "dark time", "light time", "harvest", "packaging")


class NotStartedException(Exception):
    def __init__(self, floor_name):
        super().__init__(f"Floor '{floor_name}' is not started.")

class Farm(TrelloClient):
    """ Wrapper around the Farm trello board """
    def __init__(self, key=API["key"], token=API["token"]):
        """ Gets instanciated with default keys """
        super().__init__(api_key=key, token=token)
        self.farm = self.get_board('jQk67bqb')

    def get_shelves(self, list_keyword="Etagère"):
        """ List shelves in the farm declared as lists on Trello """
        return [Shelf(shelf) for shelf in self.farm.list_lists() if shelf.name.startswith(list_keyword)]


class Shelf:
    """ A wrapper aroud a shelf (trello list) """
    def __init__(self, trello_object):
        self.contained = trello_object

    def get_floors(self):
        """ Get a list of floors """
        return [Floor(floor) for floor in self.contained.list_cards()]
    
    # Wrapping method
    def __getattr__(self, item):
        result = getattr(self.contained, item)
        return result

class Floor:
    """ A wrapper aroud a floor (trello card) """
    def __init__(self, trello_object, steps=DEFAULT_CHECKLIST_STEPS, title=DEFAULT_CHECKLIST_TITLE):
        self.steps = steps
        self.title = title
        self.contained = trello_object

    def is_started(self):
        """ Checks if the floor is ongoing by checking if the corresponding trello card has a positive number of checklist items """
        #? return len(self.contained.checklists) > 0
        return self.contained.badges["checkItems"] > 0
    
    # Wrapping method
    def __getattr__(self, item):
        result = getattr(self.contained, item)
        return result
    
    def start(self, force=False):
        """ Starts the floor by adding a checklist with the elements in `steps` as checklist items. Returns False if it is already started. If force is True, it creates a new checklist"""
        started = self.is_started()
        if started and not force:
            print("Floor already started")
            return False
        else:
            if started:
                for checklist in self.contained.checklists:
                    checklist.delete()
            self.contained.add_checklist(title=self.title, items=self.steps)
    
    def advance(self):
        """ Increases the checklist progress by one step. Returns True if it was the last item to check in the list, False instead. Raises a `NotStartedException` if the card has no checklist """
        if not self.is_started():
            raise NotStartedException(self.contained.name)
        
        checklist = self.contained.checklists[0]
        for i, item in enumerate(checklist.items):
            if not item["checked"]:
                checklist.set_checklist_item(item["name"], True)
                if i == len(checklist.items) - 1:
                    return True
                return False
                



#%%

if __name__ == "__main__":
    # Iterate over shelves
    for shelf in Farm().get_shelves():
        # Iterate over floors
        for floor in shelf.get_floors():
            # Print information
            print(f"Floor", floor.name, "is", "ongoing" if floor.is_started() else "new", "and due", floor.due)
            # If floor not started then start it
            if not floor.is_started():
                floor.start()
            if floor.name == "Carotte":
                print(floor.advance())
            

# %%
