import sublime, re
import sublime_plugin
from .completion import available_completions

class JavascriptCommand(sublime_plugin.EventListener):

	def on_query_completions(self, view, prefix, locations):
		source = [
			view.match_selector(locations[0], "source.js"),
			view.match_selector(locations[0], "source.jsx"),
			view.match_selector(locations[0], "source.ts"),
			view.match_selector(locations[0], "source.tsx")
		]
		if not True in source:
			return []

		prefix 		= prefix.lower()
		out 		= []
		for comp in available_completions:
			if comp.trigger.find(r'{{prefix}}'):
				out.append(comp)

		return out