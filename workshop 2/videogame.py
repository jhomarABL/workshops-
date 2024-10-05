class VideoGame:
    def __init__(
        self,
        name,
        creator_story,
        creator_graphics,
        category,
        price,
        year,
        definition="Standard",
    ):
        self.name = name
        self.creator_story = creator_story
        self.creator_graphics = creator_graphics
        self.category = category
        self.price = price * (1.1 if definition == "High" else 1)
        self.year = year
        self.definition = definition

    def __str__(self):
        return f"{self.name} ({self.definition}): ${self.price:.2f}, Category: {self.category}, Year: {self.year}"
