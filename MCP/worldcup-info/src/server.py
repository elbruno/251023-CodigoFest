import json
from typing import Optional
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
server = FastMCP("worldcup_2026_info")

# World Cup 2026 Data
TOURNAMENT_INFO = {
    "name": "FIFA World Cup 2026",
    "hosts": ["United States", "Canada", "Mexico"],
    "dates": "June 11 - July 19, 2026",
    "teams": 48,
    "matches": 104,
    "venues": 16,
    "first_tri_nation_host": True,
    "final_venue": "MetLife Stadium, New Jersey, USA",
    "opening_match": "Estadio Azteca, Mexico City, Mexico"
}

HOST_CITIES = {
    "United States": [
        {"city": "New York/New Jersey", "stadium": "MetLife Stadium", "capacity": 82500, "matches": "Including Final"},
        {"city": "Los Angeles", "stadium": "SoFi Stadium", "capacity": 70000, "matches": "Multiple group stage and knockout"},
        {"city": "Dallas", "stadium": "AT&T Stadium", "capacity": 80000, "matches": "Including Semi-final"},
        {"city": "San Francisco Bay Area", "stadium": "Levi's Stadium", "capacity": 68500, "matches": "Group stage and knockout"},
        {"city": "Miami", "stadium": "Hard Rock Stadium", "capacity": 65000, "matches": "Third-place playoff"},
        {"city": "Atlanta", "stadium": "Mercedes-Benz Stadium", "capacity": 71000, "matches": "Including Semi-final"},
        {"city": "Seattle", "stadium": "Lumen Field", "capacity": 69000, "matches": "Group stage and knockout"},
        {"city": "Houston", "stadium": "NRG Stadium", "capacity": 72000, "matches": "Group stage and knockout"},
        {"city": "Philadelphia", "stadium": "Lincoln Financial Field", "capacity": 69000, "matches": "Group stage and knockout"},
        {"city": "Kansas City", "stadium": "Arrowhead Stadium", "capacity": 76000, "matches": "Group stage and knockout"},
        {"city": "Boston", "stadium": "Gillette Stadium", "capacity": 65000, "matches": "Group stage and knockout"}
    ],
    "Mexico": [
        {"city": "Mexico City", "stadium": "Estadio Azteca", "capacity": 87000, "matches": "Including Opening Match"},
        {"city": "Guadalajara", "stadium": "Estadio Akron", "capacity": 46000, "matches": "Group stage and knockout"},
        {"city": "Monterrey", "stadium": "Estadio BBVA", "capacity": 53000, "matches": "Group stage and knockout"}
    ],
    "Canada": [
        {"city": "Toronto", "stadium": "BMO Field", "capacity": 45000, "matches": "Group stage and knockout"},
        {"city": "Vancouver", "stadium": "BC Place", "capacity": 54000, "matches": "Group stage and knockout"}
    ]
}

MATCH_SCHEDULE_INFO = {
    "tournament_structure": {
        "group_stage": {
            "groups": 12,
            "teams_per_group": 4,
            "matches": 80,
            "description": "Top 2 teams from each group and 8 best third-placed teams advance"
        },
        "knockout_stage": {
            "round_of_32": "16 matches",
            "round_of_16": "8 matches",
            "quarter_finals": "4 matches",
            "semi_finals": "2 matches",
            "third_place": "1 match",
            "final": "1 match"
        }
    },
    "key_dates": {
        "opening_ceremony": "June 11, 2026",
        "opening_match": "June 11, 2026 - Estadio Azteca, Mexico City",
        "group_stage_ends": "June 27, 2026",
        "round_of_32": "June 29 - July 3, 2026",
        "round_of_16": "July 5-7, 2026",
        "quarter_finals": "July 9-11, 2026",
        "semi_finals": "July 14-15, 2026",
        "third_place_playoff": "July 18, 2026 - Hard Rock Stadium, Miami",
        "final": "July 19, 2026 - MetLife Stadium, New Jersey"
    },
    "notes": [
        "First World Cup with 48 teams",
        "First World Cup hosted by three nations",
        "Mexico's Estadio Azteca will be the first stadium to host World Cup matches in three tournaments (1970, 1986, 2026)",
        "USA will host 60 matches, including the final",
        "Mexico and Canada will each host 10 matches"
    ]
}

@server.tool()
async def get_tournament_info() -> str:
    """Get general information about the FIFA World Cup 2026.
    
    Returns comprehensive details about the tournament including dates,
    host countries, number of teams, venues, and special facts.
    """
    return json.dumps(TOURNAMENT_INFO, indent=2, ensure_ascii=False)

@server.tool()
async def get_host_cities(country: Optional[str] = None) -> str:
    """Get information about host cities and stadiums for World Cup 2026.
    
    Args:
        country: Optional filter by country ('United States', 'Canada', or 'Mexico').
                If not provided, returns all host cities.
    
    Returns:
        JSON with host city information including stadium names, capacities,
        and types of matches they will host.
    """
    if country:
        # Normalize country name
        country_map = {
            "usa": "United States",
            "united states": "United States",
            "us": "United States",
            "mexico": "Mexico",
            "canada": "Canada"
        }
        normalized_country = country_map.get(country.lower(), country)
        
        if normalized_country in HOST_CITIES:
            result = {normalized_country: HOST_CITIES[normalized_country]}
            return json.dumps(result, indent=2, ensure_ascii=False)
        else:
            return json.dumps({
                "error": f"Country '{country}' not found. Valid countries: United States, Canada, Mexico"
            }, indent=2)
    
    return json.dumps(HOST_CITIES, indent=2, ensure_ascii=False)

@server.tool()
async def get_match_schedule() -> str:
    """Get tournament structure and schedule information for World Cup 2026.
    
    Returns detailed information about:
    - Tournament structure (group stage and knockout rounds)
    - Key dates and milestones
    - Special notes and historical facts
    """
    return json.dumps(MATCH_SCHEDULE_INFO, indent=2, ensure_ascii=False)
