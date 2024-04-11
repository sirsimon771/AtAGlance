- event ongoing
    - allday event
        - *"today"*
    - normal event
        - *"until _time_"*

- event in future

  - allday event
    - event tomorrow
        - *"tomorrow"*
    - event not tomorrow
        - *"in X days"*
    
  - normal event
    - event today
        - *"in XhYmin"*
    - event not today
      - event tomorrow
        - event in < 12h
            - *"in XhYmin"*
        - event in > 12h
            - *"tomorrow"*
      - event not tomorrow
          - *"in X days"*


# TODO
- only "Ymin" if hours are 0
- only "Xh" if minutes are 0
- write "day" / "days"


# snippets
// check if event is today
``$df(yyMMDD, ci(start, gv(eventN))) = df(yyMMDD)$``

`// check if event is tomorrow
````