class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    for person in people:
        person_obj = Person(person["name"], person["age"])
        if "wife" in person and person["wife"] is not None:
            person_obj.wife = person["wife"]
        elif "husband" in person and person["husband"] is not None:
            person_obj.husband = person["husband"]
    for person_obj in Person.people.values():
        for person_ in Person.people.values():
            if (hasattr(person_, "wife")
                    and person_.wife == person_obj.name):
                person_.wife = person_obj
            elif (hasattr(person_, "husband")
                  and person_.husband == person_obj.name):
                person_.husband = person_obj
    return list(Person.people.values())
