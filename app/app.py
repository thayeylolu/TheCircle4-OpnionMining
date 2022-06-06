import sys

sys.path.append("../")

from click import style
from dash import (
    Dash,
    Input,
    Output,
    html,
    dcc,
    callback,
)  # need version dash 2.0.0 or higher
from components.style import *

# import 'components/style' as sty

app = Dash(__name__)
app.config.suppress_callback_exceptions = True


app.layout = html.Div(
    [
        html.Div(
            [
                html.Div(html.P("contains 1"), style=LeftContainer()),
                html.Div(html.P("contains 2"), style=RightContainer()),
            ],
            style=BgStyle(),
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True, port=2031)
