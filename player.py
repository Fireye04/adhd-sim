class Player:
    def __init__(self, _stats) -> None:
        # Each stat gets a value and an increment. The increment is the daily change

        # ----------------STATS----------------

        self.stats = _stats

        self.stress = _stats["stress"][0]
        self.stress_increment = _stats["stress"][1]

        self.happiness = _stats["happiness"][0]
        self.happiness_increment = _stats["happiness"][1]

        self.hunger = _stats["hunger"][0]
        self.hunger_increment = _stats["hunger"][1]

        self.hygiene = _stats["hygiene"][0]
        self.hygiene_increment = _stats["hygiene"][1]

        self.sleep = _stats["sleep"][0]
        self.sleep_increment = _stats["sleep"][1]

        self.bananas = _stats["bananas"][0]
        self.bananas_increment = _stats["bananas"][1]

        self.grades = _stats["grades"][0]
        self.grades_increment = _stats["grades"][1]

        self.relationships = _stats["relationships"][0]
        self.relationship_increment = _stats["relationships"][1]

        self.skills = _stats["skills"][0]
        self.skills_increment = _stats["skills"][1]

        # ----------------/STATS----------------

    def format_dict(self, dict):
        final = ""
        for key, item in dict.items():
            final = final + f"\n    {key}- {item}"
        return final

    def __str__(self) -> str:
        return (
            f"stress- {self.stress} ({self.stress_increment})\n"
            f"happness- {self.happiness} ({self.happiness_increment})\n"
            f"hunger- {self.hunger} ({self.hunger_increment})\n"
            f"hygiene- {self.hygiene} ({self.hygiene_increment})\n"
            f"sleep- {self.sleep} ({self.sleep_increment})\n"
            f"bananas- {self.bananas} ({self.bananas_increment})\n"
            f"grades- {self.grades} ({self.grades_increment})\n"
            f"relationships- ({self.relationship_increment}){self.format_dict(self.relationships)}\n"
            f"skills- ({self.skills_increment}){self.format_dict(self.skills)}\n"
        )

    def pass_time(self):
        pass
