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
                                    SectionOneHTML(),
                                    Rows(
                                        children=[SectionThreeHTML(), SectionFourHTML()]
                                    ),
                                    Rows(
                                        children=[SectionSixHTML(), SectionSevenHTML()]
                                    ),
                                    SectionEightHTML(),
                                ]
                            )
                        ),
                        # rights
                        ColumnSections(
                            Rows(
                                children=[
                                    html.P("Righ Container"),
                                    # section 2
                                    SectionTwoHTML(),
                                    # section 5
                                    SectionFiveHTML(),
                                ],
                                style=Hold2N5(),
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
