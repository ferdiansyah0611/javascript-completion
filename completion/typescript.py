import sublime

typescript = [
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

def update(text):
	return sublime.CompletionItem(
		text,
		annotation=text,
		completion=text,
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_KEYWORD
	)

typescript = list(map(update, typescript))