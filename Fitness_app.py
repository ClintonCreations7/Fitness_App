from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
import time

workouts={
    'Upper':{
        'Easy':[
            {'name': 'Knee push-ups','type':'reps', 'value':'10'},
            {'name': 'Wall push-ups', 'type': 'reps', 'value':'10'},
            {'name': 'Arm circles', 'type': 'time', 'value':'10'}
        ],
        'Medium':[
            {'name': 'Regular push-ups','type':'reps', 'value':'10'},
            {'name': 'Triceps dips','type':'reps', 'value':'15'},
            {'name': 'Plank hold','type':'time', 'value':'30'},
            {'name': 'Pike push-ups','type':'reps', 'value':'10'}
        ],
        'Hard':[
            {'name': 'Regular push-ups','type':'reps', 'value':'25'},
            {'name': 'Elevated push-ups','type':'reps', 'value':'15'},
            {'name': 'Pike push-ups','type':'reps', 'value':'15'},
            {'name': 'One arm push-ups','type':'reps', 'value':'X5 each side'},
            {'name': 'Plank hold','type':'time', 'value':'60'}
        ]
    },
    'Lower':{
        'Easy':[
            {'name': 'Squats','type':'reps', 'value':'20'},
            {'name': 'Lunges','type':'reps', 'value':'15'},
            {'name': 'Glute bridges','type':'reps', 'value':'20'},
        ],
        'Medium':[
            {'name': 'Squats','type':'reps', 'value':'30'},
            {'name': 'Jump squats','type':'reps', 'value':'10'},
            {'name': 'Lunges','type':'reps', 'value':'20'},
            {'name': 'Glute bridges','type':'reps', 'value':'25'},
            {'name': 'Squats','type':'reps', 'value':'20'},
            {'name': 'Wall sit','type':'time', 'value':'30'}
        ],
        'Hard':[
            {'name': 'Squats','type':'reps', 'value':'50'},
            {'name': 'Jump squats','type':'reps', 'value':'25'},
            {'name': 'Jump squats','type':'reps', 'value':'20'},
            {'name': 'Jumping lunges','type':'reps', 'value':'20'},
            {'name': 'Burpees high knees','type':'reps', 'value':'10'},
            {'name': 'Burpees jump squats','type':'reps', 'value':'10'},
            {'name': 'Wall sit','type':'time', 'value':'60'}
        ]
    },
    'Full':{
        'Easy':[
            {'name': 'Knee push-ups','type':'reps', 'value':'10'},
            {'name': 'Jumping jacks', 'type':'time', 'value':'20'},
            {'name': 'Squats','type':'reps', 'value':'10'},
            {'name': 'Side lunges','type':'reps', 'value':'10'}
        ],
        'Medium':[
            {'name': 'Regular push-ups','type':'reps', 'value':'10'},
            {'name': 'abs crunches','type':'reps', 'value':'25'},
            {'name': 'Regular push-ups','type':'reps', 'value':'10'},
            {'name': 'Jumping Squats','type':'reps', 'value':'10'},
            {'name': 'Burpees','type':'reps', 'value':'10'}
        ],
        'Hard':[
            {'name': 'Regular push-ups','type':'reps', 'value':'20'},
            {'name': 'Elevated push-ups','type':'reps', 'value':'15'},
            {'name': 'Abs bicycles','type':'time', 'value':'30'},
            {'name': 'Jumping squats','type':'reps', 'value':'15'},
            {'name': 'Jumping Lunges','type':'reps', 'value':'15'},
            {'name': 'Wall sit','type':'time', 'value':'60'},
            {'name': 'Burpees','type':'reps', 'value':'20'},
        ]
    },
    'Abs':{
        'Easy':[
            {'name': 'Standed Skips','type':'reps', 'value':'15'},
            {'name': 'Abs crunches','type':'reps', 'value':'10'},
            {'name': 'Abs bicycles','type':'time', 'value':'20'},
            {'name': 'Abs crunches','type':'reps', 'value':'10'}
        ],
        'Medium':[
            {'name': 'Standed Skips','type':'reps', 'value':'20'},
            {'name': 'Abs crunches','type':'reps', 'value':'20'},
            {'name': 'Abs bicycles','type':'time', 'value':'30'},
            {'name': 'Mountain climbers','type':'time', 'value':'30'},
            {'name': 'In and outs','type':'reps', 'value':'10'},
            {'name': 'Plank hold','type':'time', 'value':'30'}
        ],
        'Hard':[
            {'name': 'Abs crunches','type':'reps', 'value':'40'},
            {'name': 'Abs bicycles','type':'time', 'value':'30'},
            {'name': 'In and outs','type':'reps', 'value':'20'},
            {'name': 'Abs crunches','type':'reps', 'value':'40'},
            {'name': 'Mountain climbers','type':'time', 'value':'60'},
            {'name': 'Plank hold','type':'time', 'value':'120'}
        ]
    },
    'Cardio':{
        'Easy':[
            {'name': 'Jumping jacks','type':'time', 'value':'30'},
            {'name': 'High knees','type':'time', 'value':'30'},
            {'name': 'Mountain climbers','type':'time', 'value':'30'},
            {'name': 'Burpees','type':'reps', 'value':'20'}
        ],
        'Medium':[
            {'name': 'Jog in place','type':'time', 'value':'60'},
            {'name': 'Burpees','type':'reps', 'value':'15'},
            {'name': 'Skater jumps','type':'time', 'value':'15'},
            {'name': 'Burpees','type':'reps', 'value':'20'},
            {'name': 'Mountain climbers','type':'time', 'value':'40'}
        ],
        'Hard':[
            {'name': 'Jog in place','type':'time', 'value':'60'},
            {'name': 'Burpees','type':'reps', 'value':'20'},
            {'name': 'Burpees high knees','type':'reps', 'value':'10'},
            {'name': 'Skater jumps','type':'time', 'value':'30'},
            {'name': 'Burpees','type':'reps', 'value':'20'},
            {'name': 'Mountain climbers','type':'time', 'value':'60'},
            {'name': 'Burpees','type':'reps', 'value':'20'}
        ]
    }
}

