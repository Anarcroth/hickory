"""More like manual testing; without the aim of being comprehensive."""

import controllers
from controllers import User, Route, Recommendation

print(User.get(1))
print(Route.get(6))

r = controllers.get_recommendation(1)
for x in r:
	print(controllers.Route.to_json(x))
