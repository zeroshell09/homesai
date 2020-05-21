inkling "2.0"

type HomeState{

    lastAction:Button,
    currentState:number,
    comfort: number
}

type Button number<Up = 0, Down = 1>

type HomeAction{
    
    topLight:Button,
    bottomLight:Button,
    leftWallLight:Button,
    rightWallLight:Button
}


simulator home_sim(Action:HomeAction):HomeState{

}

graph (input: HomeState) {

    concept FindSubjectComfort(input): HomeAction {
        curriculum  {
            
            source home_sim 
        }
    }

    output FindSubjectComfort
}