def home_page():
    clear()
    put_html("<h1>Welcome to Fitness plus, please choose the type of work-out you want to do :</h1>")
    put_buttons(['Upper', 'Lower', 'Full body'], onclick=[choose_difficulty_Upper, choose_difficulty_Lower, choose_difficulty_Full])
    put_buttons(['Abs', 'Cardio'], onclick=[choose_difficulty_Abs, choose_difficulty_Cardio])

def choose_difficulty_Upper():
    clear()
    put_html("<h1>Choose workout difficulty:</h1>")
    put_buttons(['Easy', 'Medium', 'Hard'], onclick=[lambda: start_workout('Upper','Easy'),
                                                     lambda: start_workout('Upper', 'Medium'),
                                                     lambda: start_workout('Upper', 'Hard')])
    put_buttons(['back'], onclick=[home_page])

def choose_difficulty_Lower():
    clear()
    put_html("<h1>Choose workout difficulty:</h1>")
    put_buttons(['Easy', 'Medium', 'Hard'],  onclick=[lambda: start_workout('Lower', 'Easy'),
                                   lambda: start_workout('Lower', 'Medium'),
                                   lambda: start_workout('Lower', 'Hard')])
    put_buttons(['back'], onclick=[home_page])

def choose_difficulty_Full():
    clear()
    put_html("<h1>Choose workout difficulty:</h1>")
    put_buttons(['Easy', 'Medium', 'Hard'], onclick=[lambda: start_workout('Full', 'Easy'),
                                                     lambda: start_workout('Full', 'Medium'),
                                                     lambda: start_workout('Full', 'Hard')])
    put_buttons(['back'], onclick=[home_page])

def choose_difficulty_Abs():
    clear()
    put_html("<h1>Choose workout difficulty:</h1>")
    put_buttons(['Easy', 'Medium', 'Hard'], onclick=[lambda: start_workout('Abs', 'Easy'),
                                                     lambda: start_workout('Abs', 'Medium'),
                                                     lambda: start_workout('Abs', 'Hard')])
    put_buttons(['back'], onclick=[home_page])

def choose_difficulty_Cardio():
    clear()
    put_html("<h1>Choose workout difficulty:</h1>")
    put_buttons(['Easy', 'Medium', 'Hard'], onclick=[lambda: start_workout('Cardio', 'Easy'),
                                                     lambda: start_workout('Cardio', 'Medium'),
                                                     lambda: start_workout('Cardio', 'Hard')])
    put_buttons(['back'], onclick=[home_page])

def start_workout(workout_type, difficulty, index=0):
    clear()
    exercises=workouts[workout_type][difficulty]
    if index>=len(exercises):
        end_screen()
        return

    exercise=exercises[index]
    name=exercise['name']
    reps_or_time=exercise['value']
    ex_type=exercise['type']

    put_html(f"<h2>{name}</h2>")
    put_text(f"{'Reps' if ex_type=='reps' else 'Time'}: {reps_or_time}")

    last=(index+1 >= len(exercises))

    if ex_type=='reps':
        put_buttons(['Done', 'Skip', 'Previous'], onclick=[
            lambda: end_screen() if last else break_screen(workout_type, difficulty, index + 1),
            lambda: end_screen() if last else start_workout(workout_type, difficulty, max(0, index + 1)),
            lambda: start_workout(workout_type, difficulty, max(0, index - 1)),
        ])

    elif ex_type=='time':
        action = actions('', buttons=[
            {'label': 'Skip', 'value': 'skip'},
            {'label': 'Previous', 'value': 'previous'},
            {'label': 'Start', 'value': 'start'},
        ], help_text='Choose an option')

        if action=='skip':
            if last:
                end_screen()
            else:
                start_workout(workout_type, difficulty, index+1)
            return
        elif action =='previous':
            start_workout(workout_type, difficulty, max(0, index -1))
            return


        duration = int(reps_or_time)
        for i in range(duration, 0, -1):
            clear()
            put_html(f"<h2>{name}</h2>")
            put_text(f"Time remaining: {i} seconds")
            time.sleep(1)

        go_next(workout_type, difficulty, index)

def go_next(workout_type, difficulty, current_index):
    exercises= workouts[workout_type][difficulty]
    if current_index + 1 >=len(exercises):
        end_screen()
    else:
        break_screen(workout_type, difficulty, current_index + 1)


def break_screen(workout_type, difficulty, next_index):
    clear()
    put_html("<h3>Break Time - 10 seconds</h3>")
    for i in range(30, 0, -1):
        clear()
        put_html(f"<h3>Break: {i} Seconds remaining...</h3>")
        time.sleep(1)
    start_workout(workout_type, difficulty, next_index)

def end_screen():
    clear()
    put_html("<h2>Workout complete</h2>")
    put_buttons(['Home'], onclick=[home_page])





if __name__ == '__main__':
    start_server(home_page, port=8080)
