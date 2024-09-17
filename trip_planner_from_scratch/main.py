import os 
from crewai import Crew, Process
from textwrap import dedent
from agents import TravelAgents
from tasks import TravelTasks


from dotenv import load_dotenv
load_dotenv()


class TripCrew:

    def __init__(self, origin, cities, date_range, interests):
        self.origin = origin
        self.cities = cities
        self.date_range = date_range
        self.interests = interests



    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = TravelAgents()
        tasks = TravelTasks()


        # Define your custom agents and tasks here

        expert_travel_agent = agents.expert_travel_agent()
        city_selection_agent = agents.city_selection_agent()
        local_tour_guide = agents.local_tour_guide()


        # Custom tasks include agent name and variables as input
        plan_itinerary = tasks.plan_itinerary(
            expert_travel_agent,
            self.cities,
            self.date_range,
            self.interests
        )
        



        Identify_city = tasks.Identify_city(
            city_selection_agent,
            self.origin,
            self.cities,
            self.interests,
            self.date_range
        )



        gether_city_info = tasks.gether_city_info(
            local_tour_guide,
            self.cities,
            self.interests,
            self.date_range
        )


        # Define your custom crew here

        crew = Crew(
            agents = [expert_travel_agent,
                      city_selection_agent,
                      local_tour_guide],
            tasks = [plan_itinerary,
                     Identify_city,
                     gether_city_info],
            verbose = True,
        )

        result = crew.kickoff()
        return result


        