import sublime

length = [
	sublime.CompletionItem(
		"length",
		annotation="length",
		completion="length",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_VARIABLE
	),
]

_logic = [
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

_var = [
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

_array = [
	sublime.CompletionItem(
		"find",
		annotation="array",
		completion="find((item, i) => {\n\treturn true;$0\n})",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"findindex",
		annotation="array",
		completion="findIndex((item, i) => {\n\treturn true;$0\n})",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"filter",
		annotation="array",
		completion="filter((item, i) => {\n\treturn i === 0;$0\n})",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"forEach",
		annotation="array",
		completion="forEach((item, i) => {\n\t$0\n})",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"map",
		annotation="array",
		completion="map((item, i) => {\n\treturn item;$0\n})",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"at",
		annotation="array",
		completion="at(-1$0)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"concat",
		annotation="array",
		completion="concat([$0])",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"includes",
		annotation="array",
		completion="includes($0)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"join",
		annotation="array",
		completion="join($0)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"push",
		annotation="array",
		completion="push($0)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"reverse",
		annotation="array",
		completion="reverse()",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"slice",
		annotation="array",
		completion="slice(0, 1$0)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"some",
		annotation="array",
		completion="some((item, i) => {\n\t$0\n})",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"reduce",
		annotation="array",
		completion="reduce((prev, cur, i) => {\n\t$0\n})",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"fill",
		annotation="array",
		completion="fill($0, 0, 1)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
] + length

_try_catch = [
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
]

_function = [
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
		completion="let name$0 = (arguments) => {}",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"fn",
		annotation="async arrow function",
		completion="let name$0 = async (arguments) => {}",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
]

_class = [
	sublime.CompletionItem(
		"class",
		annotation="class",
		completion="class Main$0(){\n\tconstructor(){\n\t\n\t}\n}",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
]

_object = [
	sublime.CompletionItem(
		"object",
		annotation="Object",
		completion="{}",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"assign",
		annotation="Object",
		completion="Object.assign($0, value)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"create",
		annotation="Object",
		completion="Object.create({$0})",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"entries",
		annotation="Object",
		completion="Object.entries($0)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"freeze",
		annotation="Object",
		completion="Object.freeze($0)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"fromentries",
		annotation="Object",
		completion="Object.fromEntries($0)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"keys",
		annotation="Object",
		completion="Object.keys($0)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"seal",
		annotation="Object",
		completion="Object.seal($0)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"defineproperty",
		annotation="Object",
		completion="Object.defineProperty($0, 'property', {\n\tvalue: 1,\n\twritable: false\n});",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
]

_string = [
	sublime.CompletionItem(
		"match",
		annotation="string",
		completion="match($0)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"matchall",
		annotation="string",
		completion="matchAll($0)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"indexof",
		annotation="string",
		completion="indexOf($0)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"includes",
		annotation="string",
		completion="includes(\"$0\")",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"localecompare",
		annotation="string",
		completion="localeCompare($0)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"repeat",
		annotation="string",
		completion="repeat($0)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"replace",
		annotation="string",
		completion="replace($0, '')",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"replaceall",
		annotation="string",
		completion="replaceAll($0, '')",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"search",
		annotation="string",
		completion="search($0)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"slice",
		annotation="string",
		completion="slice(0, $0)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"split",
		annotation="string",
		completion="split($0)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"startswith",
		annotation="string",
		completion="startsWith($0)",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"tolowercase",
		annotation="string",
		completion="toLowerCase()",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
	sublime.CompletionItem(
		"touppercase",
		annotation="string",
		completion="toUpperCase()",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_FUNCTION
	),
] + length

_more = [
	sublime.CompletionItem(
		"switch",
		annotation="switch",
		completion="switch(variable$0){\n\tcase 0:\n\t\tbreak;\n\tdefault:\n\t\treturn;\n}",
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
]

available_completions = _logic + _var + _array + _try_catch + _function + _class + _object + _string + _more