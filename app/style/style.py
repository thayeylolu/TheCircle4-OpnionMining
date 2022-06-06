from turtle import position


def BgStyle():
    return {
        "background": "red",
        # "width": "100%",
        # "overflowX": "hidden",
        # "overflowY": "hidden",
        # "margin": "20px",
        "height": "100vh",
    }


def Container():
    return {
        "display": "flex",
        "justifyContent": "center",
        "alignContent": "space-between",
        "flexDirection": "row",
        "padding": 15,
        "background": "sand",
    }


def RightContainer():
    return {
        "display": "flex",
        "flex": "1",
        "align-items": "center",
        "flex-direction": "row",
        "background": "#F5F5F5",
        "border": "1px solid #000000",
    }


def LeftContainer():
    return {
        "display": "flex",
        "flex": "1.5",
        "align-items": "center",
        "flex-direction": "row",
        "background": "#F5F5F5",
        "border": "1px solid #000000",
    }


def TopInfo():
    return {
        "display": "flex",
        "flex": 1,
        "margin": "10px",
        "align-items": "start",
        "flex-direction": "row",
        "background": "#F5F5F5",
        "border": "1px solid #000000",
    }


def HighlightBoxMed():
    return {
        "display": "flex",
        "flex": "0.2",
        "margin": "10px",
        "align-items": "start",
        "flex-direction": "row",
        "background": "yellow",
        "border": "1px solid #000000",
    }


def HighlightBoxLarge():
    return {
        "display": "flex",
        "flex": "0.5",
        "margin": "10px",
        "align-items": "start",
        "flex-direction": "row",
        "background": "yellow",
        "border": "1px solid #000000",
        # "@media screen and (min-width: 320px) and (max-width: 1080px)" {
        #     "width": "100%",
        #     "height": "max-content !important"
        #     }
    }


def CircleInfo():
    return {
        "display": "flex",
        "flex": "1",
        "flex-direction": "column",
        "flex-wrap": "wrap",
        "margin": "10px",
        "align-items": "center",
        "flex-direction": "column",
        "background": "yellow",
        "border": "1px solid #000000",
        "float": "left",
    }


def SectionOneChild():
    return {
        "background": "yellow",
        "border": "1px solid #000000",
        # "margin": "5px 2px 5px 2px"
    }


def SectionOneParent():
    return {
        "background": "white",
        "height": "50px",
        "border": "1px solid #000000",
        "margin": "2px 2px 2px 2px",
        "padding": "2px"
    }


def SectionOneChild():
    return {
        "background": "yellow",
        "border": "1px solid #000000",
        # "margin": "5px 2px 5px 2px"
        "padding": "2px"
    }


def SectionTwoParent():
    return {
        "height": "50px",
        "background": "white",
        "border": "1px solid #000000",
        "margin": "2px",
        "padding": "2px"
    }

def SectionTwo():
    return {
  
        "border": "1px solid #000000",
        "margin": "2px",
         "background": "orange",
         "padding": "2px"
    }

def SectionFive():
    return {
  
        "border": "1px solid #000000",
        "margin": "2px 2px 2px 2px",
         "background": "orange",
         "padding": "2px"
    }


def SectionFiveA():
    return {
        #"height": "180px",
        "border": "1px solid #000000",
        "margin": "2px",
         "background": "green",
         "padding": "2px"
    }


def SectionFiveB():
    return {
        #"height": "180px",
        "border": "1px solid #000000",
        "margin": "2px",
         "background": "black",
         "padding": "2px"
    }


def SectionTwoParentMain():
    return {
        "height": "190px",
        "background": "white",
        "border": "1px solid #000000",
        "margin": "2px",
        "padding":"2px"
    }


def Hold2N5():
    return {
        "background": "blue",
        "margin": "2px",
         "padding":"2px"
    }

def HoldLR():
    return {
        "background": "grey",
    }