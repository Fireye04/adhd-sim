

class Player:
    def __init__(self, d_stress: int, d_stress_i: int, d_happiness: int, 
                 d_happiness_i: int, d_hunger: int, d_hunger_i: int, 
                 d_hygiene: int, d_hygiene_i: int, d_sleep: int, 
                 d_sleep_i: int, d_bananas: int, d_bananas_i: int, 
                 d_grades: int, d_grades_i:int, d_relationips: {}, 
                 d_relationships_i: int, d_skills: {}, d_skills_i: int
                ) -> None:
        
        # Each stat gets a value and an increment. The increment is the daily change
       
        #----------------STATS----------------

        self.stress = d_stress
        self.stress_increment = d_stress_i

        self.happiness = d_happiness
        self.happiness_increment = d_happiness_i

        self.hunger = d_hunger
        self.hunger_increment = d_hunger_i

        self.hygiene = d_hygiene
        self.hygiene_increment = d_hygiene_i

        self.sleep = d_sleep
        self.sleep_increment = d_sleep_i

        self.bananas = d_bananas
        self.bananas_increment = d_bananas_i

        self.grades = d_grades
        self.grades_increment = d_grades_i

        self.relationships = d_relationips
        self.relationship_increment = d_relationships_i

        self.skills = d_skills
        self.skills_increment = d_skills_i

        #TODO: add all stats to the stats dict
        self.stats = {}

        #----------------/STATS----------------

        
    

    def format_dict(self, dict):
        final = ""
        for key,item in dict.items():
            final = final + f"\n    {key}- {item}"
        return final


    def __str__(self) -> str:

        return (f"stress- {self.stress} ({self.stress_increment})\n"
                f"happness- {self.happiness} ({self.happiness_increment})\n"
                f"hunger- {self.hunger} ({self.hunger_increment})\n"
                f"hygiene- {self.hygiene} ({self.hygiene_increment})\n"
                f"sleep- {self.sleep} ({self.sleep_increment})\n"
                f"bananas- {self.bananas} ({self.bananas_increment})\n"
                f"grades- {self.grades} ({self.grades_increment})\n"
                f"relationships- {self.format_dict(self.relationships)}\n({self.relationship_increment})\n"
                f"skills- {self.format_dict(self.skills)} ({self.skills_increment})")


    def pass_time(self):
        pass
        # Here iterate over the stats dict and increment vals