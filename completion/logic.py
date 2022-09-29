import sublime

logic = [
	sublime.CompletionItem(
		"if",
		annotation="if",
		completion="if (true$0) {\n\t\n}",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"else if",
		annotation="else if",
		completion="else if(true) {\n\t$0\n}",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"else",
		annotation="else",
		completion="else {\n\t$0\n}",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
]