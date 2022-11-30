import sublime

date_prototype = [
	sublime.CompletionItem(
		"now",
		annotation="date",
		completion="now()",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"parse",
		annotation="date",
		completion="parse($0)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
]