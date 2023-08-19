def person_lister(f):
    def inner(people):
        # complete the function
        people.sort(key=lambda person: int(person[2]))  # Sort based on the second item (age)
        return [f(person) for person in people]
    return inner