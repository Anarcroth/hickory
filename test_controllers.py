"""More like manual testing; without the aim of being comprehensive."""

import controllers
from controllers import User, Route, Recommendation

print(User.get(1))
print(Route.get(6))
print(controllers.get_recommendation(1))
