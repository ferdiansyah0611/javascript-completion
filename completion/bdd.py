import sublime

bdd = [
	sublime.CompletionItem(
		"describe",
		annotation="describe",
		completion="describe('', () => {\n\t$0\n})",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"it",
		annotation="it",
		completion="it('', () => {\n\t$0\n})",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"expect",
		annotation="expect",
		completion="expect($0).toBe($1)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
]