# Security Policy

## Supported Versions

gs_corona is in pre-1.0 development (just me scrambling to debug code), but see notes below for planned enhancements that may bring more security concerns
into relevance:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

gs_corona is a python app analyzing testing, hospitalization, cases, and deaths as reported by state and federal entities in the U.S.
It is focused on data wrangling and plotting and geographic visualization.  It is intended to be run behind a firewall, on top of Python 3.8 or later.
As such, there are few direct security concerns with the code, but since the range of apps that need to be security and privacy aware continually
expands, perhaps there are considerations of which I should be aware and make modifications.

As of July 6, 2020 as I write this, I am scrambling to get a baseline version debugged and uploaded to GitHub, after this is done (est. 1 week) I will
look at next issues:  adapting the app for more interactive use via hosting (such as via Dash or Bokeh) and corresponding security concerns.
