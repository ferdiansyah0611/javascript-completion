import sublime

variable = [
	sublime.CompletionItem(
		"var",
		annotation="var",
		completion="var name = '$0';",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_VARIABLE
	),
	sublime.CompletionItem(
		"let",
		annotation="var",
		completion="let name = '$0';",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_VARIABLE
	),
	sublime.CompletionItem(
		"const",
		annotation="var",
		completion="const name = '$0';",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_VARIABLE
	),
]