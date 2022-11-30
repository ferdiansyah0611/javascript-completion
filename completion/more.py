import sublime

more = [
	sublime.CompletionItem(
		"includes",
		annotation="array|string",
		completion="includes($0)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"switch",
		annotation="switch",
		completion="switch(variable$0){\n\tcase 0:\n\t\tbreak;\n\tdefault:\n\t\treturn;\n}",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"us",
		annotation="use strict",
		completion="'use strict';",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"json",
		annotation="JSON.parse",
		completion="JSON.parse(object$0)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"json",
		annotation="JSON.stringify",
		completion="JSON.stringify(object$0)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"try",
		annotation="try/catch",
		completion="try {\n\t$0\n} catch(e) {\n\tconsole.log(e.message)\n}",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"try",
		annotation="try/catch/finally",
		completion="try {\n\t$0\n} catch(e) {\n\tconsole.log(e.message)\n} finally{\n\t\n}",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"setinterval",
		annotation="setInterval",
		completion="setInterval(() => {\n\t$0\n})",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"settimeout",
		annotation="setTimeout",
		completion="setTimeout(() => {\n\t$0\n})",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"clearinterval",
		annotation="clearInterval",
		completion="clearInterval($0)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"cleartimeout",
		annotation="clearTimeout",
		completion="clearTimeout($0)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"fetch",
		annotation="fetch then",
		completion="fetch(url, {}).then(response => response.json()).then(response => {\n\t\n})",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"fetch",
		annotation="fetch await",
		completion="let response = await fetch(url, {})\nresult = await response.json()\n",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"length",
		annotation="length",
		completion="length",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_VARIABLE
	),
	sublime.CompletionItem(
		"require",
		annotation="require('$0');",
		completion="var name = require('$0');",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"module",
		annotation="module.exports",
		completion="module.exports = $0;",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"import",
		annotation="import es6",
		completion="import name from '$0';",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"export",
		annotation="export es6",
		completion="export default $0;",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
]