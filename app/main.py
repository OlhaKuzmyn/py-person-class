class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    for person in people:
        person_obj = Person(person["name"], person["age"])
        if person.get("wife"):
            person_obj.wife = person["wife"]
        elif person.get("husband"):
            person_obj.husband = person["husband"]

    for person_obj in Person.people.values():
        if hasattr(person_obj, "wife"):
            person_obj.wife = Person.people.get(person_obj.wife)
        elif hasattr(person_obj, "husband"):
            person_obj.husband = Person.people.get(person_obj.husband)
    return list(Person.people.values())
