For this project I made use of Python for the creation of a fitness application.
Where the user will be able to choose the the body part that they want to work on plus choose the difficulty.
The UI is very clean and user-friendly, the user once they start the workout they will be guided on the exercise that
they have to perform.
Alongside the reps/Time they have to do it for, once the exercise is done there is a break-screen with a count down
timer, that once it reaches 0 it sends the user to the next screen that can be either the next exercise or the end of
the workout.
For the timer since Pyweb-IO doesnt support a live timer I simulated the timer by making use of the timer.sleep()
function for given seconds where the screen keeps clearing and just printing the number countdown until it reaches 0,
This helps the user to have a complete experience within the application despite the limitations of Pyweb-IO.
Also within the workout screens the user can decide to either skip a exercise or go back to a previous one through the
use of the buttons provided within the workout screen.
Other than Python I also made use of Pyweb-io for a cleaner UI.
