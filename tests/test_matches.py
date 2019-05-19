from classes.MatchesADT import Matches


matches1 = Matches(1)
assert(matches1.is_empty())

matches2 = Matches(1)
matches2.add("sr:match:16618843")
assert (matches2 == Matches(1, ["sr:match:16618843"]))

matches3 = Matches(1, ["sr:match:16618843"])
assert(matches3.pop() == "sr:match:16618843")


matches4 = Matches(1, ["sr:match:16608857"])
assert(matches4.process_match() == ['sr:competitor:71660', 'Marterer Maximilian','sr:competitor:16194',
                                    'Gojowczyk Peter', 'sr:match:16608857', '0.528', '0.463', '0.5', '0'])

matches5 = Matches(1, ["sr:match:16608857"])
assert(len(matches5) == 1)
