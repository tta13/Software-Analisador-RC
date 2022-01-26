# Backend
The backend consists of a Flask application that listens and answers to HTTP requests and a series of Python scripts which perform the match analysis.

## Match analysis file format
* gameResult:
	* leftTeamName: score 
	* rightTeamName: score
* leftTeamName: left team stats
	* teamName: name of the team
	* shots: total shots computed for the team
	* onTargetShots: on target shots computed for the team
	* shotAccuracy: % of shots on target relative to total shots
	* goals: goals scored by the team
	* scorers: list of goal scorers and the cycle in which they scored
	* completedPasses: # of completed passes
	* wrongPasses: # of intercepted passes
	* passAccuracy: % of completed passes
	* interceptions: # of interceptions
	* possession: % of play on cycles in which the team was deemed the ball owner
	* fouls: # of fouls charged against the team
	* corners: # of corners registered for the club
	* offsides: # of offsides calls against the team
	* playersDistances: array of distances covered for each player
	* averageDistance10: average distance covered from outfield players
	* playersStamina: array of used stamina from each player at the end of the match
	* averageStamina10: average of used stamina from the outfield players
	* averageStaminaPerDistance10: average used stamina per distance from outfield players
	* staminaPerDistance: array of stamina used for each player per distance covered
* rightTeamName: right team stats (same as above)