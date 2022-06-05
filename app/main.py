import sys
from turtle import st
import dash_bootstrap_components as dbc

sys.path.append("../")

from click import style
from dash import (
    Dash,
    Input,
    Output,
    html,
    dcc,
    callback,
)
from components.main_component import *


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config.suppress_callback_exceptions = True


app.layout = html.Div(
    [
        Containers(
            children=[
                RowMains(
                    children=[
                        ColumnSections(
                            Rows(
                                children=[
                                    html.P("Left Container"),
                                    Rows(
                                        children=[
                                            ColsOne(lg=2),
                                            ColsOne(lg=2),
                                            ColsOne(lg=2),
                                            ColsOne(lg=6),
                                        ],
                                        justify="evenly",
                                        style=SectionOneParent(),
                                    ),
                                ],
                            )
                        ),
                        # rights
                        ColumnSections(
                            Rows(
                                children=[
                                    html.P("Righ Container"),
                                    # section 2
                                    Rows(
                                        children=[
                                            ColsTwo(),
                                        ],
                                    ),
                                    # section 5
                                    Rows(
                                        children=[
                                            # Section 5a
                                            Rows(
                                                children=[
                                                    ColsTwoInner(),
                                                ],
                                                style = SectionFiveA()
                                            ),
                                             # Section 5b
                                            Rows(
                                                children=[
                                                    ColsTwoInner(),
                                                    
                                                ],
                                                style = SectionFiveB()
                                            ),
                                        ],
                                        style=SectionFive()
                                    ),
                                ],
                                style=Hold2N5()
                            )
                        ),
                    ],
                    justify="evenly",
                    style=HoldLR(),
                )
            ]
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True, port=2031)
