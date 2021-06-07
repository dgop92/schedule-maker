# Schedule Maker

Based on the idea of [Cronun](https://cronun.co/schedules), this project attempts to help students in the process of making a new schedule for the next semester.

## Project setup

The only dependency so far is xlwt

### Download the dependencies with pip

```
pip install -r requirements.txt
```

## How to use

Before starting to generate schedules, is necessary to download (scraping) the subject json files that you want in your schedule, 

subject json file structure:

```javascript
{
  "0": {
    "name": "str",
    "nrc": "str",
    "professors": [
        { "first_name": "str", "last_name": "str" },
        ...
    ],
    "schedule": [
      {
        "day": "str",
        "interval": { "start": "str", "end": "str" },
      },
      ...
    ]
  },
  "1": {
     ...
  }
},

// each item in this object represents a course of that subject
// day: M|T|W|R|F|S
// hour: HHMM, HH: military hour ex: (09, 15), MM: minutes

```

you must put these files in my_subjects folder

now you have to create a json file called my_schedule_info.json in the parent folder to specify how to create the combination of schedules

```javascript
[
    {
        "professors_to_ignored": ["str", ...],
        "subject_file_path": "my_subjects/<subject_name>.json",
        "nrc_to_ignored": ["str", ...],
    },
]

// The path to the subject file is required, the other two attributes are optional

```

finally, run the command

```
python schedule_maker.py
```

All schedules are save in my_schedules folder