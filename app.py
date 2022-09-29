import sublime, re
import sublime_plugin

from .completions import completions
from .completion.string import string
from .completion.console import console
from .completion.array import array

class JavascriptCommand(sublime_plugin.EventListener):
	def on_query_completions(self, view, prefix, locations):
		source = [
			view.match_selector(locations[0], "source.js"),
			view.match_selector(locations[0], "source.jsx"),
			view.match_selector(locations[0], "source.ts"),
			view.match_selector(locations[0], "source.tsx"),
			view.match_selector(locations[0], "source.mjs"),
		]
		if not True in source:
			return []

		prefix 		= prefix.lower()
		out 		= []
		target 		= completions

		if prefix != '':
			target = completions + array + string + console

		for comp in target:
			if comp.trigger.find(r'{{prefix}}'):
				out.append(comp)

		return out