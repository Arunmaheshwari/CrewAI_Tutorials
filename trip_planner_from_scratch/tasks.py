"""
Creating Tasks Cheat sheet:
- Begin with the end in mind. Identify the specific outcome your tasks are aiming to achieve.
- Break down the outcome into actionable tasks, assiging each task to the appropriate agent.
- Ensure tasks are descriptive, providing clear instructions and expected deliverables.


Goal:
- Develop a detailed itinerary, including city selection, attractions, and practical travel advice.

Key steps for Task Creation:
1. Identify the Desired Outcome: Define what success looks like for your project.
    - A detailed 7 day travel itenerary.

2. Taks Breakdown: Divide the goal into smaller, manageable tasks that agents can execute.
    - Iternerary Planning: develop a detailed plan for each day of the trip.
    - City Selection: Analayze adn pick the best cities to visit.
    - Local Tour Guide: Find a local expert to provide insights and recommendations.

3. Assign Tasks to Agents: Match tasks with agents based on their roles and expertise.

4. Task Description Template:
 - Use this template as a guide to difine each task in your CrewAI application.
  - This template helps ensure that each task is clearly defined, actionable, and aligned with the specific goals of


  Template:
  ------------
  def [task_name](self, agent, [parameters]):
       return Taks(decription = dedent(f'''
       **Task**: [Provide a concise nam or summary of the task.]
       **Description**: [Detailed decription of what the agent is expected to do, including actionable steps and expected outcomes. This should be clear and direct, outlining the sepecific actions required to complete the task.]))
       **Parameters**:
       - [parameter 1]: [Description]
       - [Parameter 2]: [Description]
       ... [Add more parameters as needed.]

       **Note**: [Optional section for incetives or encouragement for high-quality work. This can include tips, additional context, or motivations to encourage agents to deliver their best work.]
       '''), agent = agent       
"""


class CustomTasks:
    def __tips_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"
    
    def plan_itinerary(self, agent, city, travel_dates, interests):
        return Task(
            decription = dedent(f'''
            **Task**: Develop a 7-Day Travel Itinerary
            **Description**: Expand the city guide into a full 7-day travel itinerary with detailed
                per-day plans, including weather forecasts, places to eat, packing suggestions,
                and a budget breakdown. You MUST suggest actual places to visit, actual hotels to stay,
                from arrival to departure, integrating the city guide information with practical travel logistics.
            **Parameters**:
            - City: {city}
            - Trip Date: {travel_dates}
            - Traveler Interests: {interests}

            **Note**: {self.__tips_section()}
'''   
            ),
            agent = agent,
        )
    


    def Identify_city(self, agent, origin, cities, interests, travel_dates):
        return Task(
            description = dedent(
                f"""
                    **Task**: Identify the Best City for the Trip
                    **Description**: Analyze and select the best city for the trip based on specific
                        criteria such as weather patterns, seasonal events, adn travel costs. 
                        This task involves comparing multiple cities, considering factors like current weather
                        conditions, upcoming cultural or seasonal events, and overall travel expenses. 
                        Your final answer must be a detailed reeport on the chosen city,
                        including actual flight costs, weather forecast, and attractions. 

                    
                        **Parameters**:
                        - Origin: {origin}
                        - Cities: {cities}
                        - Interests: {interests}
                        - Travel Date: {travel_dates}

                        **Note**: {self.__tips_section()}
        """
            ),
            agent = agent,


        )
    


    def gether_city_info(self, agent, city, interests, travel_dates):
        return Task(
            description = dedent(
                f"""
                    **Task**: Gather In-depth City Guide Information
                    **Description**: Compile an in-depth guide for the selected city, gathering information about
                    key attractions, local customs, special events, and daily activity recommendations.
                    This guide should provide a thorough overview of what the city has to offer, including
                    hidden gems, cultural hotspots, must-visit landmarks, weather forecasts, and high-level costs.

                    
                        **Parameters**:
                        
                        - Cities: {city}
                        - Interests: {interests}
                        - Travel Date: {travel_dates}

                        **Note**: {self.__tips_section()}
        """
            ),
            agent = agent,


        )
        
