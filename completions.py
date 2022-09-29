import sublime
from .completion.logic import logic
from .completion.variable import variable
from .completion.function import function
from .completion.classes import classes
from .completion.objects import objects
from .completion.more import more

completions = logic + variable + function + classes + objects + more