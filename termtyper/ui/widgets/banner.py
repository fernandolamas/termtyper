from rich.align import Align
from rich.panel import Panel
from rich.text import Text


banners = {
    "welcome": """
╔╦╗┌─┐┬─┐┌┬┐┌┬┐┬ ┬┌─┐┌─┐┬─┐┬─┐
 ║ ├┤ ├┬┘│││ │ └┬┘├─┘├┤ ├┬┘├┬┘
 ╩ └─┘┴└─┴ ┴ ┴  ┴ ┴  └─┘┴└─┴└─
""",
    "settings": """
╔═╗┌─┐┌┬┐┌┬┐┬┌┐┌┌─┐┌─┐
╚═╗├┤  │  │ │││││ ┬└─┐
╚═╝└─┘ ┴  ┴ ┴┘└┘└─┘└─┘
""",
    "hardcore": """
┬ ┬┌─┐┬─┐┌┬┐┌─┐┌─┐┬─┐┌─┐
├─┤├─┤├┬┘ │││  │ │├┬┘├┤
┴ ┴┴ ┴┴└──┴┘└─┘└─┘┴└─└─┘
""",
    "push_your_limits": """
┌─┐┬ ┬┌─┐┬ ┬  ┬ ┬┌─┐┬ ┬┬─┐  ┬  ┬┌┬┐┬┌┬┐┌─┐
├─┘│ │└─┐├─┤  └┬┘│ ││ │├┬┘  │  │││││ │ └─┐
┴  └─┘└─┘┴ ┴   ┴ └─┘└─┘┴└─  ┴─┘┴┴ ┴┴ ┴ └─┘
""",
    "discipline": """
┌┬┐┬┌─┐┌─┐┬┌─┐┬  ┬┌┐┌┌─┐
 │││└─┐│  │├─┘│  ││││├┤
─┴┘┴└─┘└─┘┴┴  ┴─┘┴┘└┘└─┘
""",
    "eye_candy": """
┌─┐┬ ┬┌─┐  ┌─┐┌─┐┌┐┌┌┬┐┬ ┬
├┤ └┬┘├┤   │  ├─┤│││ ││└┬┘
└─┘ ┴ └─┘  └─┘┴ ┴┘└┘─┴┘ ┴
""",
    "aesthetics": """
┌─┐┌─┐┌─┐┌┬┐┬ ┬┌─┐┌┬┐┬┌─┐┌─┐
├─┤├┤ └─┐ │ ├─┤├┤  │ ││  └─┐
┴ ┴└─┘└─┘ ┴ ┴ ┴└─┘ ┴ ┴└─┘└─┘
""",
    "misc": """
┌┬┐┬┌─┐┌─┐┌─┐┬  ┬  ┌─┐┌┐┌┌─┐┌─┐┬ ┬┌─┐
││││└─┐│  ├┤ │  │  ├─┤│││├┤ │ ││ │└─┐
┴ ┴┴└─┘└─┘└─┘┴─┘┴─┘┴ ┴┘└┘└─┘└─┘└─┘└─┘
""",
}

banners = {
    i: Panel(Align.center(Text(j, style="bold blue"), vertical="middle"))
    for i, j in banners.items()
}
