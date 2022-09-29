import sublime

classes = [
	sublime.CompletionItem(
		"class",
		annotation="class",
		completion="class Main$0(){\n\tconstructor(){\n\t\n\t}\n}",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
]