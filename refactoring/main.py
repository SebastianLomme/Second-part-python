__winc_id__ = "9920545368b24a06babf1b57cee44171"
__human_name__ = "refactoring"

import weakref

class Homeowner:
    def __init__(self, name, address, needs):
        self.name = name
        self.address = address
        self.needs = needs

    def contracts(self):
        contract = []
        for need in self.needs:
            cheapest_price = float('inf')
            cheapest_name = ""
            for spec in Specialist.getinstances():
                if need == spec.profession:
                    if spec.pricing < cheapest_price:
                        cheapest_price = spec.pricing
                        cheapest_name = spec.name
            contract.append(cheapest_name)
        return contract


class Specialist:
    _instances = set()
    def __init__(self, name, pricing):
        self.name = name
        self.pricing = pricing
        self._instances.add(weakref.ref(self))

    @classmethod
    def getinstances(cls):
        dead = set()
        for ref in cls._instances:
            obj = ref()
            if obj is not None:
                yield obj
            else:
                dead.add(ref)
        cls._instances -= dead


class Electrician(Specialist):
    profession = "electrician"

    def __init__(self, name, pricing):
        super().__init__(name, pricing)



class Painter(Specialist):
    profession = "painter"

    def __init__(self, name, pricing):
        super().__init__(name, pricing)


class Plumber(Specialist):
    profession = "plumber"

    def __init__(self, name, pricing):
        super().__init__(name, pricing)


alfred = Homeowner("Alfred Alfredson", "Alfredslane 123", ["painter", "plumber"])
bert = Homeowner("Bert Bertson", "Bertslane 231", ["plumber"])
candice = Homeowner(
    "Candice Candicedottir", "Candicelane 312", ["electrician", "painter"]
)


alice = Electrician("Alice Aliceville", 40)
Land = Electrician("Land Landville", 32)
bob = Painter("Bob Bobsville", 40)
craig = Plumber("Craig Craigsville", 30)
tess = Plumber("Tess Tessville", 50)

print("Alfred's contracts:", alfred.contracts())
print("Bert's contracts:", bert.contracts())
print("Candice's contracts:", candice.contracts())


