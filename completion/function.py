import sublime

function = [
	sublime.CompletionItem(
		"fn",
		annotation="function es6",
		completion="function name$0(arguments){\n\t\n}",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"fn",
		annotation="async function es6",
		completion="async function name$0(arguments){\n\t\n}",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"fn",
		annotation="arrow function",
		completion="(arguments) => {}",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"fn",
		annotation="async arrow function",
		completion="async (arguments) => {}",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
]