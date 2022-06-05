import sys
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
)  # need version dash 2.0.0 or higher
from style.style import *

# import 'components/style' as sty

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config.suppress_callback_exceptions = True


def Containers(children):
    return dbc.Container(children=children, style=BgStyle(), fluid=True)


def ColumnSections(children, style=None, **kwargs):
    return dbc.Col(children=children, style=style, lg=6, md=6, xs=12)


def RowMains(children, style, **kwargs):
    return dbc.Row(children=children, style=style)


def Rows(children, style=None, **kwargs):
    return dbc.Row(children=children, style=style)


def Cols(children, style=None, **kwargs):
    return dbc.Col(children=children, style=style)


def ColsOne(children=None, style=None, lg=None, **kwargs):
    return dbc.Col(
        lg=lg,
        md=3,
        xs=12,
        style=SectionOneChild(),
    )


def ColsTwo(children=None, style=None, lg=None, **kwargs):
    return dbc.Col(
        lg=12,
        md=12,
        xs=12,
        style=SectionTwoParentMain(),
    )


def ColsTwoInner(children=None, style=None, lg=None, **kwargs):
    return dbc.Col(
        lg=12,
        md=12,
        xs=12,
        style=SectionTwoParent(),
    )


def SectionFiveHTML():
    return Rows(
        children=[
            # Section 5a
            Rows(
                children=[
                    ColsTwoInner(),
                ],
                style=SectionFiveA(),
            ),
            # Section 5b
            Rows(
                children=[
                    ColsTwoInner(),
                ],
                style=SectionFiveB(),
            ),
        ],
        style=SectionFive(),
    )


def SectionTwoHTML():
    return Rows(
        children=[
            ColsTwoInner(),
        ],
        style=SectionTwo(),
    )


def SectionOneHTML():
    return Rows(
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


def SectionThreeHTML():
    return ColsOne(
        children=[
            html.P("Section Three"),
            Rows(
                children=[
                    ColsOne(lg=3),
                    ColsOne(lg=3),
                    ColsOne(lg=3),
                ],
                justify="evenly",
                style=SectionOneParent(),
            ),
        ],
        lg=6,
    )


def SectionFourHTML():
    return ColsOne(
        children=[
            ColsTwoInner(),
        ],
        lg=6,
        style=SectionTwo(),
    )


def SectionSixHTML():
    return ColsOne(
        children=[
            ColsTwoInner(),
        ],
        lg=6,
        style=SectionTwo(),
    )


def SectionSevenHTML():
    return ColsOne(
        children=[
            ColsTwoInner(),
        ],
        lg=6,
        style=SectionTwo(),
    )


def SectionEightHTML():
    return Rows(
        children=[
            html.P("Left Container"),
            Rows(
                children=[ColsOne(lg=4), ColsOne(lg=4), ColsOne(lg=4)],
                justify="evenly",
                style=SectionOneParent(),
            ),
        ]
    )
