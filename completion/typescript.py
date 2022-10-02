import sublime

typescript = []
text = [
    "any",
    "string",
    "number",
    "boolean",
    "object",
    "symbol",
    "bigint",
    "unknown",
    "interface",
    "type",
    "readonly",
    "unique",
    "implements",
    "public",
    "private",
    "protected",
    "abstract"
]

for x in text:
	typescript.append(sublime.CompletionItem(
		x,
		annotation=x,
		completion=x,
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_KEYWORD
	))