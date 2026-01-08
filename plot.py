import matplotlib.pyplot as plt

def line_plot(df):
    fig, ax = plt.subplots()
    df.plot(y="Close",kind="line",ax=ax)
    ax.set_xlabel("Dates")
    ax.set_ylabel("Prices")
    ax.set_title("Closing Price")
    return fig
def daily_plot(df):
    fig, ax = plt.subplots()
    df.plot(y="Daily Return", kind="line", ax=ax)
    ax.set_xlabel("Dates")
    ax.set_ylabel("Returns")
    ax.set_title("Daily Returns")
    return fig
def cumm_plot(df):
    fig, ax = plt.subplots()
    df.plot(y="Cummulative", kind="line", ax=ax)
    ax.set_xlabel("Dates")
    ax.set_ylabel("Cummulative Returns")
    ax.set_title("Cummulative Return")
    return fig

def MA_plot(df):
    fig, ax = plt.subplots()
    df.plot(y="MA", kind="line", ax=ax)
    ax.set_xlabel("Dates")
    ax.set_ylabel("Averages")
    ax.set_title("Moving Average")
    return fig